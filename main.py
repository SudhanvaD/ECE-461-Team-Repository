from API import *
from graphQlAPI import *
from npmAPI import *
from urlParser import *
import sys


if __name__ == "__main__":
    token = config('API_KEY')
    #urlFilePath = sys.argv[1] #.split("/").pop()
    urlFilePath = "/Users/haani/Documents/Spring 2023/ECE 461/Haani's Fork/ECE-461-Haani-Repository/Url File.txt"
    validUrls = generateValidUrls(urlFilePath)
    generateGraphQLData(validUrls)
    write(validUrls, token)