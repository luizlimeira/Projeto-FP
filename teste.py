import json

x = input("Digite nome: ")
y = input("Digite idade: ")
z = input("Digite cidade: ")

my_dict = {
  "pessoas": 
    [
      {"nome": x, "idade": int(y), "cidade": z},
      {"nome": "fodase", "idade": 25, "cidade": "Salgadinho"}
    ]
  }

with open("data.json", "w") as file:
    json.dump(my_dict, file, indent=5)