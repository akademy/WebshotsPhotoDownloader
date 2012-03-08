Webshots Photo Download
-----------------------

Main code now on BitBucket: https://bitbucket.org/akademy/webshotsphotodownloader/overview

Download all the photos you have on webshots in the highest resolution they have. The downloads will be divided into folders by album name.

To use it just call:
python webshots.py <webshots-username> <webshots-password>

A folder called "webshots" will be created in the folder you run in. Inside that folder will be a folder for each album. 

Somethings to note:
* At the moment only the first page of albmus is downloaded.
* No videos are downloaded.
* Webshots reduces large file so the full size images may be smaller than the ones you originally uploaded.

This package users the useful httplib2 package : http://code.google.com/p/httplib2/

Some useful websites at:
# http://www.testingreflections.com/node/view/5919
# http://www.techniqal.com/blog/2008/07/31/python-file-read-write-with-urllib2/
