from flask import Flask, render_template, request
import os


app = Flask(__name__)

# Check for environment variable
if not os.getenv("MAPBOX_ACCESS_TOKEN"):
    raise RuntimeError("MAPBOX_ACCESS_TOKEN is not set")


@app.route("/", methods=["POST", "GET"])
def index():
    mapboxAccessToken = os.getenv("MAPBOX_ACCESS_TOKEN")
    geoJsonUrl = ''
    dateFrom = ''
    dateTo = ''
    showmapbox = ''
    if request.method == "POST":
        daterange = request.form['daterange']
        if 'showmapbox' in request.form:
            showmapbox = 'checked'
        dates = daterange.split()
        dateFrom = dates[0]
        dateTo = dates[1]
        geoJsonUrl = f"https://data.calgary.ca/resource/c2es-76ed.geojson?$where=issueddate%20%3E%20%27{dateFrom}%27%20and%20issueddate%20%3C%20%27{dateTo}%27";

    return render_template('index.html', geoJsonUrl=geoJsonUrl, dateFrom=dateFrom, dateTo=dateTo, mapboxAccessToken=mapboxAccessToken,showmapbox=showmapbox)

@app.route("/search")
def search():
    return render_template('search.html')

