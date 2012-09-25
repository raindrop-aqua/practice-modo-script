#python

import urllib2

url_string = "http://download.thinkbroadband.com/10MB.zip"

file_name = url_string.split('/')[-1]
url = urllib2.urlopen(url_string)
file = open(file_name, 'wb')
meta = url.info()
file_size = int(meta.getheaders("Content-Length")[0])

print "Downloading:%s / Bytes:%s" % (file_name, file_size)

file_size_downloaded = 0
block_size = 8192

while True:
    buffer = url.read(block_size)
    if not buffer:
        break;

    file_size_downloaded += len(buffer)
    file.write(buffer)
    progress = file_size_downloaded * 100. / file_size
    status = "%10d [%6.2f%%]" % (file_size_downloaded, progress)
    status = status + "O" * (int(progress / 10))
    print status

file.close()
