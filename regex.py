import re

hand = open("story.txt")

for line in hand:
  line = line.rstrip()
  if re.search('Fox',line):
    print line

text = "x-hello: x-men movie\n x-holla: not movie\n x-hihi.com\n"

print re.findall('x.*:',text)


text1 = "my fav 2 numbers are 4 & 32"

print re.findall('[0-9]+', text1) #find any digits in text1

emailAddress = "khaled@afc.com.bd anjan@gmail.com mahtab@yahoo.com"

#have to find all the email domains from the text

domains = re.findall('@([^ ]*)', emailAddress)# find @ but take within ( ) only not blank zero or more

print domains