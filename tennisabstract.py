import urllib2
response = urllib2.urlopen("http://www.tennisabstract.com/cgi-bin/player.cgi?p=RogerFederer")
# response = urllib2.urlopen(val)
responseVal = response.read()
print responseVal
