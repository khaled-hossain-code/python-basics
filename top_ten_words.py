story = open("story.txt")
counts = dict()

for line in story:
  words = line.split()
  for word in words:
    counts[word]= counts.get(word,0) + 1

lst = list()

for (word,count) in counts.items():
  lst.append((count,word))

lst.sort(reverse=True)

for (val,key) in lst[:10]:
  print key,val