from urlParser import *
from API_GraphQL import *
from API import *


validUrls,npmUrls = urlParse("Url File.txt")
write(validUrls,token)
run_QL()