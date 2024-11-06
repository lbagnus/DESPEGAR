from pymongo import MongoClient
from datetime import datetime

def connect_mongodb():
    client = MongoClient('mongodb://localhost:27017/')  # Cambia si tienes otra configuración
    db = client['agencia_viajes']
    return db
db = connect_mongodb()
print(db)


def insertar_pais(data):
    db.pais.insert_one(data)
def insertar_ciudad(data):
    db.ciudad.insert_one(data)
def insertar_cliente(data):
    db.clientes.insert_one(data)
def insertar_hotel(data):
    db.hotel.insert_one(data)
def insertar_reserva(data):
    db.reservas.insert_one(data)
def insertar_personas_reservas(data):
    db.personaEnReserva.insert_one(data)
def insert_pago(data):
    db.pago.insert_one(data)

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
