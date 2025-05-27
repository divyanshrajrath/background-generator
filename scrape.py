import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news") # to recieve all the data from the hacker news website
soup = BeautifulSoup(res.text, "html.parser") #to view it response as a html code
links = soup.select(".titleline") #to grab all the links
subtext= soup.select(".subtext")# to grab all the scores of news

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k["votes"], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for inx, item in enumerate(links):
        title=links[inx].getText()
        href=links[inx].get("href", None)
        vote=subtext[inx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points",""))
            if points>=100:
                hn.append({"title":title, "link": href, "votes":points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))