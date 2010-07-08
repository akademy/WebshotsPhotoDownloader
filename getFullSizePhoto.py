# Get the fullsize 

def getFullSizePhotoFromPhotoPage( photoPageUrl, http, headers ):
	"Get the full sized image url"

	response, s = http.request(photoPageUrl, 'GET', headers=headers)

	photoFullSizeLocation = 'class="fullsize'
	photoHrefLocation = '<a href="'
	photoUrl = ""

	if s.find( photoFullSizeLocation ) != -1:
		posPhoto = s.find( photoFullSizeLocation )

		posHrefStart = s.find( photoHrefLocation, posPhoto ) + len( photoHrefLocation )
		posHrefEnd = s.find( '"', posHrefStart )

		photoUrl = s[posHrefStart:posHrefEnd].strip()

	return photoUrl
