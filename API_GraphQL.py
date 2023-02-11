import requests
from decouple import config

token = config('API_KEY')

headers = {"Authorization": 'Bearer ' + token}


def run_graphQlQuery(graphQlQuery):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': graphQlQuery}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, graphQlQuery))


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
def run_QL():
  graphQlQuery = """
  {
    viewer {
      login
    }
    rateLimit {
      limit
      cost
      remaining
      resetAt
    }
  }
  """

  result = run_graphQlQuery(graphQlQuery)  # Execute the query
  remaining_rate_limit = result["data"]["rateLimit"]["remaining"]  # Drill down the dictionary
#print("Remaining rate limit - {}".format(remaining_rate_limit))

  with open("outputGraphQl.txt", "w") as f:
      print("Remaining rate limit - {}".format(remaining_rate_limit), file=f)
