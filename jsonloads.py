import json

data = '''
{
  "name":"shakhi",
  "university":"south-east",
  "phone":{
    "type":"intl",
    "value":"+8801944665975"
  },
  "email":{
    "hide":"true"
  }
}'''

info = json.loads(data)
print 'Name: ',info["name"]


data1 = '''[
  { "name":"shakhi",
    "university":"south-east",
    "phone":"+8801944665975"
  },
  {  "name":"afnan",
     "university":"mist",
     "phone":"+8801944665975"
  }
]'''

info1 = json.loads(data1)

for person in info1:
  print person["name"]