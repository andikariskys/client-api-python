import requests
import os

url = "https://restaurant-api.dicoding.dev/list"
respon = requests.get(url)

if respon.status_code == 200 :
    data = respon.json()
    data_resto = data['restaurants']
    # print(data_resto)
    i = 0
    while i < len(data_resto):
        print(data_resto[i])
        i +=1
