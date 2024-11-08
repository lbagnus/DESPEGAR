from pymongo import MongoClient
from datetime import datetime
import random
from bson import ObjectId

def connect_mongodb():
    client = MongoClient('mongodb://localhost:27017/')  # Cambia si tienes otra configuración
    db = client['agencia_viajes']
    return db
db = connect_mongodb()
print(db)


def disponibilidad():
    random_bool = bool(random.randint(0, 1))
    return random_bool

def habitaciones():
    habitaciones = []
    i = 0
    n = int(input("Cuantas habitaciones tiene? "))
    while i < n :
        habitacion = input ("Ingresa el tipo de habitacion (doble o simple): ")
        habitaciones.append(habitacion)
        i += 1
    return habitaciones

def telefono():
    telefonos = []
    while True:
        telefono = input("Ingresa teléfono: ")
        telefonos.append(telefono)  # Agregar el teléfono a la lista
        continuar = input("¿Deseas agregar otro teléfono? (sí/no): ").strip().lower()
        if continuar != 'si':
            break
    return telefonos

def login():
    print("<< BIENVENIDOS A DESPEGAR >>\n")
#hacer reserva o crear hotel
    data = {
    "_id": ObjectId(),  # Generar un nuevo ObjectId
    "nombre": input("Ingresa tu nombre y apellido: "),
    "direccion": {
        "calle": input("Ingresa tu calle: "),
        "numero": input("Ingresa el número: "),
        "ciudad": input("Ingresa la ciudad: "),
        "pais": input("Ingresa tu país: ")
    },
    "telefono": telefono(),  
    "email": input("Ingresa tu email: ")
    }
    insertar_cliente(data)
    print ("--- Se ha registrado correctamente ---\n ")

def operaciones():
    print("Que queres hacer?\n")
    print("1. Reservar\n2. Agregar alojamiento \n")
    opcion = input("Selecciona: ")
    if opcion == "2":
        datos_hotel = {
            "_id": ObjectId(),
            "nombre": input("Nombre del alojamiento: "),
            "direccion": {
                "calle": input("Ingresa la calle: "),
                "numero": input("Ingresa el número: "),
                "ciudad": input("Ingresa la ciudad: "),
                "pais": input("Ingresa el país: "),
                "zona": input("Centrica o periferia: ")
            },
            "tipo_alojamiento": input("Ingrese el tipo de alojamiento: "),
            "nEstrellas": input("Ingresa el número de estrellas: "),
            "tipo_Habitaciones" : habitaciones(),
            "precio" : int(input("Ingrese el precio por noche: ")),
            "disponibilidad": disponibilidad(),
            "fecha": datetime.now(),
        }
        insertar_hotel(datos_hotel)
        print ("--- Se ha registrado correctamente ---\n ")


def insertar_cliente(data):
    db.clientes.insert_one(data)
def insertar_hotel(data):
    db.hotel.insert_one(data)


def eliminar ():
    db.pais.drop()
    db.ciudad.drop()
    db.clientes.drop()
    db.vuelo.drop()
    db.hotel.drop()
    db.paqueteTuristico.drop()
    db.reservas.drop()
    db.pago.drop()
    db.personaEnReserva.drop()
    # Verificar colecciones restantes
    print("Colecciones actuales en la base de datos:", db.list_collection_names())
def view_all_documents():
    db = connect_mongodb()
    collections = db.list_collection_names()  # Obtiene todas las colecciones en la base de datos

    for collection in collections:
        print(f"\nDocumentos en la colección '{collection}':")
        documents = db[collection].find()  # Obtiene todos los documentos de la colección
        for doc in documents:
            print(doc)
#view_all_documents()
#eliminar()
