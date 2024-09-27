import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "Dim", "views": 100000},
        {"likes": 41, "name": "Fwick", "views": 999987},
        {"likes": 2, "name": "Unpopular", "views": 1000000000}]

for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i), json=data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
response = requests.patch(BASE + "video/2", json={"views":99})
print(response.json())