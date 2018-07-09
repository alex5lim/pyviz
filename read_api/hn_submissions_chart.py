import requests
from operator import itemgetter
import pygal
from pygal.style import LightenStyle, LightColorizedStyle

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
if r.status_code == 200:
    print("Processing")
else:
    print("Can't connect to {0:s}. Error {1:d}".format(url, r.status_code))
    exit(1)

# Process information about each submission
submission_ids = r.json()
submission_dicts = []

for id in submission_ids[:30]:
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(id) + ".json"
    r = requests.get(url)
    if r.status_code != 200:
        print("Can't connect to {0:s}. Error {1:d}".format(url, r.status_code))
    submission_item = r.json()
    submission_dict = {
       'title': submission_item['title'],
       'link': submission_item['url'],
       'comments': submission_item.get('descendants', 0)
       }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

chart_x_labels = []
chart_plots = []
for item in submission_dicts:
    chart_x_labels.append(item['title'])
    chart_plots.append({
                        'value': item['comments'],
                        'label': item['title'],
                        'xlink': item['link'],
                        })

# Make the chart
chart_style = LightenStyle('#333366', base_style=LightColorizedStyle)
chart_style.title_font_size = 18
chart_style.label_font_size = 12
chart_style.major_label_font_size = 14

chart_config = pygal.Config()
chart_config.x_label_rotation = 45
chart_config.show_legend = False
chart_config.truncate_label = 15
chart_config.show_y_guides = False
chart_config.width = 1000

chart = pygal.Bar(chart_config, style=chart_style)
chart.title = "Hacker News Top Stories"
chart.x_labels = chart_x_labels
chart.add("", chart_plots)
chart.render_to_file("hn_submissions_chart.svg")
print("saved chart to hn_submissions_chart.svg")
