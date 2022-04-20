#!/usr/bin/env python
# coding: utf-8

# # Data Visualization
# 
# ## Introduction
# In this chapter, we will visualize the data we were working on, so that we can present them with the best layout and the best way.
# 
# ## FrameWork
# Away from the basic softwares used for data visualisation, We will stick to Python and create the dashboard from scratch using dash-plotly as a framework. We're going to build an analytical web application. 
# 
# ### What is Dash ?
# 
# Dash is a python framework created by plotly for creating interactive web applications. Dash is written on the top of Flask, Plotly.js and React.js.Dash is open source and the application build using this framework are viewed on the web browser.
# 
# The Dash application is made of two building blocks
# 
# Layout :
# : It defines the structure of the application . Elements used such as dropdowns , buttons , graphs etc and the placement , size , color etc. Dash contains Dash HTML components which we can create and style HTML content such as heading, paragraph, images etc using python . Elements such as dropdowns, graphs, cards are created using Dash Core components.
# Dash also includes Dash Bootstrap components that makes it easier to build consistently styled apps with complex, responsive layouts.
# 
# Callbacks :
# : Are used to bring interactivity to the dash application. These are the functions using which, for example, we can define the activity that would happen on clicking a button or a dropdown.
# 
# ### Dash Bootstrap Components
# For improved layout design, we will use Bootstrap. Dash-bootstrap-components is a library of Bootstrap components for Plotly Dash, that makes it easier to build consistently styled apps with complex, responsive layouts.
# ## Dashboard Content
# 
# ### Match page
# 
# The landing page which contains game information such as home team and away team, name and score also two buttons to pass to display the line-up for each team and comparison of players.
# ```{figure} img/landingpage.png
# ---
# name: landingpage-fig
# ---
# The landing page.
# ```
# ```{figure} img/lineuppage.png
# ---
# name: lineuppage-fig
# ---
# Displayed content after clicking on line-up button.
# ```
# ### Running configuration
# It where the user can configurate each type of running.
# ```{figure} img/config.png
# ---
# name: config-fig
# ---
# Configuration of the runiing types.
# ```

# ### Player page
# It is the main page on which the player performance information will be displayed.
# ```{figure} img/playerpage.png
# ---
# name: playerpage-fig
# ---
# Displayed content after selecting on one player .
# ```

# ### Player Comparison
# ```{figure} img/playercomp.png
# ---
# name: playercomp-fig
# ---
# Displayed content after selecting on two player.
# ```
