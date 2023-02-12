import requests
from decouple import config
import urlParser
import re
from urllib.parse import urlparse


token = config('API_KEY')

headers = {"Authorization": 'Bearer ' + token}

def generateQuery(url):

    parseResults = urlparse(url)
    path = parseResults.path
    repoDetails = path.split('/')
    owner = '"' + repoDetails[1] + '"'
    name = '"' + repoDetails[2] + '"'


    graphQlQuery = """
    query {
      repositoryOwner (login: """+owner+""") {
        repository(name: """+name+""") {
          forks {
            totalCount
          }
          issues {
            totalCount
          }
          stargazers {
            totalCount
          }
          watchers {
            totalCount
          }
          pullRequests {
            totalCount
          }
        }
      }
    }"""
    #print(graphQlQuery)
    return graphQlQuery

def run_graphQlQuery(graphQlQuery):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': graphQlQuery}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, graphQlQuery))

def generateGraphQLData(validUrls):
    graphQlData = []
    for url in validUrls:
        query = generateQuery(url)
        result = run_graphQlQuery(query)
        graphQlData.append(result['data']['repositoryOwner']['repository'])
    for i in graphQlData: print("Info - {}".format(i))
    with open("outputGraphQl.txt", "w") as f:
        for i in graphQlData: print("Info - {}\n".format(i), file=f)
