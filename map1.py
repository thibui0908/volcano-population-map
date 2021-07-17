import folium
import pandas 

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if (elevation < 2000):
        return 'green'
    elif 2000 <= elevation < 4000:
        return 'orange'
    else: 
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6,popup= "Mountain " + name + ": " + str(el) + " meters", fill_color=color_producer(el), color='grey', fill_opacity=0.7, fill=True ))

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))

map.add_child(fg)

map.save("Map1.html")
