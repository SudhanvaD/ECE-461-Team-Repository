import requests
import json

## Get number of contributors
url = 'https://api.github.com/repos/namruthahari/Sample-Git-Repo/contributors'
response = requests.get(url)
rd = response.json()
num_contributors = len(rd)

url = 'https://api.github.com/repos/namruthahari/Sample-Git-Repo/issues'
response = requests.get(url)
rd = response.json()

print(rd['issue_events_url'])
print(rd['issue_comment_url'])
print(rd['issues_url'])
print(rd['has_issues'])
print(rd['open_issues_count'])
print(rd['open_issues'])


