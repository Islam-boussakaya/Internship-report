---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

## The InStat Provider

### What is InStat ?
InStat is a worldwide sports performance analysis company, it prepares statistics for pre-game analysis, collects data during games and breaks down the game after it is completed.

### InStat Files
As we mentionned before we will analyze the line-up & events file.

#### Line-up 
```{figure} img/lineupxml.png
---
name: lineupfile-fig
---
This a sample of the lineup XML file
```

#### Events
Each row is considered an event that occurred within the match, every action has the following characteristics: time, type of action , place on the pitch, the player who committed it, the opponent (in the case of challenges).
```{figure} img/eventsxml.png
---
name: lineupfile-fig
---
This a sample of the events XML file
```
### InStat Actions
InStat has a specific way of structuring events as well as its type of action, each action has a specefic identifier .

|GENERIC ACTION| ACTION|
|--------------|-------|
|Pass| Attacking pass - Key pass - Assist - Key Assit|
|Challenge| Challenge - Air challenge - Tackle - Dribble |
|Disipline| Yellow card - Red card - RC for 2 YC| 
|Shot| Shot on target - Shot into the bar - Shot blocked|
|Set Piece|Open play - Throw-in - Free-Kick - Corner|
|Goal|Goal - Own goal|
|Cross|Cross accurate - cross accurate|

### InStat Coordinates System
The Coordinates system is X,Y coordinates of the player on the pitch , it refers to his position.
The origin of the coordinates is in the bottom left and the vertical orientation is from bottom to top of the pitch. The dimension of the picth is 105 * 68 .
```{figure} img/pitch.png
---
name: pitch-fig
---
InStat pitch representation. 
```

### InStat Standart
Every event is qualified with a standart name as the following table shows.

|Standart name|
|-------------|
|Open Play|
|Throw-in|
|Indirect Freekick|
|Direct free kick|
|Corner|

### InStat Body Part
Every event is qualified with a Body name that reffers to the body part as the following table shows.

|Body name|
|-------------|
|Right foot|
|Left foot|
|Header|
|Hand|
|Other body part|
