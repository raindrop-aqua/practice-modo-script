#python

import urllib2

url_string = "http://download.thinkbroadband.com/10MB.zip"

r = urllib2.urlopen(url_string)
lx.out(r.code, r.msg)
lx.out(r.info())
