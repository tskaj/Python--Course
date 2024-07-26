import requests

payload = {
    "firstName": "Jhon",
    "lastName" : "smith"
}
r = requests.get("https://httpbin.org/get", params = payload)

print(r.url) #Url with the parameters

print(r.url)


r = requests.post("https://httpbin.org/post", data = payload)


print(r.text)