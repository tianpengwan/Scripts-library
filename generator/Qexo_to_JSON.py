import requests 
import json

url = "https://admin.uyoahz.cn/pub/friends/"
response = requests.get(url)  
data = response.json()['data']  

friends_circle = {"friends": []}
for count, friend in enumerate(data):  
    friends = [friend['name'], friend['url'], friend['image']]
    friends_circle["friends"].append(friends)

print(friends_circle)
friends_json = json.dumps(friends_circle)

with open('friends.json', 'w') as f:
    f.write(friends_json)
