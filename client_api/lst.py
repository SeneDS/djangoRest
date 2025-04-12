
import requests
from getpass import getpass



endpoint = "http://127.0.0.1:8001/ecom/auth/"
auth_response= requests.get(endpoint)
username= input("Entrez votre username: \n")
password = getpass("Entez votre password: \n")
auth_response = requests.post(endpoint, json = {"username" :username, "password" :password})
print(auth_response.json())



if auth_response.status_code == 200:
    endpoint = "http://127.0.0.1:8001/product/create-list/"


    headers = {"Authorization": "Token " + auth_response.json()["token"]  }

    print(headers)

    responses = requests.get(endpoint, headers=headers)
    print("✅ Statut:", responses.status_code)
    print("📦 Réponse:", responses.json())




    #endpoint = "http://127.0.0.1:8001/product/list/"





