import requests

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

querystring = {"ingr":"cookie"}

headers = {
    'x-rapidapi-key': "32f932ef51msh331ed4d658f9775p1ef862jsnf7256ccd66f4",
    'x-rapidapi-host': "edamam-food-and-grocery-database.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)