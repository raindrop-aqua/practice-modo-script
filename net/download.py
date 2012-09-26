# python

import urllib

url = "http://download.thinkbroadband.com/10MB.zip"
file_name = "e:/10MB.zip"
# call back
def progress(block_count, block_size, total_size):
    percentage = int(100.0 * block_count * block_size / total_size)
    lx.out("%10d [%6.2f%%]" % (block_count * block_size / 1024, percentage))

urllib.urlretrieve(url, file_name, progress)
lx.out("download done.")
