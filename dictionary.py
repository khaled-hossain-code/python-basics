names =['khaled','anjan','mahtab','anjan','mahtab','khaled','anjan','anjan','mahtab']
collection = dict()

for name in names:
  collection[name] = collection.get(name,0) + 1

print collection
bWord = ''
bCount = 0

for name,count in collection.items(): 
  if count > bCount:
    bWord = name
    bCount = count

print bWord,bCount