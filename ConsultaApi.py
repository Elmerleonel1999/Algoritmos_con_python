import requests as rq
from tabulate import tabulate

data = []
# aqui obtengo el nombre de pikachu solicitandolo a la api de pokemon
# response = rq.get("https://pokeapi.co/api/v2/pokemon/25")
# rs = response.json()
# rs2 = rs["forms"][0]["name"]
# print(rs2)

response2 = rq.get("https://pokeapi.co/api/v2/pokemon?limit=100")
res = response2.json()
for i in range(25):
  data.append([i + 1, res["results"][i]["name"], res["results"][i]["url"]])

tabla = tabulate(data, headers=["Nº", "NAME", "URL"])
print("\n\n", tabla, "\n\n")