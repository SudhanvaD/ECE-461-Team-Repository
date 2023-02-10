import requests
import json
import os

## Get number of contributors

url1 = 'https://api.github.com/repos/cloudinary/cloudinary_npm'
url2 = 'https://github.com/nullivex/nodist'
url3 = 'https://github.com/lodash/lodash'

file = open(r'Sample Url File.txt',"r")
input = file.readlines()
file.close()
input[len(input)-1] = input[len(input)-1] + '\n'
input = [i[:-1] for i in input]
git_inputs = [i for i in input if i[8:11] == 'git']
npm_inputs = [i for i in input if i[8:11] == 'npm']
error_inputs = [i for i in input if ((i[8:11] == 'npm') and (i[8:11] == 'git'))]
os.environ['GITHUB_TOKEN'] = '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'
token = os.getenv('GITHUB_TOKEN')

def format_url(url):
    url = url.split('://')
    url = url[0] + '://api.' + url[1]
    url = url.split('.com/')
    url = url[0] + '.com/repos/' + url[1]
    return url

## If username and token are provided then will authorize, can be adjusted as neccesary
def authorize(token):
    if(token != False):
        return {'Authorization': 'token ' + token}
    else:
        return None
    
## Returns the number of events per repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
def events(url,token = False):
    params = {
        'per_page': 100
    }
    url = url + '/events'
    response = requests.get(url,params = params,headers = authorize(token))
    rd = response.json()
    return len(rd)

## Returns the number of people that starred a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
def starred(url,token = False):
    params = {
        'per_page': 100
    }
    url += '/stargazers'
    response = requests.get(url,params = params,headers = authorize(token))
    rd = response.json()
    return len(rd)

## Returns the number of people that are subscribed to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
def subscribers(url,token = False):
    params = {
        'per_page': 100
    }
    url += '/subscribers'
    response = requests.get(url,params = params,headers = authorize(token))
    rd = response.json()
    return len(rd)

## Returns the number of commitsto a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date to check for recency, but did not do that yet because not sure how to handle
def commits(url,token = False):
    params = {
        'per_page': 100
    }
    url += '/commits'
    response = requests.get(url,params = params,headers = authorize(token))
    rd = response.json()
    return len(rd)

## Returns the number of open issues to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date of creation and last update to check for recency, but did not do that yet because not sure how to handle
def open_issues(url,token = False):
    params = {
        'per_page': 100
    }
    url += '/issues'
    response = requests.get(url,params = params,headers = authorize(token))
    rd = response.json()
    return len(rd)

## Returns the number of closed issues to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date of creation, last update, and closure to check for recency, but did not do that yet because not sure how to handle
def closed_issues(url,token = False):
    params = {
        'per_page': 100,
        'state': 'closed'
    }
    url += '/issues'
    
    response = requests.get(url,params = params,headers = authorize(token))
    rd = response.json()
    return len(rd)

## Returns the license, only works for second example git url, needs updating
def license(url,token = False):
    url += '/license'
    
    response = requests.get(url,headers = authorize(token))
    rd = response.json()
    if 'license' in rd:
        return(rd['license']['name'])
    else:
        return 'None'

## Returns a health percentage score based on if there is a readme, contributing, license, and code of conduct
## Can be edited to retrieve any of these
def Community_Metrics(url,token = False):
    url += '/community/profile'
    
    response = requests.get(url,headers = authorize(token))
    rd = response.json()
    return rd['health_percentage']

## Returns the number of closed issues to a repo, can do up to 100
## Can do more than 100, but will need multiple calls and there are call limits
## ***** Can also get date of creation, last update, to check for recency, but did not do that yet because not sure how to handle
def pull_requests(url,token = False):
    params = {
        'per_page': 100,
    }
    url += '/pulls'
    
    response = requests.get(url,params = params,headers = authorize(token))
    rd = response.json()
    return len(rd)

def write(input):
    out = open(r'out.txt','w')
    for url in input:
        url = format_url(url)
        print(url)
        out.write(url + '\n')
        out.write('Number of Events: ' + str(events(url,token)) + '\n')
        out.write('Number of Starred: ' + str(starred(url,token)) + '\n')
        out.write('Number of Subscribers: ' + str(subscribers(url,token)) + '\n')
        out.write('Number of Commits: ' + str(commits(url,token)) + '\n')
        out.write('Number of Open_Issues: ' + str(open_issues(url,token)) + '\n')
        out.write('Number of Closed_Issues: ' + str(closed_issues(url,token)) + '\n')
        out.write('License: ' + license(url,token) + '\n')
        out.write('Community Metric: ' + str(Community_Metrics(url,token)) + '\n')
        out.write('Pull_Requests: ' + str(pull_requests(url,token)) + '\n')
        out.write('\n')
    out.close()


write(git_inputs)
# urlx = format_url(url2)
# print(events(urlx,'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'))




