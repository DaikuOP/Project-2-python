from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        comentarios = response_dict['descendants']
    except KeyError:
        print(f'El articulo de HN no tiene comentarios')
        continue
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': comentarios,
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, links, coments = [], [], []
for element in range(len(submission_dicts)):
    title = f"<a href='{submission_dicts[element]['hn_link']}'>{submission_dicts[element]['title']}</a>"
    coment = submission_dicts[element]['comments']
    titles.append(title)
    coments.append(coment)    

data = [{
    'type':'bar',
    'x': titles,
    'y': coments,
    'marker' : {
        'color' : 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': f"Los articulos de Hacker News con mas comentarios hoy",
    'titlefont': {'size' : 28},
    'xaxis': {
        'title' : 'Titulos',
        'titlefont': {'size' : 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title' : 'Comentarios',
        'titlefont': {'size' : 24},
        'tickfont': {'size': 14},        
        } 
}

fig = {'data' : data, 'layout': my_layout}
offline.plot(fig, filename= f'Hacker_News_comments.html')

