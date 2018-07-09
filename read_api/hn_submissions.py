import requests
from operator import itemgetter

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
if r.status_code == 200:
    print("Processing")
else:
    print("Error", r.status_code)
    exit(1)

# Process information about each submission
submission_ids = r.json()
submission_dicts = []

for id in submission_ids[:30]:
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(id) + ".json"
    r = requests.get(url)
    if r.status_code != 200:
        print("Error: ", r.status_code)
    submission_item = r.json()
    submission_dict = {
       'title': submission_item['title'],
       'link': submission_item['url'],
       'comments': submission_item.get('descendants', 0)
       }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for item in submission_dicts:
    print("\nTitle:", item['title'])
    print("Discussion link:", item['link'])
    print("Coments: ", item['comments'])
