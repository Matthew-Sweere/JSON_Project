import csv

# Load files
with open('MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2020026.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None) #skip the headers

    #extract longitudes, latitudes, and brightness
    lats, lons, brights = [],[],[]

    for row in csv.reader(csv_file):
        lat = row[0]
        lon = row[1]
        bright = float(row[2])
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

print(brights[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon = lons, lat = lats)]


# make points colored based on brightness

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{
        'size': 10,
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    },
}]

my_layout = Layout(title = "Australian Fires - January 2020")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename = 'Australian_Fires_January_2020.html')

