#!/usr/bin/env python
# coding: utf-8

# # Project Context
# 
# The use of data in sport, particularly in football, plays an important role in the development of players' skills or in the analysis of the game. Nowadays, we can talk about football in a more detailed way than before.
# This analysis could help clubs, managers or even individuals to identify and uncover new facts about football, this leads to an innovative and winning startegy.
# 
# The knowledge gained in my university years helped me achieve this project. The Business intelligence (BI) combines data analytics, data visualization, data mining, data tools and infrastructure. This project includes the first two terms, data analytics and data visualization on football.
# 
# 
# ## Real analytics
# ### Definition 
# Real Analytics is leading AI company of professors in mathematics, Statistics, Computer Science and economics. It has built a word-leading research in sports analytics.
# In 2018 Real Analytics was formed with the objective of using the re-search expertise in the football industry to mitigate the risk and uncertainty associated with player recruitment and team selection.
# ### Achivements
# * In january 2017, Real Analytics predicted Chelsea to win by seven points and Arsenal to finish outside the top 4.
# * During the extraordinary 2016-17 Premier League season, they identified earlier than anyone that Leicester City were favourites for the league title. Their player ratings models predicted that Leicester City had a team capable of continuing their incredible start to the season.
# * In April 2020 Real Analytics took a closer look at the impact of the potential sale of Pierre-Emerick Aubameyang for Arsenal FC. Their AI powered prediction models simulate the season more than 100k iteration under two scenarios: Arsenal keep Aubameyang, and Arsenal sell Aubamyang to Barcelona (Squad after). The results show that although there is no impact on Arsenal's chances of winning the league which stays at zero. 
# 
# ## Methodology
# Real Analytics chooses to treat scrum methodology as its core project management framework for the team to generate innovative and adaptive solutions for real-world problems.
# Adapting the Srcum framework to a company which has a small team with a heavy workload Scrum methodology will be the most appropriate choice.
# ### What is SCRUM methodology ?
# Scrum is an Agile project management methodology involving a small team led by a Scrum master, whose main job is to remove all obstacles to getting work done. Work is done in short cycles called sprints, and the team meets daily to discuss current tasks and any roadblocks that need clearing.
# ```{figure} img/blog-scrum-process.jpg
# ---
# name: scrum-fig
# ---
# SCRUM framework. 
# ```
# There are fundamentally 3 Scrum roles:
# * **Product Owner** : The PO is a vital link between the development team and the product stakeholders, including the customer.
# * **Scrum Master**: It is the role of the Scrum master to keep on top of the project’s status and ensure that the development team follows the Scrum process. 
# * **Scrum Development Team**: The team is made up of 5-9 developers, programmers, designers and testers who collaborate. They do not have designated roles, but are given a specific set of tasks to complete in a given sprint. 
# 
# Each sprint is subdivided into 5 phases :
# 
# * **Sprint planning**: During the sprint planning session, the Srum Master meets with the development team to plan details of the upcoming sprint. The team collectively decides which high-priority items in the product backlog can reasonably be completed during the sprint, given their available time and resources. Tasks are then assigned to individual team members.
# 
# * **Daily Scrum**: This brief daily is meeting limited to 15 minutes or less. The purpose of the daily Scrum is to check in with other team members, assess the day’s progress, discuss any issues and plan the next day’s work. 
# 
# * **Sprint review**: The sprint review is a tune-up session that typically takes place on the last day of a sprint. It looks at what went well, what went wrong and what can be done better. 
# 
# * **Sprint retrospective**: The retrospective is the final meeting at the end of a sprint, attended by the Product Owner, Scrum Master and development team. During the meeting, participants discuss what improvements can be made, and how to implement them in future sprints. 
# 
# * **Sprint**: The sprint itself is considered an element of the development process. It encompasses all the work and events that occurred during its limited time increment. 
# 
# ### Project
# This project consists of 3 sprints, each sprint is a chapter.
# * Sprint 1 : the kloppy package.
# * Sprint 2 : Physical report.
# * Sprint 3 : Visualization.
# 
# ### Tools
# The company uses the following tools.
# * **Jira Board**: Jira Board displays problems from one or more projects, giving a flexible way to see, manage and report on work in progress.
# ```{figure} img/jira.png
# ---
# name: jira-fig
# ---
# Jira Board . 
# ```
# * **Slack**: Slack is a messaging app for business. It facilitates communication in the workplace. Helps teams communicate, collaborate across remote distances. Enables and encourages the sharing of documents, images and other assets across teams.
# * **Google Meet**: Google meet serves for the daily virtual meetings.
# 
# ## Project objectives
# The aim of this project is to build a tool to visualize tracking and event data of football games.
# The project consists of two main parts that will be divided into three independent chapters.
# * **Processing Data** : Transform the raw data of the **Event data** from the data provider into a more user-friendly format and provide a standardized data model and Extract the player's physical summary report from the **Tracking data**.
# * **Visualization** : Build a package to visualize the tracking data processed for a given football game (game score, players performance, player comparison).
# 
# ## Data
# The data on which we will work on is created by remote sensing devices worn by prospective players and data  gathered during actual gameplay, and supplied by dedicated data providers.
# The data we will be working on are tracking and event data that we intend to identify in the next chapters.
