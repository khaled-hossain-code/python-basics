try:
  file = open("text1.txt")
except:
  print "file can not be openned"
  exit()

for line in file:
  print line.rstrip()
