import requests
import json

## Get number of contributors
url1 = 'https://api.github.com/repos/cloudinary/cloudinary_npm'
url2 = 'https://github.com/nullivex/nodist'
url3 = 'https://github.com/lodash/lodash'

## If username and token are provided then will authorize, can be adjusted as neccesary
def authorize(username,token):
    if(username != False and token != False):
        return (username,token)
    else:
        return None
    
## Returns the number of events per repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
def events(url,username = False,token = False):
    params = {
        'per_page': 100
    }
    url = url + '/events'
    response = requests.get(url,params = params,auth = authorize(username,token))
    rd = response.json()
    return len(rd)

## Returns the number of people that starred a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
def starred(url,username = False,token = False):
    params = {
        'per_page': 100
    }
    url += '/stargazers'
    response = requests.get(url,params = params,auth = authorize(username,token))
    rd = response.json()
    return len(rd)

## Returns the number of people that are subscribed to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
def subscribers(url,username = False,token = False):
    params = {
        'per_page': 100
    }
    url += '/subscribers'
    response = requests.get(url,params = params,auth = authorize(username,token))
    rd = response.json()
    return len(rd)

## Returns the number of commitsto a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date to check for recency, but did not do that yet because not sure how to handle
def commits(url,username = False,token = False):
    params = {
        'per_page': 100
    }
    url += '/commits'
    response = requests.get(url,params = params,auth = authorize(username,token))
    rd = response.json()
    return len(rd)

## Returns the number of open issues to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date of creation and last update to check for recency, but did not do that yet because not sure how to handle
def open_issues(url,username = False,token = False):
    params = {
        'per_page': 100
    }
    url += '/issues'
    response = requests.get(url,params = params,auth = authorize(username,token))
    rd = response.json()
    return len(rd)

## Returns the number of closed issues to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date of creation, last update, and closure to check for recency, but did not do that yet because not sure how to handle
def closed_issues(url,username = False,token = False):
    params = {
        'per_page': 100,
        'state': 'closed'
    }
    url += '/issues'
    
    response = requests.get(url,params = params,auth = authorize(username,token))
    rd = response.json()
    return len(rd)

## Returns the license, only works for second example git url, needs updating
def license(url,username = False,token = False):
    url += '/license'
    
    response = requests.get(url,auth = authorize(username,token))
    rd = response.json()
    if 'license' in rd:
        return(rd['license']['name'])
    else:
        return None

## Returns a health percentage score based on if there is a readme, contributing, license, and code of conduct
## Can be edited to retrieve any of these
def Community_Metrics(url,username = False,token = False):
    url += '/community/profile'
    
    response = requests.get(url,auth = authorize(username,token))
    rd = response.json()
    return rd['health_percentage']

## Returns the number of closed issues to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date of creation, last update, to check for recency, but did not do that yet because not sure how to handle
def pull_requests(url,username = False,token = False):
    params = {
        'per_page': 100,
    }
    url += '/pulls'
    
    response = requests.get(url,params = params,auth = authorize(username,token))
    rd = response.json()
    return len(rd)






