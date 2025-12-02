
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["biblioteca"]
coleccion = db["libros"]

def agregar():
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado = input("Estado lectura: ")
    doc = {"titulo": titulo, "autor": autor, "genero": genero, "estado": estado}
    coleccion.insert_one(doc)
    print("Libro agregado.")

def actualizar():
    titulo = input("Título del libro a actualizar: ")
    libro = coleccion.find_one({"titulo": titulo})
    if not libro:
        print("No encontrado.")
        return
    nuevo = {
        "titulo": input("Nuevo título: "),
        "autor": input("Nuevo autor: "),
        "genero": input("Nuevo género: "),
        "estado": input("Nuevo estado: ")
    }
    coleccion.update_one({"_id": libro["_id"]}, {"$set": nuevo})
    print("Actualizado.")

def eliminar():
    titulo = input("Título eliminar: ")
    coleccion.delete_one({"titulo": titulo})
    print("Eliminado.")

def ver():
    for l in coleccion.find():
        print(l)

def buscar():
    campo = input("Buscar por (titulo/autor/genero): ")
    valor = input("Valor: ")
    for l in coleccion.find({campo: valor}):
        print(l)

def menu():
    while True:
        print("1 Agregar
2 Actualizar
3 Eliminar
4 Ver
5 Buscar
6 Salir")
        op=input("> ")
        if op=="1": agregar()
        elif op=="2": actualizar()
        elif op=="3": eliminar()
        elif op=="4": ver()
        elif op=="5": buscar()
        elif op=="6": break

if __name__=="__main__":
    menu()
