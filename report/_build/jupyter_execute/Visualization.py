#!/usr/bin/env python
# coding: utf-8

# # Visualization
# 
# ## Introduction
# In this chapter , we will present the data analyzed for visualization purposes.
# 
# 
# ## Tools
# As we mentioned earlier, this internship is done only using python programming language. We will use Dash-plotly as a framework.
# 
# ### What is Dash ?
# 
# Dash is a python framework created by plotly for creating interactive web applications. Dash is written on the top of Flask, Plotly.js and React.js.Dash is open source and the application build using this framework are viewed on the web browser.
# 
# The Dash application is made of two building blocks
# 
# **Layout :** It defines the structure of the application . Elements used such as dropdowns , buttons , graphs etc and the placement , size , color etc. Dash contains Dash HTML components which we can create and style HTML content such as heading, paragraph, images etc using python . Elements such as dropdowns, graphs, cards are created using Dash Core components.
# Dash also includes Dash Bootstrap components that makes it easier to build consistently styled apps with complex, responsive layouts.
# 
# **Callbacks :** Are used to bring interactivity to the dash application. These are the functions using which, for example, we can define the activity that would happen on clicking a button or a dropdown.
# 
# 
# ## Dashboard Content
# ### Match page
# ### Player page
# ### Player Comparison
# 
# A player metrcis dashboard that dipsplay the types of running performance of the player in a game.
# 
# 
# |Variable|Description|
# |--------|-----------|
# |Total Minutes|Total minutes in MM:SS format that a player played in the game.|
# |Distance|Total distance player travelled in meters|
# |No. of High Intensity Runs|The number of high speed runs and sprints that the player performs in a game.|
# |No. of High Speed Runs|The number of high speed runs that the player performs in a game.|
# |No. of Sprints|The number of sprints that the player performs in a game.|
# |Standing|Total distance player travelled in meters while standing.|
# |Walking| Total distance player travelled in meters while walking. |
# |Jogging| Total distance player travelled in meters while jogging. |
# |Running| Total distance player travelled in meters while running. |
# |High Speed Running| Total distance player travelled in meters while high speed running.|
# |Sprint| Total distance player travelled in meters while sprinting.|
