import pytest
import sys
from API import *
from graphQlAPI import *
from npmAPI import *
from urlParser import *

def test_main_functionality():
    # Set the API key
    sys.argv = ['', 'API_KEY']
    token = config('API_KEY')
    assert token is not None

    # Set the URL file path
    urlFilePath = "/Users/haani/Documents/Spring 2023/ECE 461/Haani's Fork/ECE-461-Haani-Repository/Url File.txt"

    # Test the `generateValidUrls` function
    validUrls = generateValidUrls(urlFilePath)
    assert validUrls is not None
    assert len(validUrls) > 0
    assert all(isinstance(url, str) for url in validUrls)

    # Test the `generateGraphQLData` function
    data = generateGraphQLData(validUrls)
    assert data is not None
    assert len(data) > 0
    assert all(isinstance(datum, dict) for datum in data)

    # Test the `write` function
    write(validUrls, token)
    # Add additional assertions as needed to verify the data has been written correctly

def compare_open_issues(hardcoded_value):
    # Get the open issues from the API
    open_issues = get_open_issues_from_api()
    
    if open_issues == hardcoded_value:
        return "The value of open issues is equal to the hardcoded value of %d." % hardcoded_value
    else:
        return "The value of open issues is not equal to the hardcoded value of %d." % hardcoded_value

