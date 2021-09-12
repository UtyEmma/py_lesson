# from json import loads
import json

# Sample Json
userJSON = '{"firstname" : "John", "lastname": "Doe", "age": 30}'

# Parser to Python Dictionary
user = json.loads(userJSON)
print(user)

newJSON = json.dumps(user)
print(newJSON)