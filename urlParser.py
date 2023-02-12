import validators
from npmAPI import findGitUrl

urlFilePath = "/Users/haani/Documents/Spring 2023/ECE 461/Haani's Fork/ECE-461-Haani-Repository/Url File.txt"

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
validUrls = urlValidator(urls)

with open("Validated Urls", "w") as f:
    for url in validUrls:
        print(url, file=f)