
#The MetMuseum 400000 item Collection is organized by Object ID, starting approximately at 10000 and going up to 700000. Not all ID numbers are attributed.
#The code requests the API, gets the json response and checks if the object ID coresponds to a HIghlight. If so, checks the Image Link and downloads it
#If only looking for Highlights, there will be large sections of the ID list which have no Highlights, as there are only around 1000 highlights in the collection.
#Connection timeout is likely, thus the last ID printed can be set as the objectID parameter to continue to scrap from there.
#If you wish to get all images, change r_dict['isHighlight'] equal to False:


import requests
import re


#Change object ID to the last one downloaded to go through images
objectID = 491691

IDlimit = 20000

r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/%s'%objectID)

#The range sets how many IDs gonna check
for x in range (1,IDlimit):
	#iterates the ID
	objectID += 1
	#makes the request which the new ID that is now looping
	new_r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/%s'%objectID)

	#get all category information in request in json format in a dictionary
	r_dict = new_r.json()
	
	print(objectID)
	#creates an exception in case there is no objectID for that number
	if r_dict == {'message': 'ObjectID not found'} :
		continue
	
	if r_dict['isHighlight'] == True:
		#Gets the link from the API

		imagelink = r_dict['primaryImage']
		#activates the code when the link exists
		if imagelink != '':
			imagecontent = requests.get('%s'%imagelink)
			requests.get('%s'%imagelink)
			filename = "%s"%r_dict['title'][:60]
			cleanfilename = re.sub(r'[^a-zA-Z0-9,.]', ' ', filename)
			print(cleanfilename)
			with open("%s"%(cleanfilename + " %s"%(objectID) + ".jpg"), "wb") as output:
    				output.write(imagecontent.content)


