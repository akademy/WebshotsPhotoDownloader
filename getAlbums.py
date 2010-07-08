# Get albums

def getAlbumsFromUser( user, http, headers ):
	"Get the list of albums - Note: only a single page of albums is retrieved."

	url = "http://community.webshots.com/user/" + user

	response, s = http.request(url, 'GET', headers=headers)

	pos = 0
	albumLocation = 'class="album'
	albumHrefLocation = '<a href="'
	albums = []

	while s.find( albumLocation, pos ) != -1:
		posAlbum = s.find( albumLocation, pos )

		posHrefStart = s.find( albumHrefLocation, posAlbum ) + len( albumHrefLocation )
		posHrefEnd = s.find( '"', posHrefStart )
	
		albums.append( s[posHrefStart:posHrefEnd].strip() )

		pos = posHrefEnd

		#posNameStart = s.find( '>', posHrefStart ) + 1
		#posNameEnd = s.find( '<', posNameStart )

		#albums[s[posNameStart:posNameEnd].strip()] = s[posHrefStart:posHrefEnd].strip()

		#pos = posNameEnd

	return albums
