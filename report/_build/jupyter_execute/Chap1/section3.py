#!/usr/bin/env python
# coding: utf-8

# ## Workflow
# In this section, we will describe in detail the approach adopted.
# ### Instat Inputs
# Every provider in Kloppy has an input class that contains the files that will be used. We created the InStatInputs class which has as attributes the file line-up and events as the following code states.
# ```python
# class InStatInputs(NamedTuple):
#     lineup_data: IO[bytes]
#     events_data: IO[bytes]
# ```
# ### Coordinates System
# Each provider has its own coordinate system, so we defined a data class that that specifies the pitch parameters.
# ```python
# @dataclass
# class InstatCoordinateSystem(CoordinateSystem):
#     @property
#     def provider(self) -> Provider:
#         return Provider.INSTAT
# 
#     @property
#     def origin(self) -> Origin:
#         return Origin.BOTTOM_LEFT 
# 
#     @property
#     def vertical_orientation(self) -> VerticalOrientation:
#         return VerticalOrientation.BOTTOM_TO_TOP
# 
#     @property
#     def pitch_dimensions(self) -> PitchDimensions:
#         return PitchDimensions(
#             x_dim=Dimension(0, 105),
#             y_dim=Dimension(0, 68),
#         )
# ```
# ### Action Id
# In this section, we will try to match the types of InStat events and actions to Kloppy classes in order to proceed with the deserialization process.
# We have created a file called "InStat Events" that contains all types of events with their identifiers.
# This is a sample of the code.
# ```python
# EVENT_TYPE_BALL_OUT = "27000"
# EVENT_TYPE_CORNER_AWARDED ="5060"
# BALL_OUT_EVENTS = [EVENT_TYPE_BALL_OUT, EVENT_TYPE_CORNER_AWARDED]
# 
# EVENT_BODYPART_RIGHT_FOOT = 1
# EVENT_BODYPART_LEFT_FOOT = 2
# EVENT_BODYPART_HEADER = 3
# EVENT_BODYPART_BODY = 4
# EVENT_BODYPART_HAND = 5
# 
# SET_PIECE_THROW_IN = 2
# SET_PIECE_INDIRECT_FREE_KICK = 3
# SET_PIECE_DIRECT_FREE_KICK = 4
# SET_PIECE_CORNER = 5
# 
# ```
# ### Qualifiers Functions
# Qualifiers describe each single event with one or more of these following qualifiers (Body part, Card, Set piece and Pass).
# #### Body Part Qualifier
# This qualifier function returns which body part is used with each event.
# ```python
# def _get_event_bodypart(body_id : int) -> List[Qualifier]:
#     qualifiers =  []
#     if body_id == instat_events.EVENT_BODYPART_RIGHT_FOOT:
#         qualifiers.append(BodyPartQualifier(value=BodyPart.RIGHT_FOOT))
#     elif body_id == instat_events.EVENT_BODYPART_LEFT_FOOT:
#         qualifiers.append(BodyPartQualifier(value=BodyPart.LEFT_FOOT))
#     elif body_id == instat_events.EVENT_BODYPART_HEADER:
#         qualifiers.append(BodyPartQualifier(value=BodyPart.HEAD))
#     elif body_id == instat_events.EVENT_BODYPART_BODY :
#         qualifiers.append(BodyPartQualifier(value=BodyPart.OTHER))
#     elif body_id == instat_events.EVENT_BODYPART_HAND :
#         qualifiers.append(BodyPartQualifier(value=BodyPart.OTHER))
#     
#     return qualifiers
# ```
# #### Card Qualifier
# This qualifier function returns which card type is used with each card event.
# ```python
# def _get_event_card(action_id : str) -> List[Qualifier]:
#     qualifiers =  []
#     if action_id == instat_events.EVENT_TYPE_RED_CARD:
#         qualifiers.append(CardQualifier(value=CardType.RED))
#     elif action_id == instat_events.EVENT_TYPE_SECOND_YELLOW_CARD:
#         qualifiers.append(CardQualifier(value=CardType.SECOND_YELLOW))
#     elif action_id == instat_events.EVENT_TYPE_FIRST_YELLOW_CARD:
#         qualifiers.append(CardQualifier(value=CardType.FIRST_YELLOW))
#     return qualifiers
# ```
# #### Pass Qualifier
# This qualifier function returns the type of the pass concerned with each pass event.
# ```python
# def _get_event_pass(action_id : str) -> List[Qualifier]:
#     qualifiers =  []
#     if action_id in instat_events.EVENT_TYPE_CROSS:
#         qualifiers.append(PassQualifier(value=PassType.CROSS))
#     elif action_id in instat_events.EVENT_TYPE_ASSIST:
#         qualifiers.append(PassQualifier(value=PassType.ASSIST))
#     elif action_id in instat_events.EVENT_TYPE_ASSISIT_2ND:
#         qualifiers.append(PassQualifier(value=PassType.ASSIST_2ND))
#     return qualifiers
# ```
# #### Set Piece Qualifier
# As we mentioned previously, the equivalent of set piece in Instat is **standart**.
# This qualifier function returns the type of the set piece concerned with each event.
# ```python
# def _get_event_setpiece(standart_id) -> List[Qualifier]:
#     qualifiers = []
#     if standart_id == instat_events.SET_PIECE_CORNER:
#         qualifiers.append(SetPieceQualifier(value=SetPieceType.CORNER_KICK))
#     elif standart_id == instat_events.SET_PIECE_DIRECT_FREE_KICK:
#         qualifiers.append(SetPieceQualifier(value=SetPieceType.FREE_KICK))
#     elif standart_id == instat_events.SET_PIECE_INDIRECT_FREE_KICK:
#         qualifiers.append(SetPieceQualifier(value=SetPieceType.FREE_KICK))
#     elif standart_id == instat_events.SET_PIECE_THROW_IN:
#         qualifiers.append(SetPieceQualifier(value=SetPieceType.THROW_IN))
#     return qualifiers
# ```
# 
# ### Parse Functions
# The parse functions are used to retrieve data from the file to specific classes set by kloppy.
# This is where de-serialization takes its parts and transforms the data extracted from the XML file into the classes identified by KLoppy.
# As stated in the preceding chapter, Qualifier describes each event type with the correspondents qualifiers.
# #### Parse Team
# This function identifies the team (id, name, ground, team side and starting formation) & players of the team (player id, team, jersey number, first name, last name, starting, position) as the following code shows.
# 
# ```python
# def _parse_team(team_root , team_side
#                 )-> Team:
#     team_id = team_root.attrib["id"]
#     formation = "-".join(re.findall(r'\d+', team_root.lineup.main.attrib["starting_tactic"]))
#     team = Team(
#         team_id=str(team_id),
#         name=team_root.attrib["name"],
#         ground=Ground.HOME
#         if str(team_side) == "first_team"
#         else Ground.AWAY,
#         starting_formation=FormationType(formation),
#     )
#     team.players = [
#         Player(
#             player_id=player_elm.attrib["id"],
#             team=team,
#             jersey_no=int(player_elm.attrib["num"]),
#             first_name=player_elm.attrib["firstname"],
#             last_name=player_elm.attrib["lastname"],
#             starting=True if player_elm.attrib["starting_lineup"] == 1 else False,
#             position=Position(
#                 position_id=player_elm.attrib["starting_position_id"],
#                 name=player_elm.attrib["starting_position_name"],
#                 coordinates=None,
#             ),
#         )
#         for player_elm in team_root.lineup.main.iterchildren("player")
#     ]
#     return team , team_id
# ```
# 
# #### Parse Score
# This function returns the score of both teams, the home and away team.
# ```python
# def _parse_score (events_root,home_team_id,away_team_id):
#     
#     home_score = 0
#     away_score = 0
#     try:
#         for event in events_root.iterchildren("row"):
#             if event.attrib["action_id"]=="8010" and event.attrib["team_id"]==str(home_team_id):
#                 home_score +=1
#             elif event.attrib["action_id"]=="8010" and event.attrib["team_id"]==str(away_team_id):
#                 away_score +=1
#     
#     except KeyError:
#         pass
#     return home_score,away_score
# ```
# #### Parse Card
# This function returns the type of the card.
# ```python
# def _get_event_card(action_id : str) -> List[Qualifier]:
#     qualifiers =  []
#     if action_id == instat_events.EVENT_TYPE_RED_CARD:
#         qualifiers.append(CardQualifier(value=CardType.RED))
#     elif action_id == instat_events.EVENT_TYPE_SECOND_YELLOW_CARD:
#         qualifiers.append(CardQualifier(value=CardType.SECOND_YELLOW))
#     elif action_id == instat_events.EVENT_TYPE_FIRST_YELLOW_CARD:
#         qualifiers.append(CardQualifier(value=CardType.FIRST_YELLOW))
#     return qualifiers
# ```
# 
# #### Parse pass
# This function takes as an input a pass event and the action id, it returns the attributes used in the Pass Event class.
# 
# ```python
# def _parse_pass(action_id: str, row_elm) -> Dict:
#     if action_id in instat_events.EVENT_TYPE_CROSS:
#         if action_id in instat_events.EVENT_TYPE_CROSS_INCOMPLETE:
#             result = PassResult.INCOMPLETE
#         elif action_id in instat_events.EVENT_TYPE_CROSS_COMPLETE:
#             result = PassResult.COMPLETE    
#     elif action_id in instat_events.EVENT_TYPE_ASSIST:
#         result = PassResult.COMPLETE    
#     elif action_id in instat_events.EVENT_TYPE_ASSISIT_2ND:
#         result = PassResult.COMPLETE   
#         
#     receiver_coordinates = Point(
#             x=float(row_elm.attrib["pos_dest_x"]), y=float(row_elm.attrib["pos_dest_y"])
#         )
#     qualifiers = _get_event_qualifiers(row_elm)
#     
#     return dict(
#         result=result,
#         receiver_coordinates=receiver_coordinates,
#         receiver_player=None,
#         receive_timestamp=None,
#         qualifiers=qualifiers,
#     )
# ```
# #### Parse shot
# This function takes as an input a shot event, the action id, and the coordinates. It returns the attributes used in the Shot Event class.
# 
# ```python
# def _parse_shot(
#             action_id: str, 
#             coordinates: Point, 
#             row_elm
#                ) -> Dict:
#     if action_id == instat_events.EVENT_TYPE_SHOT_GOAL:
#         result = ShotResult.GOAL
#     elif action_id == instat_events.EVENT_TYPE_SHOT_OWN_GOAL:
#         result = ShotResult.OWN_GOAL
#     elif action_id == instat_events.EVENT_TYPE_SHOT_BLOCKED:
#         result = ShotResult.BLOCKED
#     elif action_id == instat_events.EVENT_TYPE_SHOT_POST:
#         result = ShotResult.POST
#     elif action_id == instat_events.EVENT_TYPE_SHOT_SAVED:
#         result = ShotResult.SAVED
#     else:
#         result = None
#     qualifiers = _get_event_qualifiers(row_elm)
#     return dict(
#         coordinates=coordinates, 
#         result=result,
#         qualifiers=qualifiers)
# ```
# #### Parse take-on
# This function takes as an input the action id and it returns the result of the take on.
# 
# ```python
# def _parse_take_on(action_id: str) -> Dict:
#     if action_id in instat_events.EVENT_TYPE_TAKE_ON_COMPLETE:
#         result = TakeOnResult.COMPLETE
#     elif action_id == instat_events.EVENT_TYPE_TAKE_ON_INSUCC_DRIBBLING:
#         result = TakeOnResult.INCOMPLETE
#     return dict(result=result)
# ```
# 
# ### InStat Deserializer 
# It is the final class that includes all previous sections and will return the final Dataset after the de-serialization process took part.
# ```python
# return EventDataset(
#             metadata=metadata,
#             records=events,
#         )
# ```
# **EventDataset** is a data class that contains the metadata & records of the game.
# #### Metadata
# The Metadata contains both team (home & away team), Period (timestamp of the first & second half), Score of the game, coordiantes system of Instat .
# ```python
# metadata = Metadata(
#             teams=teams,
#             periods=periods,
#             pitch_dimensions=transformer.get_to_coordinate_system().pitch_dimensions,
#             score=score,
#             frame_rate=None,
#             orientation=Orientation.ACTION_EXECUTING_TEAM,
#             flags=DatasetFlag.BALL_OWNING_TEAM,
#             provider=Provider.INSTAT,
#             coordinate_system=transformer.get_to_coordinate_system(),
#         )
# ```
# #### Records
# The records refer to the list of events after it is generated (de-serialized) into Kloppy classes.
