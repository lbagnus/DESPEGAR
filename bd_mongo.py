from pymongo import MongoClient
from datetime import datetime

def connect_mongodb():
    client = MongoClient('mongodb://localhost:27017/')  # Cambia si tienes otra configuración
    db = client['agencia_viajes']
    return db
db = connect_mongodb()
print(db)

def insert_data_mongodb():
    
    def sumar_precios(reserva_id):
    
        # 1. Obtener el documento de reserva por ID
        reserva = db.reservas.find_one({"_id": reserva_id})
        total_precio = 0
        
        if not reserva:
            print(f"No se encontró ninguna reserva con ID: {reserva_id}")
            return 0
        
        print(f"Detalles de la reserva: {reserva}")
        
        # 2. Obtener los IDs de los vuelos referenciados en servicios
        for servicio in reserva.get("servicios", []):
            if "precio" in servicio:
                total_precio += servicio["precio"]
        
        return total_precio
    
    def get_pais_by_id(pais_id):
        pais = db.pais.find_one({"_id": pais_id})
        return pais

    def get_ciudad_by_id(ciudad_id):
        ciudad = db.ciudad.find_one({"_id": ciudad_id})
        return ciudad
    
    # Insertar datos en la colección de clientes y obtener sus IDs

    pais_data = [
        {"_id": "ARG", "nombre": "Argentina"},
        {"_id": "ESP", "nombre": "España"},
        {"_id": "GBR", "nombre": "Reino Unido"},
        {"_id": "FRA", "nombre": "Francia"}
    ]
    db.pais.insert_many(pais_data)

    # Definición de datos de ciudad con códigos postales
    ciudad_data = [
        {"_id": "CABA", "nombre": "Buenos Aires", "pais":  get_pais_by_id("ARG")},
        {"_id": "MAD", "nombre": "Madrid", "pais": get_pais_by_id("ESP")},
        {"_id": "BCN", "nombre": "Barcelona", "pais": get_pais_by_id("ESP")},
        {"_id": "LON", "nombre": "Londres", "pais": get_pais_by_id("GBR")},
        {"_id": "PAR", "nombre": "París", "pais": get_pais_by_id("FRA")}
    ]
    db.ciudad.insert_many(ciudad_data)


    cliente_data = [
        {  
            "_id": 1,
            "nombre": "Juan Pérez",
            "direccion": {
                "calle": "Belgrano",
                "numero": 1095,
                "ciudad": "San Fernando",
                "Provincia": "Buenos Aires",
                "Pais": "Argentina"
            },
            "telefono": ["12345678", "1122628497"],
            "email": "juan@example.com"
        },
        {  
            "_id": 2,
            "nombre": "Maria Gomez",
            "direccion": {
                "calle": "Rivadavia",
                "numero": 850,
                "ciudad": "Córdoba",
                "Provincia": "Córdoba",
                "Pais": "Argentina"
            },
            "telefono": ["22334455", "1167891234"],
            "email": "maria@example.com"
        },
        { 
            "_id": 3,
            "nombre": "Carlos López",
            "direccion": {
                "calle": "San Martín",
                "numero": 1234,
                "ciudad": "Rosario",
                "Provincia": "Santa Fe",
                "Pais": "Argentina"
            },
            "telefono": ["44556677", "1133445566"],
            "email": "carlos@example.com"
        },
        {
            "_id": 4,
            "nombre": "Ana Fernández",
            "direccion": {
                "calle": "Mitre",
                "numero": 2222,
                "ciudad": "Mendoza",
                "Provincia": "Mendoza",
                "Pais": "Argentina"
            },
            "telefono": ["66778899", "1144556677"],
            "email": "ana@example.com"
        }
    ]
    db.clientes.insert_many(cliente_data)

     # Insertar datos en la colección de vuelos
    vuelo_data = [
        {"_id": 0,"nro_vuelo": "AR123", "ciudad_origen": get_ciudad_by_id("CABA"), "ciudad_destino": get_ciudad_by_id("MAD"), "fecha_salida": datetime(2024, 10, 28, 15, 30), "fecha_llegada": datetime(2024, 10, 28, 20, 30), "duracion": "5:00", "precio": 500},
        {"_id": 1,"nro_vuelo": "AR124", "ciudad_origen": get_ciudad_by_id("CABA"), "ciudad_destino": get_ciudad_by_id("BCN"), "fecha_salida": datetime(2024, 11, 1, 15, 30), "fecha_llegada": datetime(2024, 11, 1, 20, 30), "duracion": "5:00", "precio": 550},
        {"_id": 2,"nro_vuelo": "AR125", "ciudad_origen": get_ciudad_by_id("CABA"), "ciudad_destino": get_ciudad_by_id("PAR"), "fecha_salida": datetime(2024, 11, 5, 15, 30), "fecha_llegada": datetime(2024, 11, 5, 20, 30), "duracion": "5:00", "precio": 600},
        {"_id": 3,"nro_vuelo": "AR126", "ciudad_origen": get_ciudad_by_id("CABA"), "ciudad_destino": get_ciudad_by_id("LON"), "fecha_salida": datetime(2024, 11, 9, 15, 30), "fecha_llegada": datetime(2024, 11, 9, 20, 30), "duracion": "5:00", "precio": 650}
    ]
    db.vuelo.insert_many(vuelo_data)

    # Insertar datos en la colección de hoteles
    hotel_data = [
        {"_id": 0,"ciudad": get_ciudad_by_id("MAD"), "nombre": "Hilton", "direccion": {"calle": "10 de mayo", "numero": 1095, "ciudad": "Madrid", "Provincia": "Madrid", "Pais": "España"}, "estrellas": "5", "precio": 300, "tipo_habitacion": "simple", "disponibilidad": "libre", "fecha_agregada":datetime(2024, 11, 9)},
        {"_id": 1,"ciudad": get_ciudad_by_id("BCN"), "nombre": "Sheraton", "direccion": {"calle": "Avenida Diagonal", "numero": 1234, "ciudad": "Barcelona", "Provincia": "Barcelona", "Pais": "España"}, "estrellas": "4", "precio": 250, "tipo_habitacion": "doble", "disponibilidad": "libre", "fecha_agregada":datetime(2020, 10, 6)},
        {"_id": 2,"ciudad": get_ciudad_by_id("PAR"), "nombre": "Le Meridien", "direccion": {"calle": "Rue de Rivoli", "numero": 555, "ciudad": "Paris", "Provincia": "Ile-de-France", "Pais": "Francia"}, "estrellas": "5", "precio": 350, "tipo_habitacion": "suite", "disponibilidad": "libre", "fecha_agregada":datetime(2023, 8, 9)},
        {"_id": 3,"ciudad": get_ciudad_by_id("LON"), "nombre": "Ritz", "direccion": {"calle": "Piccadilly", "numero": 200, "ciudad": "Londres", "Provincia": "Greater London", "Pais": "Reino Unido"}, "estrellas": "5", "precio": 400, "tipo_habitacion": "suite", "disponibilidad": "ocupado", "fecha_agregada":datetime(2024, 5, 10)}
    ]
    db.hotel.insert_many(hotel_data)

    # Insertar datos en la colección de paquetes turísticos referenciando vuelo y hotel
    paqueteTuristico_data = [
        {"_id": 0,"nombre": "Noche de lujo en Madrid", "descripcion": "Noche de lujo para 2 personas en el Hilton de Madrid con vuelo incluido desde Buenos Aires.", "precio": vuelo_data[0]['precio'] + hotel_data[0]['precio']* 0.9, "id_ciudad": get_ciudad_by_id("MAD"), "id_vuelo": vuelo_data[0], "id_hotel": hotel_data[0]},
        {"_id": 1,"nombre": "Fin de semana en Barcelona", "descripcion": "Estancia para 2 personas en el Sheraton de Barcelona con vuelo incluido desde Buenos Aires.", "precio": vuelo_data[1]['precio'] + hotel_data[1]['precio']*0.9, "id_ciudad": get_ciudad_by_id("BCN"), "id_vuelo": vuelo_data[1], "id_hotel": hotel_data[1]},
        {"_id": 2,"nombre": "Escapada romántica a París", "descripcion": "Estancia de 2 noches para pareja en el Le Meridien de París con vuelo incluido desde Buenos Aires.", "precio": vuelo_data[2]['precio'] + hotel_data[2]['precio'] * 0.9, "id_ciudad": get_ciudad_by_id("PAR"), "id_vuelo": vuelo_data[2], "id_hotel": hotel_data[2]},
        {"_id": 3,"nombre": "Aventura en Londres", "descripcion": "Estancia de 3 noches en el Ritz de Londres con vuelo incluido desde Buenos Aires.", "precio": vuelo_data[3]['precio'] + hotel_data[3]['precio'] * 0.9, "id_ciudad": get_ciudad_by_id("LON"), "id_vuelo": vuelo_data[3], "id_hotel": hotel_data[3]}
    ]
    db.paqueteTuristico.insert_many(paqueteTuristico_data)

    # Insertar datos en la colección de reservas referenciando clientes
    reserva_data = [
        {
            "_id": 0,
            "id_cliente": cliente_data[0],
            "fecha_reserva": datetime(2024, 10, 23),
            "estado": "confirmada",
            "servicios": [vuelo_data[0], vuelo_data[1], hotel_data[0]]
        },
        {
            "_id": 1,
            "id_cliente": cliente_data[1],
            "fecha_reserva": datetime(2024, 10, 24),
            "estado": "pendiente",
            "servicios": [vuelo_data[2], hotel_data[0], hotel_data[1]]
        },
        {
            "_id": 2,
            "id_cliente": cliente_data[2],
            "fecha_reserva": datetime(2024, 10, 25),
            "estado": "confirmada",
            "servicios": [paqueteTuristico_data[0]]
        },
        {
            "_id": 3,
            "id_cliente": cliente_data[3],
            "fecha_reserva": datetime(2024, 10, 26),
            "estado": "cancelada",
            "servicios": [paqueteTuristico_data[2]]
        }
    ]
    db.reservas.insert_many(reserva_data)

    # Insertar datos en la colección de personaEnReserva referenciando reservas
    personaEnReserva_data = [
        {"id_reserva": reserva_data[0], "pasaporte": "ABC123", "nombre": "Jose Perez"},
        {"id_reserva": reserva_data[0], "pasaporte": "DEF456", "nombre": "Lucia Gomez"},
        {"id_reserva": reserva_data[1], "pasaporte": "GHI789", "nombre": "Carlos Lopez"},
        {"id_reserva": reserva_data[2], "pasaporte": "JKL012", "nombre": "Ana Fernandez"}
    ]
    db.personaEnReserva.insert_many(personaEnReserva_data)

    # Insertar datos en la colección de pago referenciando reservas
    pago_data = [
        {"_id": 0,"monto":  sumar_precios(0) ,"fecha_pago": datetime(2024, 1, 10), "estado": "pago", "metodo": "mercado pago", "id_reserva": reserva_data[0]},
        {"_id": 1,"monto": sumar_precios(1), "fecha_pago": datetime(2024, 1, 15), "estado": "pendiente", "metodo": "transferencia", "id_reserva": reserva_data[1]},
        {"_id": 2,"monto": sumar_precios(2), "fecha_pago": datetime(2024, 1, 20), "estado": "cancelado", "metodo": "efectivo", "id_reserva": reserva_data[2]},
        {"_id": 3,"monto": sumar_precios(3), "fecha_pago": datetime(2024, 1, 25), "estado": "pago", "metodo": "tarjeta", "id_reserva": reserva_data[3]}
    ]
    db.pago.insert_many(pago_data)

    print("Se insertaron correctamente")


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
def consultar_vuelos():
    vuelos = db.vuelos.find()
    return vuelos
# Ejecuta la función para insertar datos
    #insert_data_mongodb()
    #eliminar()

#Consultas
consultar_vuelos()
view_all_documents()