import requests
import json

"""https://github.com/cloudinary/cloudinary_npm
https://www.npmjs.com/package/express
https://github.com/nullivex/nodist
https://github.com/lodash/lodash
https://www.npmjs.com/package/browserify"""

# Get number of contributors
url = 'https://api.github.com/repos/namruthahari/Sample-Git-Repo/contributors'
response = requests.get(url)
rd = response.json()
num_contributors = len(rd)

url = 'https://github.com/nullivex/nodist'
response = requests.get(url)
rd = response.json()
print(rd)
print(rd[0]['url'])

"""
print(rd[0]['issue_events_url'])
print(rd[0]['issue_comment_url'])
print(rd[0]['issues_url'])
print(rd[0]['has_issues'])
print(rd[0]['open_issues_count'])
print(rd[0]['open_issues'])
"""
