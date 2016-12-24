import urllib

handler = urllib.urlopen('http://www.iddbd.net/')

for line in handler:
  print line.rstrip()