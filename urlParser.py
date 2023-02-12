import validators
from npmAPI import findGitUrl
import git

#urlFilePath = "/Users/haani/Documents/Spring 2023/ECE 461/Haani's Fork/ECE-461-Haani-Repository/Url File.txt"

def clone(url):
    s = url.split("/").pop()
    local_path = s
    #os.makedirs(s)
    git.Repo.clone_from(url, local_path)

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
        url = url.replace('\n','')
        if validators.url(url) is True and 'github.com' in url:
            try:
                clone(url)
            except:
                print('No Access')
                # log that repo could not be cloned
            validatedUrls.append(url)
        elif validators.url(url) is True and 'www.npmjs.com' in url:
            print(url)
            gitUrl = findGitUrl(url)
            try:
                clone(gitUrl)
            except:
                print('No Access')
                 # Log that repo could not be cloned
            validatedUrls.append(gitUrl)

    for i in range(len(validatedUrls)):
        if 'ssh://git@' in validatedUrls[i]:
            print(url)
            validatedUrls[i] = validatedUrls[i].replace('ssh://git@','https://')
    return validatedUrls

def generateValidUrls(urlFilePath):
    urls = parseUrls(urlFilePath)
    validUrls = urlValidator(urls)
    return validUrls
