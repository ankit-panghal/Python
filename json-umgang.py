import json

daten = {'modell' : 'claude-sonnet-4','maxTokens' : 10000}

json_text = json.dumps(daten) # wie stringify in js

print(type(json_text)) # str

jsonObj = json.loads(json_text) # wie parse in js
print(type(jsonObj)) # dict