import validators
import sys



def parseUrls(urlFilePath):
    try:
        fp = open(urlFilePath)
        urls = fp.readlines()
    finally:
        fp.close()
    return urls

def urlValidator(urls):
    validatedUrls = []
    npmUrls = []
    for url in urls:
        if validators.url(url) is True and 'github.com' in url:
            validatedUrls.append(url.replace('\n',''))
        elif validators.url(url) is True and 'npmjs.com' in url:
            npmUrls.append(url.replace('\n',''))

    return validatedUrls, npmUrls

def urlParse(urlFilePath):
    urls = parseUrls(urlFilePath)
    validUrls, npmUrls = urlValidator(urls)

    # with open("Validated Urls", "w") as f:
    #     for url in validUrls:
    #         print(url, file=f)
    return validUrls, npmUrls