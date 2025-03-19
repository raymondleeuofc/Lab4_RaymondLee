# ENGO551/651 - Lab 3 Assignment
The objective of this lab was to gain experience with Leaflet.js and GeoJSON as well as learning to build a geoweb app through combining two APIs. 

## Important Folders and Files
- static : contains the style sheets
    - styles.css : CSS style sheet file
- templates : contains the html files used on the website
    - base.html : the base webpage format that all other html files inherit
    - index.html : the main webpage file
- application.py : the Python script containing all the functionality for getting building permit information. 
- run.bat : a batch file used to run the application.py script

## Requirements Met
1. When users visit the building permit website, they are shown a map of Calgary.
2. Users can search for building permits in a range of dates using the date selector widget. 
3. Users can click on each marker (representing a building permit) to which they are shown all relevant information for that permit. 
4. In the case of overlapping markers, the OverlappingMarkerSpiderfier Leafltet Plug-in is used to expand these markers to clearly show the user permit information. 
5. When zoomed out to certain levels, markers can become very close and look unappealing, to remedy this issue these markers are clustered together. The individual markers can be shown by clicking on a cluster which causes the map to zoom out. 
6. The map is refreshed when the user searches for a new date range. 


## Additional Details about the Lab Assignment 
To run the building permit website please follow the steps below: 
1. Set up your environment with all the necessary dependencies.
2. Run the run.bat file in a command terminal (this runs the application.py file). 
3. Explore the website! :D
