---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region -->
# Visualization

In this chapter , we will present the data analyzed for visualization purposes.


## Tools

To build our dashboard we will use :
* Dash for the dashboard
* Plotly for chart presentation

## Dashboard Content

A player metrcis dashboard that dipsplay the types of running performance of the player in a game.


|Variable|Description|
|--------|-----------|
|Total Minutes|Total minutes in MM:SS format that a player played in the game.|
|Distance|Total distance player travelled in meters|
|No. of High Intensity Runs|The number of high speed runs and sprints that the player performs in a game.|
|No. of High Speed Runs|The number of high speed runs that the player performs in a game.|
|No. of Sprints|The number of sprints that the player performs in a game.|
|Standing|Total distance player travelled in meters while standing.By default , Player is deﬁned as standing if they are moving <= 0.2 m/s.|
|Walking| Total distance player travelled in meters while walking. By default, Player is deﬁned as walking if they are moving >0.2 m/s and <= 2.0 m/s.|
|Jogging| Total distance player travelled in meters while jogging. By default, Player is deﬁned as jogging if they are moving >2.0 m/s and <= 4.0 m/s.|
|Running| Total distance player travelled in meters while running. By default, Player is deﬁned as running if they are moving >4.0 m/s and <= 5.5 m/s.|
|High Speed Running| Total distance player travelled in meters while high speed running. By default,Player is deﬁned as high speed running if they are moving >5.5 m/s and <= 7.0 m/s.|
|Sprint| Total distance player travelled in meters while sprinting. By default, Player is deﬁned as sprinting if they are moving >7.0 m/s.|
<!-- #endregion -->
