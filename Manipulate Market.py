import requests

url = "http://127.0.0.1:8080"



x = requests.get(url+"/register", json={"startBalanceA" : 1000.0, "startBalanceB" : 1000.0})
print(x.json())

y = requests.post(url+"/placeOrder", json={"userID" : x.json()["userID"],
                   "ask" : True,
                   "unitPrice" : 0.2,
                   "quantity" : 500.0})

print(x.text)
print(y.text)

x = requests.get(url+"/register", json={"startBalanceA" : 1000.0, "startBalanceB" : 1000.0})
print(x.json())

y = requests.post(url+"/placeOrder", json={"userID" : x.json()["userID"],
                   "ask" : True,
                   "unitPrice" : 0.3,
                   "quantity" : 500.0})

print(x.text)
print(y.text)

x = requests.get(url+"/register", json={"startBalanceA" : 1000.0, "startBalanceB" : 1000.0})
print(x.json())

y = requests.post(url+"/placeOrder", json={"userID" : x.json()["userID"],
                   "ask" : False,
                   "unitPrice" : 0.1,
                   "quantity" : 500.0})

print(x.text)
print(y.text)

x = requests.get(url+"/register", json={"startBalanceA" : 1000.0, "startBalanceB" : 1000.0})
print(x.json())

y = requests.post(url+"/placeOrder", json={"userID" : x.json()["userID"],
                   "ask" : False,
                   "unitPrice" : 0.15,
                   "quantity" : 500.0})

print(x.text)
print(y.text)