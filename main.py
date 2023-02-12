from urlParser import *
from API_GraphQL import *
from API import *

urlFilePath = sys.argv[1]

validUrls,npmUrls = urlParse(urlFilePath)
write(validUrls,token)
get_info(validUrls)