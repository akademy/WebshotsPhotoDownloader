# Webshots grabber

"Login, list and download all photos at fullsize into folders with album name"

import os
import sys
import time

import urllib
import httplib2

import getAlbums
import getPhotos
import getFullSizePhoto

# 
# Place your Username and password here before running
#
if len(sys.argv) != 3:
   print "Usage: webshots.py <username> <password>"
   sys.exit(0)

user = sys.argv[1] 
password = sys.argv[2]	

# Authenticate login.
url = 'http://www.webshots.com/login'
body = { 'done':'http%3A%2F%2Fwww.webshots.com%2Fhomepage.html', 'username': user, 'password': password, 'I1.x':'0', 'I1.y':'0', 'I1':'Login' }
headers = {'Content-type': 'application/x-www-form-urlencoded'}

print "Accessing " + user + "'s photos..."

http = httplib2.Http()
response, content = http.request(url,'POST', headers=headers, body=urllib.urlencode(body))

headers['Cookie'] = response['set-cookie']

print "Obtaining albums..."
albums = getAlbums.getAlbumsFromUser( user, http, headers )

if len( albums ) > 0 :
	print  str( len( albums ) ) + " albums found."

	rootPath = "webshots"
	if os.path.exists( rootPath ) == False:
		os.mkdir( rootPath )

	photolist = ""
	for albumUrl in albums:
		albumName, photos = getPhotos.getPhotosFromAlbum( albumUrl, http, headers )
	
		print albumName + " : " + str( len( photos ) ) + " photos (or videos)"

		albumPath = rootPath + "/" + albumName
		if os.path.exists( albumPath ) == False:
			os.mkdir( albumPath )

		for photoName, photoUrl in photos.iteritems():
			photoFullUrl = getFullSizePhoto.getFullSizePhotoFromPhotoPage( photoUrl, http, headers )

			if photoFullUrl != "" :

				photoFileOutput = albumPath + "/" + photoName + ".jpg"

				if os.path.exists( photoFileOutput ) == False:
					print "  Retrieving " + photoName
					response, image = http.request( photoFullUrl, 'GET', headers=headers )		

					fopen = open( photoFileOutput, "wb" )
					fopen.write( image )
					fopen.close();
	
					photolist += albumName + "   " + photoName + "   " + photoFullUrl + "\n"

					time.sleep(3) # sleep so we don't hit webshots to often (this is 3 seconds, 100 photos will take *at least* 5 minutes)

					#break # Just get the one for testing
		time.sleep(1) 

		#break

	fopen = open( rootPath + "/photolist.txt", "a" )
	fopen.write( photolist )
	fopen.close()
else:
	print "No albums found, were your username and password correct?"



