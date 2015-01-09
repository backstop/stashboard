import json
import urllib2

def load_stats():
    with open('data/stats.json') as fp:
    	return json.load(fp)

stats = load_stats()
