import requests

endpoint = "http://127.0.0.1:8001/product/"
responses = requests.get(endpoint)
print(responses.json())
print(responses.status_code)

## HTTP Resquest renvoie les données sous forme de html. dans ce cas ce n'est plus une api. Par ce qu'une api doit renvoyer le json ou le xml sinon c'est une requette http
# RESR API HTTP ----> JSON JAVASCRIPT OBJECT NOTATION