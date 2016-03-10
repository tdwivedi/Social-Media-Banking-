
from yelpapi import YelpAPI
import argparse
from pprint import pprint
from rauth import OAuth1Service

print("THIS WORKS !!!!!")

def get_search_parameters(lat,long):
  #See the Yelp API for more details
  params = {}
  params["term"] = "restaurant"
  params["ll"] = "{},{}".format(str(lat),str(long))
  params["radius_filter"] = "2000"
  params["limit"] = "10"
 
  return params

def get_results(params):
 
  #Obtain these from Yelp's manage access page
  consumer_key = "czXoz2KQ0AdTkDlgu_otIA"
  consumer_secret = "PiidWpHIJzSKZOMRK98IZVXre8c"
  token = "zIr1DbP6M4USoROG3DsaVCJnmeo3bj-E"
  token_secret = "YKYWxh-X7cZHwo-FjbUs58uFZgQ"
   
  session = rauth.OAuth1Session(
    consumer_key = consumer_key
    ,consumer_secret = consumer_secret
    ,access_token = token
    ,access_token_secret = token_secret)
     
  request = session.get("http://api.yelp.com/v2/search",params=params)
   
  #Transforms the JSON API response into a Python dictionary
  data = request.json()
  session.close()
   
  return data

params = get_search_parameters(37.7833,122.4167)
print("params: ", params)
data = get_results(params)
print("This is my",data)
