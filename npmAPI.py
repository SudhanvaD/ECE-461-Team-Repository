import requests
import validators

urlFilePath = "/Users/haani/Documents/Spring 2023/ECE 461/Haani's Fork/ECE-461-Haani-Repository/Url File.txt"

def findGitUrl(url):
    print('Function code 1', url)
    splits = url.split('/')
    packageName = splits[-1]
    url = 'https://registry.npmjs.org/' + packageName
    print('Function code 2', url)
    response = requests.get(url)
    print('Function code 3', response)
    rd = response.json()
    print(rd)
    gitUrl = rd['repository']['url']
    gitUrl = gitUrl[4:]
    gitUrl = gitUrl.replace('.git', '')
    print('Succes. Git URL is', gitUrl)

    return gitUrl


def parseUrls(urlFilePath):
    try:
        fp = open(urlFilePath)
        urls = fp.readlines()
    finally:
        fp.close()
    return urls

def urlValidator(urls):
    validatedUrls = []
    for url in urls:
        if validators.url(url) is True and 'github.com' in url:
            print(url)
            validatedUrls.append(url.replace('\n',''))
        elif validators.url(url) is True and 'www.npmjs.com' in url:
            print(url)
            gitUrl = findGitUrl(url)
            #print(gitUrl)
            #validatedUrls.append(gitUrl.replace('\n',''))
    return validatedUrls

urls = parseUrls(urlFilePath)
for i in range(len(urls)):
    urls[i] = urls[i].replace('\n','')
validUrls = urlValidator(urls)

with open("Validated Urls", "w") as f:
    for url in validUrls:
        print(url, file=f)

#findGitUrl('https://www.npmjs.com/package/express')
