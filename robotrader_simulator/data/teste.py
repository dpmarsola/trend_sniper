import json

with open("teste.json", "r") as f:
    data = json.load(f)
    
for i in data:
    print(i)
    
