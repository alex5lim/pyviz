import requests
import pygal
from pygal.style import LightColorizedStyle, LightenStyle

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# Store API response
response_dict = r.json()

# Print total count
print("Total count: ", response_dict['total_count'])

# Process items in response
repos_dict = response_dict['items']
print("Repositories returned: ", len(repos_dict), "\n")
names, plots = [], []
for item in repos_dict:
    names.append(item['name'])
    if item['description']:
        description = item['description']
    else:
        description = "No description provided."
    plots.append({
                  'value': item['stargazers_count'],
                  'label': description,
                  'xlink': item['html_url'],
                  })

# Make visualization
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
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names
chart.add("", plots)
chart.render_to_file('python_repos.svg')
print("Chart saved as python_repos.svg")
