# Get the pages with photos on

def getPhotosFromAlbum( albumUrl, http, headers ):
	"Get a  list of photo page urls in this album"

	photos = dict()

	itemsPerPage = 12
	totalCount = 0;

	while True:

		response, page = http.request( albumUrl + "?start=" + str( totalCount ), 'GET', headers=headers )

		photoLocation = 'class="item'

		if page.find( photoLocation, 0 ) == -1:
			break;

		albumTitleLocation = '<h1>'
		albumTitleLocationEnd = '</h1>'	

		posAlbumTitle = page.find( albumTitleLocation, 0 ) + len( albumTitleLocation )
		posAlbumTitleEnd = page.find( albumTitleLocationEnd, posAlbumTitle )

		albumName = page[posAlbumTitle:posAlbumTitleEnd].strip()

		pos = 0
		pageCount = 0

		photoLocation = 'class="item'
		photoHrefLocation = '<a href="'
		photoTitleLocation = '<h5>'
		photoNameLocation = '<a href="'

		while page.find( photoLocation, pos ) != -1 and pageCount < itemsPerPage:
			posPhoto = page.find( photoLocation, pos )

			posHrefStart = page.find( photoHrefLocation, posPhoto ) + len( photoHrefLocation )
			posHrefEnd = page.find( '"', posHrefStart )

			posTitle = page.find( photoTitleLocation, posHrefEnd )
			posName =  page.find( photoNameLocation, posTitle )

			posNameStart = page.find( '>', posName ) + 1
			posNameEnd = page.find( '<', posNameStart )

			photos[page[posNameStart:posNameEnd].strip()] = page[posHrefStart:posHrefEnd].strip()

			pos = posNameEnd

			pageCount += 1
			totalCount += 1


	return albumName, photos


