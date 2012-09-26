#python

import urllib2

url_string = "http://download.thinkbroadband.com/10MB.zip"

file_string = url_string.split('/')[-1]
url = urllib2.urlopen(url_string)
file = open("e:/" + file_string, 'w+')
file_size = int(url.info().getheaders("Content-Length")[0])

lx.out("Downloading:%s / Bytes:%s" % (file_string, file_size))

downloaded = 0
block_size = 8192

while True:
    buffer = url.read(block_size)
    if not buffer:
        break;

    downloaded += len(buffer)
    file.write(buffer)
    progress = downloaded * 100.0 / file_size
    status = "%10d [%6.2f%%]" % (downloaded, progress)
    lx.out(status)

file.close()
lx.out("download done.")
