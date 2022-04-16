
import json
import mysql.connector

auto = '''{
    "marca": "Ford",
    "modelo": "Mustang",
    "anio": 1968,
    "colores": ["Rojo","Blanco","Azul","Negro"] 
}'''


argo = '''{
    "nombre": "Alan Brito",
    "edad": 25,
    "cargo": "Navegante",
    "habilidades": ["Cocinar","Luchar","Tocar ukulele"]
}'''

x = json.load(auto)

y = json.load(argo)

with open("lista.json","w") as file:
    json.dump(x, file , indent=4)
    json.dump(y, file , indent=4)

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="argonautas"
    )

cursor = con.cursor()

def selectAll():
    sql = "Select * from argonauta"
    cursor.execute(sql) 
    res = cursor.fetchall()
    return res

def pasarAjsonDoc(lista):



    with open("lista.json","w") as file:
        json.dump(lista, file , indent=4)

# lista = selectAll()
# for i in lista:
#     print (type(i))

