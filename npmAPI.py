import requests

def findGitUrl(url):
    print('Function code 1',url)
    splits = url.split('/')
    packageName = splits[-1]
    url = 'https://registry.npmjs.org/' + packageName
    print('Function code 2', url)
    print(url)
    response = requests.get(url)
    print('Function code 3', response)
    rd = response.json()
    gitUrl = rd['repository']['url']
    gitUrl = gitUrl[4:]
    gitUrl = gitUrl.replace('.git','')
    print('Succes. Git URL is', gitUrl)
    return gitUrl

findGitUrl('https://www.npmjs.com/package/express')