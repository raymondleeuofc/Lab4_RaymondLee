# ENGO551/651 - Lab 4 Assignment
The objective of this lab was to gain experience with Mapbox Vector Tiles and Mapbox Studio, design a visually appealing map layer, and integrate a vector tileset to an existing GeoWeb application (Lab 3).

## Important Folders and Files
- static : contains the style sheets
    - styles.css : CSS style sheet file
- templates : contains the html files used on the website
    - base.html : the base webpage format that all other html files inherit
    - index.html : the main webpage file
- application.py : the Python script containing all the functionality for getting building permit information, and Mapbox Style layer. 
- run.bat : a batch file used to run the application.py script

## Requirements Met
1. All requirements from Lab 3 are met. 
2. When the user visits the site, the 2017 Traffic Incident layer can be toggled on and off. 
3. The map layer was designed to be visually appealing, this was done by adjusting factors such as Radius, Color, Blur, and Opacity.
    - Radius : as the user zooms in, the size of the points increase.
    - Color : as the user zooms in, the color changes from a dark purple to a bright magenta. 
    - Blur : as the user zooms in, the blurring of the points decreases (becomes more sharp).
    - Opacity : as the user zooms in, the points become less opaque. 


## Additional Details about the Lab Assignment 
To run the building permit website please follow the steps below: 
1. Set up your environment with all the necessary dependencies.
2. Run the run.bat file in a command terminal (this runs the application.py file). 
3. Explore the website! :D
