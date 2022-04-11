#!/usr/bin/env python
# coding: utf-8

# ## The Kloppy Package
# 
# ### What is Kloppy ?
# 
# As previously mentioned kloppy is a great package , It provides (de)serializers, standardized data models, filters, and transformers to facilitate work with different tracking and event data from various providers,So its main features are to load data and transform it into standardized models and vice versa.
# In the following sections we will try to break-down the package to better understand the process and it works.
# 
# 
# ### Kloppy providers
# Kloppy support numerous provider with different format file (JSON & LXML) as the table below shows.
# To simplify the process, these providers display a different data structure within each format, "Kloppy" will proceed with each one to provide the same final result structure for each game. 
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
# ### What is events & line-up data in football?
# * Events Data  
# Event data can be considered as a record of the entire game, it records every move on the pitch during the match. It includes the positions of each player and data pertaining to every action during the match which include pass, shot, interception, card, goal etc.
# * Line-up Data
# The line-up data contain the lineup of players, starting & ending tactic . It includes player information full name , jersey number , starting & ending position etc.
# 
# ### Example
# To better understand what we are looking for as a result here an code example and its output.
# ```{figure} img/optaexp.png
# ---
# name: optaexp-fig
# ---
# Code exemple of Opta provider. Using filter for event types as pass and shot. 
# ```
# 
# ### Kloppy Event Types
# 
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
# #### Pass Event
# A class entitled "Pass Event" contains the following attributes:
# * recieve timestamp
# * receiver player
# * receiver coordinates **Point**
# * result **Pass Result**
# 
# |Attribute|Definition|
# |---------|----------|
# |COMPLETE|Complete pass|
# |INCOMPLETE|Incomplete pass (intercepted)|
# |OUT|Ball went out|
# |OFFSIDE|Offside|
# 
# * Pass type, a enumeration class named "Pass Type"
# 
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
# #### Shot Event
# A class entitled "Shot Event" contains the following attributes:
# 
# * result of the shot as **shot Result**
# 
# |Attribute|Definition|
# |---------|----------|
# |Goal|Shot resulted in a goal|
# |Ooff targer|Shot was off target|
# |Post|Shot hit the post|
# |Blocked|Shot was blocked by another player|
# |Saved|Shot was saved by the keeper|
# 
# * result coordinates **Point**
# 
# 
# #### Take on Event
# A class entitled "Take-on Event" contains the following attributes:
# * result of the take on **Take on Result**
# 
# |Attribute|Definition|
# |---------|----------|
# |Complete|Complete take-on|
# |Incomplete|Incomplete take-on|
# |Out|Ball went out|
# 
# #### Carry Event 
# A class entitled "Carry Event" contains the following attributes:
# 
# * end timestamp 
# * end coordinates **Point**
# * Result **Carry Result**
# 
# |Attribute|Definition|
# |---------|----------|
# |Complete|Complete carry|
# |Incomplete|Incomplete carry|
# 
# #### Substitution Event
# A class entitled "Substitution Event" contains as attribute:
# * replacement player **Player**
# 
# #### Player On/Off Event
# Two classes "PlayerOn Event" & "PlayerOff Event" that contains as attribute:
# * Event type that the player is concerned on/off
# 
# #### Card Event
# A class named "Card Event", it contains as attribute:
# * card type **Card Type**
# 
# |Attribute|Definition|
# |---------|----------|
# |FIRST_YELLOW|First yellow card|
# |SECOND_YELLOW|Second yellow card|
# |RED|Red card|
# 
# 
# #### Recovery Event
# A class named "Recovery Event", it contains as attribute:
# * Event type **Recovery**
# 
# #### Ball out Event
# A class named "Ball out Event", it contains as attribute:
# * Event type **Ball out**
# 
# #### Foul Commit Event
# A class named "Foul Commit Event", it contains as attribute:
# * Event type **Foul Commit**
# 
# #### Generic Event
# Kloppy classifies an event which does not match the above mentioned events (Unrecognised event type) as a generic event.
# 
# ### Kloppy qualifiers
# Each type of event will be qualified with one or more of the following qualifiers.
# 
# |Qualifiers||
# |------------|-|
# |Set Piece|Corner / FreeKick / Penalty /Throw in /KickOff|
# |Body Part|Chest / Right Foot / Left Foot / Head|
# |Pass Type|Cross / LongBall /ThroughBall / Launch / ChippedBall / Assist / 2nd Assist /SwitchOfPlay |
# 
# ### Dependencies
# Python libraries that Kloppy depend on
# 
# Black :
# : Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting.
# Black makes code review faster by producing the smallest diffs possible.
# 
# Lxml :
# : The lxml XML toolkit is a Pythonic binding for the C libraries libxml2 and libxslt. It is unique in that it combines the speed and XML feature completeness of these libraries with the simplicity of a native Python API, mostly compatible but superior to the well-known ElementTree API.
# 
# Requests :
# : Python module that you can use to send all kinds of HTTP requests. It is an easy-to-use library with a lot of features ranging from passing parameters in URLs to sending custom headers and SSL Verification.
# 
# NetworkX :
# : This python package is used for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. It is used to study large complex networks represented in form of graphs with nodes and edges. Using networkx we can load and store complex networks.
# 
# PyTest :
# : PyTest is a testing framework that allows users to write test codes using Python programming language. It helps you to write simple and scalable test cases for databases, APIs, or UI. PyTest is mainly used for writing tests for APIs. It helps to write tests from simple unit tests to complex functional tests.
# 
# Pandas :
# : pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real-world data analysis in Python.
# 
# Pre-commit :
# : A framework for managing and maintaining multi-language pre-commit Git hooks.
