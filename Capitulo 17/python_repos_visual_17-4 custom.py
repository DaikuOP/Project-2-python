import requests
from plotly.graph_objs import Bar
from plotly import offline


url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()


repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []

repo_dict = repo_dicts[0]

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)
    stars.append(repo_dict['stargazers_count'])

data = [{
    'type':'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker' : {
        'color' : 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': "Los proyectos de python con más estrellas en GitHub personalizado",
    'titlefont': {'size' : 28},
    'xaxis': {
        'title' : 'Repository',
        'titlefont': {'size' : 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title' : 'Stars',
        'titlefont': {'size' : 24},
        'tickfont': {'size': 14},        
        },
    'template':'plotly_dark'
}

fig = {'data' : data, 'layout': my_layout}
offline.plot(fig, filename='17-4_python_repos.html')