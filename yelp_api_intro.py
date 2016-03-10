import rauth
import time

##import sys
##reload(sys)
##sys.setdefaultencoding("utf-8")

def main():
        zipcodefile = open("zip_codes_states.csv","r")
        ziplist = []
        for line in zipcodefile:
                ziplist.append(line.strip().split(","))
        latlonglist = []
        for arrs in ziplist:
                latlonglist.append(((arrs[1]),(arrs[2])))
        print("$$$$$$%%%%%%%%%*********########",latlonglist)
        
	#locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
        locations = latlonglist
        #[(40.71,-74.01),(40.78,-73.97),(42.65,-73.76),(42.44,-76.50),(37.34,-121.89),(37.77,-122.42)] #NYC,Manhattan,Albany,Ithaca
        #SJ/SF lat/long: [(37.34,-121.89)]#,(37.77,-122.42)
	api_calls = []
	print("hope this works")
	for lat,long in locations:
		params = get_search_parameters(lat,long)
		#api_calls.append(get_results(params))
		api_calls.extend(get_results(params))

		print("params:", params)
		print("DATA TYPE:",type(api_calls))
		print("data: ", api_calls)


		#Be a good internet citizen and rate-limit yourself
		time.sleep(1.0)
		
	##Do other processing
	outfile = open("writeToThisFile.csv","w")
	b = ["Name","Branch","Area code","Rating","Phone number","Reviews"]
	outfile.write(str(b)[1:-1]+"\n")
        counter = 0
        while (counter < len(api_calls)):
                row = str(api_calls[counter])[1:-1]+"\n"
                outfile.write(row)
                counter += 1
		
##		for step in api_calls:
##                        stepz = str(step) + "\n"
##                        outfile.write(stepz)
                        
        outfile.close()

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

        #
        data_businesses = data["businesses"]
        data_names = []
##        i = data_businesses[0]
##        data_names.append(i)
##        print("DATATYPEDATAYPEDATATYPEDATATYPE",type(i))

##        print(data_businesses[0])
##        for i in data_businesses:
##                for key in i:
##                        if key == u'name':
##                                data_names.append(i[key])
        #

        #try returning a DICT
##        data_dict={}
##        num = 1
##        for i in data_businesses:
##                a = []
##                count = 0
##
##                temp = ["hi"]*len(i)
##                for trish in temp:
##                        name = "Name: "+i[u'name']
##                        rating = "Rating: "+str(i[u'rating'])
##                        phonenum = "Phone Number: "+str(i[u'phone'])
##                        loc = i[u'location']
##                        address = loc[u'display_address']
##                        #preview = "Reviews: "+i[u'snippet_text']+"\n"
##                        
##                        a = [name,rating,phonenum,address]#preview
##                numstring = "*****"+str(num)
##                data_dict[numstring] = a
##                num += 1

        for i in data_businesses:
                all_keys = i.keys()
                a = []
                
                name = str(i[u'name']) #"Name: "+
                
                rating = i[u'rating'] #"Rating: "+str()

                phonenum = "No phone number posted"
                phone_test = False
                for a_key in all_keys:
                        if a_key==u'phone':
                                phone_test = True
                if phone_test == True:
                        phonenum = int(i[u'phone'])#str()#"Phone Number: "+

                loc = i[u'location']
                address = loc[u'display_address']
                address2 = []
                for thing in address:
                        address2.append(str(thing))
                
                ad1 = str(address2)[1:-1].split(",")
                dispad = ""
                for oneofem in ad1:
                        dispad+= oneofem
                displayad = dispad #"Branch: "+

                zipcode = int(loc[u'postal_code'])

                snippet_test = False
                for a_key in all_keys:
                        if a_key==u'snippet_text':
                                snippet_test = True
                preview2 = "No reviews posted"
                if snippet_test == True:                       
                        preview = str(i[u'snippet_text']).split(",")
                        preview1 = ""
                        for oneofem in preview:
                                preview1+= oneofem
                        preview2 = preview1#"Reviews: "++"\n"
                
                a = [name,displayad,zipcode,rating,phonenum,preview2]
                data_names.append(a)

        print("************************* ORIGINAL DATA *************************",data)
	
	session.close()

	#return data_dict
	return data_names
        #return data
		
def get_search_parameters(lat,long):
	#See the Yelp API for more details
	params = {}
	params["term"] = "Bank"#of America
	params["ll"] = "{},{}".format(str(lat),str(long))
	params["radius_filter"] = "2000"
	params["limit"] = "20"

	return params

if __name__=="__main__":
	main()
