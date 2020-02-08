import json
import csv

# Load files
in_file = open("MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.txt", 'r')
new_file = open("Initial_Nov_fires.json", 'w')
out_file = open("readable_Nov_fires.json",'w')

# Create readable json file from txt file
fieldnames = 'latitude','longitude','brightness','scan','track','acq_date','acq_time','satellite','confidence','version','bright_t31','frp','daynight'
reader = csv.DictReader(in_file, fieldnames)
for row in reader:
    json.dump(row, new_file)
    new_file.write('\n')

fire_data = json.load(new_file)


json.dump(fire_data, out_file, indent = 4)


#extract longitudes, latitudes, and brightness
lons, lats, brights = [],[],[]

for row in out_file:
    lon = row['longitude']
    lat = row['latitude']
    bright = row['brightness']
    lons.append(lon)
    lats.append(lat)
    brights.append(bright)

print(lons[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon = lons, lat = lats)]


# make points colored based on brightness

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    },
}]

my_layout = Layout(title = "Australian Fires - November 2019")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename = 'Australian_Fires_November_2019.html')

