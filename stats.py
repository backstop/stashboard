import json
import urllib2

def load_stats():
    file = urllib2.urlopen("https://raw.githubusercontent.com/backstop/stashboard/master/data/stats.json")
    return json.load(file)

stats = load_stats()
