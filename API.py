import requests
import json
import os
from decouple import config

## Get number of contributors

def format_url(url):
    url = url.split('://')
    url = url[0] + '://api.' + url[1]
    url = url.split('.com/')
    url = url[0] + '.com/repos/' + url[1]
    return url




## Returns the number of events per repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
def events(url, token=False):
    params = {
        'per_page': 100
    }
    url = url + '/events'
    response = requests.get(url, params=params, headers=authorize(token))
    rd = response.json()
    return len(rd)


## Returns the number of people that starred a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
def starred(url, token=False):
    params = {
        'per_page': 100
    }
    url += '/stargazers'
    response = requests.get(url, params=params, headers=authorize(token))
    rd = response.json()
    return len(rd)


## Returns the number of people that are subscribed to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
def subscribers(url, token=False):
    params = {
        'per_page': 100
    }
    url += '/subscribers'
    response = requests.get(url, params=params, headers=authorize(token))
    rd = response.json()
    return len(rd)


## Returns the number of commitsto a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date to check for recency, but did not do that yet because not sure how to handle
def commits(url, token=False):
    params = {
        'per_page': 100
    }
    url += '/commits'
    response = requests.get(url, params=params, headers=authorize(token))
    rd = response.json()
    return len(rd)


## Returns the number of open issues to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date of creation and last update to check for recency, but did not do that yet because not sure how to handle
def open_issues(url, token=False):
    params = {
        'per_page': 100
    }
    url += '/issues'
    response = requests.get(url, params=params, headers=authorize(token))
    rd = response.json()
    return len(rd)


## Returns the number of closed issues to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date of creation, last update, and closure to check for recency, but did not do that yet because not sure how to handle
def closed_issues(url, token=False):
    params = {
        'per_page': 100,
        'state': 'closed'
    }
    url += '/issues'

    response = requests.get(url, params=params, headers=authorize(token))
    rd = response.json()
    return len(rd)


## Returns the license, only works for second example git url, needs updating
def license(url, token=False):
    url += '/license'

    response = requests.get(url, headers=authorize(token))
    rd = response.json()
    if 'license' in rd:
        return (rd['license']['name'])
    else:
        return 'None'


## Returns a health percentage score based on if there is a readme, contributing, license, and code of conduct
## Can be edited to retrieve any of these
def Community_Metrics(url, token=False):
    url += '/community/profile'

    response = requests.get(url, headers=authorize(token))
    rd = response.json()
    return rd['health_percentage']


## Returns the number of closed issues to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date of creation, last update, to check for recency, but did not do that yet because not sure how to handle
def pull_requests(url, token=False):
    params = {
        'per_page': 100,
    }
    url += '/pulls'

    response = requests.get(url, params=params, headers=authorize(token))
    rd = response.json()
    return len(rd)


def write(input, token):
    out = open(r'out.txt', 'w')
    for url in input:
        url = format_url(url)
        out.write(url + '\n')
