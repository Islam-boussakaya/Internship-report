#!/usr/bin/env python
# coding: utf-8

# # Physical  report
# 
# ## Introduction
# The evaluation of the players performance is mandatory step in the football analysis. It allows to analyze each profile, compare profiles.
# The player's physical report includes player performance, such as the total distance covered, the total number of minutes played, the number of sprints, the maximum speed, etc. 
# In this chapter, we will work on the tracking data and how we will generate the player's physical report from it.
# Besides that we want to allow the user to configure the prameters of each type of running.
# 
# ## Tracking Data
# The tracking data gives a detailed overview of each player's position and movement on the pitch at all times. It provides a vital context for everything that goes on on the pitch, on and off the ball.
# ```{figure} img/trackingdata.png
# ---
# name: tracking-fig
# ---
# This is a sample of tracking data. 
# ```
# Each frame in the above figure includes the period (1 if the first half and 2 if the second half),The side team of he player (home or away team), The position (value of X and Y of the pitch) for each player, a boolean variable whether the player is visualised or not and the recorded speed.
# ## Workflow
# The player's physical report includes these following variables :
# 
# * **Total Minutes**: Total minutes in MM:SS format that a player played in the game.
# * **Distance**: Total distance player travelled in meters.
# * **Standing**: Total distance player travelled in meters while standing. Player is deﬁned as standing if they are moving <= 0.2 m/s.
# * **Walking**: Total distance player travelled in meters while walking. Player is deﬁned as walking if they are moving >0.2 m/s and <= 2.0 m/s.
# * **Jogging**: Total distance player travelled in meters while jogging. Player is deﬁned as jogging if they are moving >2.0 m/s and <= 4.0 m/s.
# * **Running**: Total distance player travelled in meters while running. Player is deﬁned as running if they are moving >4.0 m/s and <= 5.5 m/s.
# * **High Speed Running**: Total distance player travelled in meters while high speed running.Player is deﬁned as high speed running if they are moving >5.5 m/s and <= 7.0 m/s.
# * Sprint: Total distance player travelled in meters while sprinting. Player is deﬁned as sprinting if they are moving >7.0 m/s.
# * **Top Speed**: The peak velocity that the player reached in the entire game. Top speed is reported in km/h.
# * **No. of High Intensity Runs**: The number of high speed runs and sprints that the player performs in a game.
# 
# ### Minutes played
# To compute the total minutes played we have to :
# - Identify the first and the last frame that the player appears on.
# - Calculate the difference in seconds. If the last observation is in the second half, and the first in the first half, the total length of the first half should be considered.
# ```{figure} img/minutes.png
# ---
# name: minutes-fig
# ---
# Exemple of the first and last frame of away player 4. 
# ```
# 
# ```{figure} img/codeminutes.png
# ---
# name: codeminutes-fig
# ---
# Code exemple. 
# ```
# ### Distance covered 
# for each run type we will compute the distance covered, we must go through these steps:
# * compute the sampling freqency, it is the median time in seconds between frames.
# * define the running window. In our case, it is the number of consecutive frames in one minute period.
# 
# ```{figure} img/rw.png
# ---
# name: rw-fig
# ---
# the number of running window of the left provider is 25 and for the right provider is 10. 
# ```
# * For each frame of the corresponding player we verify the condition of each run type and multiply this by the sampling frequency. Finally, we sum up these frames.
# 
# And to compute the number of high speed running, we have to verify it's condition (>5.5 m/s and <= 7.0 m/s) and find the number of occassions it was sustained for at least one running window length.
# 
# ### Top speed
# 
# To determine the top speed of the player, we look for the maximum speed recorded.
# 
# ### Exemple
# ```{figure} img/runexp.png
# ---
# name: runexp-fig
# ---
# Exemple of the away player 4. 
# ```
# 
# ## Result
# ```{figure} img/result.png
# ---
# name: result-fig
# ---
# The physical report. 
# ```

# In[ ]:




