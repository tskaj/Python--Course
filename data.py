import json

with open("data.json", "r" ) as w:
    data = json.load(w)

print("wow")

mydict = {
    "Abdullah" : 'single',
    "age"   : 20
}

with open("data2.json", "w") as f:
    f.write(json.dumps(mydict, indent = 2))          


with open("data3.json", "w") as f:
    json.dump(mydict, f, indent = 2)   

json_string = '''
    {
    "Employees": [
            {
                "id": 1,
                "Role": "intern",
                "Experience" : 3,
                "Full-time" : true
            },
            {
                "id": 2,
                "name": "Tim",
                "Experience": 21,
                "Full-time": true
            },
            {
                "id" : 2,
                "name" : "Joe",
                "Experience": 33,
                "Full-time": false
            }
        ]
    }
'''

data = json.loads(json_string)

print(data['Employees'][0])