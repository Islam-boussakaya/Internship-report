#!/usr/bin/env python
# coding: utf-8

# ## The Kloppy Package
# 
# ### What is Kloppy ?
# 
# As previously mentioned kloppy is a great package , It provides (de)serializers, standardized data models, filters, and transformers to facilitate work with different tracking and event data from various providers,So its main features are to load data and transform it into standardized models and vice versa.
# 
# 
# ### Kloppy providers
# 
# |Provider|Format|
# |--------|------|
# |Datafactory|JSON|
# |Metrica|JSON
# |Opta|LXML|
# |Sportec|LXML|
# |Statsbomb|JSON|
# |Wyscout|JSON|
# 
# *The table below shows the providers supported by kloppy.*
# 
# To simplify the process, these providers display a different data structure within each format, "Kloppy" will proceed with each one to provide the same final result structure for each game. We will work with the events & line-up data.
# 
# ### What is events & line-up data in football?
# * Events Data  
# Event data can be considered as a record of the entire game, it records every move on the pitch during the match. It includes the positions of each player and data pertaining to every action during the match which include pass, shot, interception, card, goal etc.
# * Line-up Data
# The line-up data contain the lineup of players, starting & ending tactic . It includes player information full name , jersey number , starting & ending position etc.
# 
# ### Example
# To better understand what we are looking for as a result here an code example and its output.
# 
# ![optaexp](img/optaexp.png)
# 
# 
# ### Kloppy Structure
# 
# #### Events types
# "Kloppy" classifies events depending on the type of event.
# For each event type kloppy defines a class that we will detail.
# 
# |Events Types|
# |------------|
# |Pass|
# |Shot|
# |Take on|
# |Carry|
# |Substitution|
# |PlayerOn/Off|
# |Card|
# |Recovery|
# |Ball Out|
# |Foul Committed|
# |Generic|
# 
# *Events types that kloppy is using*
# 
# ##### Pass Event
# A enumeration class named "Pass Type", Which consists of:
# * recieve timestamp
# * receiver player
# * receiver coordinates **Point**
# * result **Pass Result**
# 
# ######  Pass Type
# |PassType|
# |--------|
# |Cross|
# |Hand pass|
# |Head pass|
# |High pass|
# |Launch|
# |Simple pass|
# |Smart pass|
# |Long pass|
# |Through ball|
# |Chipped pass|
# |Flick on|
# |Assit|
# |Assist 2nd|
# |Swithc of play|
# 
# ###### Pass Result
# 
# |Attribute|Definition|
# |---------|----------|
# |COMPLETE|Complete pass|
# |INCOMPLETE|Incomplete pass (intercepted)|
# |OUT|Ball went out|
# |OFFSIDE|Offside|
# 
# ##### Shot Event
# A Class named "Shot Event" , it contains as attributes :
# * result of the shot as **shot Result**
# * result coordinates **Point**
# ###### Shot Result
# 
# |Attribute|Definition|
# |---------|----------|
# |Goal|Shot resulted in a goal|
# |OFF_TARGET|Shot was off target|
# |Post|Shot hit the post|
# |BLOCKED|Shot was blocked by another player|
# |SAVED|Shot was saved by the keeper|
# 
# ##### Take on Event
# A class named "Take on Event", it conatins as attributes :
# * result of the take on **Take on Result**
# ###### Taken on Result
# 
# |Attribute|Definition|
# |---------|----------|
# |Complete|Complete take-on|
# |Incomplete|Incomplete take-on|
# |Out|Ball went out|
# 
# ##### Carry Event 
# A Class named "Carry Event", it contains as attributes:
# * end timestamp 
# * end coordinates **Point**
# * Result **Carry Result**
# 
# ###### Carry Result
# 
# |Attribute|Definition|
# |---------|----------|
# |Complete|Complete carry|
# |Incomplete|Incomplete carry|
# 
# ##### Substitution Event
# A Class named "Substitution Event", it contains as attribute:
# * replacement player **Player**
# 
# ##### Player On/Off Event
# Two classes "PlayerOn Event" & "PlayerOff Event" that contains as attribute:
# * Event type that the player is concerned on/off
# 
# ##### Card Event
# A class named "Card Event", it contains as attribute:
# * card type **Card Type**
# 
# |Attribute|Definition|
# |---------|----------|
# |FIRST_YELLOW|First yellow card|
# |SECOND_YELLOW|Second yellow card|
# |RED|Red card|
# 
# *Class Cardtype*
# 
# ##### Recovery Event
# A class named "Recovery Event", it contains as attribute:
# * Event type **Recovery**
# 
# ##### Ball out Event
# A class named "Ball out Event", it contains as attribute:
# * Event type **Ball out**
# 
# ##### Foul Commit Event
# A class named "Foul Commit Event", it contains as attribute:
# * Event type **Foul Commit**
# 
# ##### Generic Event
# Kloppy classifies an event which does not match the above mentioned events (Unrecognised event type) as a generic event.
# 
# #### Qualifiers
# Each type of event will be qualified with one or more qualifiers.
# 
# |Qualifiers||
# |------------|-|
# |Set Piece|Corner / FreeKick / Penalty /Throw in /KickOff|
# |Body Part|Chest / Right Foot / Left Foot / Head|
# |Pass Type|Cross / LongBall /ThroughBall / Launch / ChippedBall / Assist / 2nd Assist /SwitchOfPlay |
# 
# *Qualifiers types that kloppy is using*
# 
# #### The Kloppy Coordinates System
# Kloppy is using TRACAB meters pitch dimensions.
# #### Dependencies
# Python libraries that Kloppy depend on 
# * Black  
# Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting.
# Black makes code review faster by producing the smallest diffs possible.
# * Lxml 
# The lxml XML toolkit is a Pythonic binding for the C libraries libxml2 and libxslt. It is unique in that it combines the speed and XML feature completeness of these libraries with the simplicity of a native Python API, mostly compatible but superior to the well-known ElementTree API.
# * Requests 
# Python module that you can use to send all kinds of HTTP requests. It is an easy-to-use library with a lot of features ranging from passing parameters in URLs to sending custom headers and SSL Verification.
# * NetworkX
# This python package is used for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. It is used to study large complex networks represented in form of graphs with nodes and edges. Using networkx we can load and store complex networks.
# * PyTest 
# PyTest is a testing framework that allows users to write test codes using Python programming language. It helps you to write simple and scalable test cases for databases, APIs, or UI. PyTest is mainly used for writing tests for APIs. It helps to write tests from simple unit tests to complex functional tests.
# * Pandas
# pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real-world data analysis in Python.
# * Pre-commit
# A framework for managing and maintaining multi-language pre-commit Git hooks.
# 
# 
# 
# ## The InStat Provider
# 
# 
# ### What is InStat ?
# 
# InStat is a worldwide sports performance analysis company, it prepares statistics for pre-game analysis, collects data during games and breaks down the game after it is completed.
# 
# ### InStat File Structure
# #### Line-up 
# 
# ![lineupfile](img/lineupxml.png)
# *This a sample of the lineup XML file*
# 
# #### Events
# ![eventsfile](img/eventsxml.png)
# *This a sample of the events XML file*
# 
# * Each row is considered an event that occurred within the match, every action has the following characteristics: time, type of action , place on the pitch, the player who committed it, the opponent (in the case of challenges).
# 
# #### InStat Actions
# InStat has a specific way of structuring events as well as its type of action.
# 
# |GENERIC ACTION| ACTION|
# |--------------|-------|
# |Pass| Attacking pass - Key pass - Assist - Key Assit|
# |Challenge| Challenge - Air challenge - Tackle - Dribble |
# |Disipline| Yellow card - Red card - RC for 2 YC| 
# |Shot| Shot on target - Shot into the bar - Shot blocked|
# |Set Piece|Open play - Throw-in - Free-Kick - Corner|
# |Goal|Goal - Own goal|
# |Cross|Cross accurate - cross accurate|
# 
# *InStat actions that we will use in kloppy*

# In[ ]:




