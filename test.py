import requests
import json
import sys

#Capture all arguments into a single string
args = sys.argv[1:]
result = ''
for arg in args:
    result =result+' '+arg
	
if len(sys.argv)<2:
 print("Movie name should not be empty")
else: 
  #movie='The Rotten Tomatoes'
  url='http://www.omdbapi.com/?s='+result.strip()+'&apikey=806e0135'
  req = requests.get(url)
  data=json.loads(req.text)

  if(data['Response'] == "True"):  
    print("TITLE : "+data['Search'][0]['Title'])
    print("YEAR : "+data['Search'][0]['Year'])
    print("IMDBID : "+data['Search'][0]['imdbID'])
    print("TYPE : "+data['Search'][0]['Type'])
    print("POSTER : "+data['Search'][0]['Poster'])
  else:
    print("No Results Found.")