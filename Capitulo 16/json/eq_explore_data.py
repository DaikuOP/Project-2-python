import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'Project/chapter 16/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'Project/chapter 16/data/readable_eq_data.json'

with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent = 4)

all_eq_dicts = all_eq_data['features']

# 16-6 Quite el uso de variables temporales y asigne directamente el valor a la lista 
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
        mags.append(eq_dict['properties']['mag'])
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text' : hover_texts,
    'marker': {
        'size':[5*mag for mag in mags],
        'color' : mags,
        'colorscale': 'Reds',
        'reversescale': False,
        'colorbar' : {'title' : 'Magnitud'}
    }
}]

#16-7 Se saca el titulo automaticamente del archivo JSON 
my_layout = Layout(title= all_eq_data['metadata']['title'])

fig = {'data': data, 'layout':my_layout}

offline.plot(fig, filename = 'terremotos_globales.html')

