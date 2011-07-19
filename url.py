import urllib2
request=urllib2.Request('http://python.org')
response=urllib2.urlopen(request)
#response=urllib2.urlopen("http://python.org")
html=response.read()
file=open("url_fetch.txt",'w')
file.write(html)
print "completed"
