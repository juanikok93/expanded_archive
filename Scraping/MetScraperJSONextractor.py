
# image_files takes a folder where all Highlight Images from MetCollection have been downloaded. It takes the name (whose format is artworkname_IDnumber.jpg), takes the IDnumber
# and requests all the available data for that ID in JSON format, saving it all to the 'MetHighlightsData.json' file. The data available is useful for collection analysis.

import requests
import re
import os
import glob
import json
from tqdm import tqdm


#takes in the file names for the directory in which couldn't download the image cause size or whatever
image_files = sorted(glob.glob(r"D:\Path\to\MetImage\Highlights\*.jpg"))
#some auxiliary list 
num = ['1','2','3','4','5','6','7','8','9','0']
loop = tqdm()


#Taking the index from the image names that couldn't download
img_idx = []
for i in image_files:
    if i[-10] in num:
        img_idx.append(i[-10:-4])
    else:
        img_idx.append(i[-9:-4])

MetHighlights = dict()

for num in tqdm(img_idx):
	#Makes the request to the API
    new_r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/%s'%num)
    #get all category information in request in json format in a dictionary
    r_dict = new_r.json()
    #Value with the object ID
    IDnum = num
    #New dictionary with the ID number as key
    ID = dict ()
    #For each key in the API dictionary:
    for x in r_dict:
    	#print ('Adding: ' + x + ' to collection')
    	#A new key in the ID dictionary with the values of each category of the API
        ID[x] = r_dict[x]
        #A new key entry to the MetHighlights dictionary with the ID dictionary as content, nesting the ID dictionary within Methighlights dictionary
        MetHighlights[IDnum] = ID

with open ('MetHighlightsData.json', 'w') as f:
	json.dump(MetHighlights, f)
print('DONE')

