from urlParser import *
from API_GraphQL import *
from API import *

urlFilePath = sys.argv[1]
print(urlFilePath)

validUrls,npmUrls = urlParse(urlFilePath)
write(validUrls,token)
run_QL()