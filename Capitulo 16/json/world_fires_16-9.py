import csv
import math
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'Project/chapter 16/data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    lat, long, bright, date = header_row.index("latitude"), header_row.index("longitude"), header_row.index("brightness"), header_row.index('acq_date')
    longitudes, latitudes, brightness, hover_text = [], [], [], []

    for row in reader:
        try:
            longs = row[long]
            lats = row[lat]
            brights = row[bright]
        except ValueError:
            continue
        longitudes.append(longs)
        latitudes.append(lats)
        brightness.append(brights)
        hover_text.append(row[date])

data = [{
    'type' : 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text' : hover_text,
    'marker' :{
        'size':[0.03*float(bri)//1 for bri in brightness],
        'color' : [float(bri)//1 for bri in brightness],
        'colorscale': 'RdBu',
        'reversescale': True,
        'colorbar' : {'title' : 'Magnitud'}
    }
}]

my_layout = Layout(title='Fuegos en el mundo clasificados por brillo')

fig = {'data' :data, 'layout':my_layout}
offline.plot(fig, filename ='fuegos.html')

