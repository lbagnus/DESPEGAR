from pymongo import MongoClient
from datetime import datetime
import random
import json
from bson import ObjectId
import bd_cassandra

def connect_mongodb():
    client = MongoClient('mongodb://localhost:27017/')  # Cambia si tienes otra configuración
    db = client['agencia_viajes']
    return db
db = connect_mongodb()
print(db)

def disponibilidad():
    random_bool = bool(random.randint(0, 1))
    return random_bool

def telefono():
    telefonos = []
    while True:
        telefono = input("Ingresa teléfono: ")
        telefonos.append(telefono)  # Agregar el teléfono a la lista
        continuar = input("¿Deseas agregar otro teléfono? (sí/no): ").strip().lower()
        if continuar != 'si':
            break
    return telefonos

def personas_reserva(cantidad):
    personas = []
        
    for i in range(cantidad):
        print(f"\nPersona {i + 1}:")
        persona = {
            "nombre": input("Ingrese el nombre y apellido: ").strip(),
            "pasaporte": input("Ingrese el pasaporte: ").strip()
        }
        personas.append(persona)
        
    return personas  

def monto(reserva,n):
    total = n+1
    if "precio" in reserva:
        return reserva["precio"] * total

def login():
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

def data_hotel():
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
            "tipo_Habitaciones" : input("Ingrese el tipo de habitacion: "),
            "precio" : int(input("Ingrese el precio por noche: ")),
            "disponibilidad": disponibilidad(),
            "fecha": datetime.now(),
        }
        insertar_hotel(datos_hotel)
        print ("--- Se ha registrado correctamente ---\n ")


def data_reserva(reserva):
    respuesta = input("¿Quiere agregar personas a la reserva? (si/no): ").strip().lower()
    
    if respuesta == "si":
        cantidad = int(input("¿Cuántas personas desea agregar?: "))
    else:
        return None
    datos_reserva = {
        "_id": ObjectId(),
        "resumen": reserva,
        "estado": "Pago",
        "personas_reserva": personas_reserva(cantidad),
        "monto": monto(reserva,cantidad),
    }
    insertar_reserva(datos_reserva)

#INSERT VUELOS
vuelos = [
    {
        "_id": ObjectId(),
        "nro_vuelo": "AA1001",
        "ciudad_origen": "Miami",
        "ciudad_destino": "Cancun",
        "fecha_salida": datetime(2024, 11, 20, 8, 0),
        "fecha_llegada": datetime(2024, 11, 20, 10, 30),
        "duracion": "2h 30m",
        "aerolinea": "American Airlines",
        "precio": 300
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "DL202",
        "ciudad_origen": "New York",
        "ciudad_destino": "San Juan",
        "fecha_salida": datetime(2024, 11, 15, 15, 0),
        "fecha_llegada": datetime(2024, 11, 15, 19, 0),
        "duracion": "4h",
        "aerolinea": "Delta Airlines",
        "precio": 400
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "CM303",
        "ciudad_origen": "Panama City",
        "ciudad_destino": "Bogotá",
        "fecha_salida": datetime(2024, 11, 21, 7, 30),
        "fecha_llegada": datetime(2024, 11, 21, 9, 0),
        "duracion": "1h 30m",
        "aerolinea": "Copa Airlines",
        "precio": 250
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "LA404",
        "ciudad_origen": "Lima",
        "ciudad_destino": "Buenos Aires",
        "fecha_salida": datetime(2024, 12, 5, 23, 0),
        "fecha_llegada": datetime(2024, 12, 6, 5, 0),
        "duracion": "4h",
        "aerolinea": "LATAM Airlines",
        "precio": 450
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "UA505",
        "ciudad_origen": "Chicago",
        "ciudad_destino": "Los Angeles",
        "fecha_salida": datetime(2024, 11, 28, 17, 0),
        "fecha_llegada": datetime(2024, 11, 28, 19, 30),
        "duracion": "4h 30m",
        "aerolinea": "United Airlines",
        "precio": 350
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "AF606",
        "ciudad_origen": "Paris",
        "ciudad_destino": "Cairo",
        "fecha_salida": datetime(2024, 12, 10, 10, 0),
        "fecha_llegada": datetime(2024, 12, 10, 16, 0),
        "duracion": "6h",
        "aerolinea": "Air France",
        "precio": 650
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "EK707",
        "ciudad_origen": "Dubai",
        "ciudad_destino": "Male",
        "fecha_salida": datetime(2024, 11, 30, 2, 0),
        "fecha_llegada": datetime(2024, 11, 30, 7, 0),
        "duracion": "5h",
        "aerolinea": "Emirates",
        "precio": 700
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "QF808",
        "ciudad_origen": "Sydney",
        "ciudad_destino": "Auckland",
        "fecha_salida": datetime(2024, 12, 12, 6, 0),
        "fecha_llegada": datetime(2024, 12, 12, 11, 0),
        "duracion": "3h",
        "aerolinea": "Qantas",
        "precio": 600
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "BA909",
        "ciudad_origen": "London",
        "ciudad_destino": "Barbados",
        "fecha_salida": datetime(2024, 12, 8, 14, 0),
        "fecha_llegada": datetime(2024, 12, 8, 21, 0),
        "duracion": "7h",
        "aerolinea": "British Airways",
        "precio": 850
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "TK1010",
        "ciudad_origen": "Istanbul",
        "ciudad_destino": "Antalya",
        "fecha_salida": datetime(2024, 11, 25, 9, 0),
        "fecha_llegada": datetime(2024, 11, 25, 10, 30),
        "duracion": "1h 30m",
        "aerolinea": "Turkish Airlines",
        "precio": 200
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "AV1111",
        "ciudad_origen": "Bogotá",
        "ciudad_destino": "Medellín",
        "fecha_salida": datetime(2024, 11, 22, 13, 0),
        "fecha_llegada": datetime(2024, 11, 22, 14, 0),
        "duracion": "1h",
        "aerolinea": "Avianca",
        "precio": 100
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "NH1212",
        "ciudad_origen": "Tokyo",
        "ciudad_destino": "Okinawa",
        "fecha_salida": datetime(2024, 11, 26, 5, 0),
        "fecha_llegada": datetime(2024, 11, 26, 8, 0),
        "duracion": "3h",
        "aerolinea": "All Nippon Airways",
        "precio": 350
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "SQ1313",
        "ciudad_origen": "Singapore",
        "ciudad_destino": "Bali",
        "fecha_salida": datetime(2024, 12, 1, 9, 0),
        "fecha_llegada": datetime(2024, 12, 1, 12, 0),
        "duracion": "3h",
        "aerolinea": "Singapore Airlines",
        "precio": 450
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "AR1414",
        "ciudad_origen": "Buenos Aires",
        "ciudad_destino": "Sao Paulo",
        "fecha_salida": datetime(2024, 12, 6, 7, 0),
        "fecha_llegada": datetime(2024, 12, 6, 10, 0),
        "duracion": "3h",
        "aerolinea": "Aerolineas Argentinas",
        "precio": 300
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "AC1515",
        "ciudad_origen": "Toronto",
        "ciudad_destino": "Vancouver",
        "fecha_salida": datetime(2024, 12, 9, 14, 0),
        "fecha_llegada": datetime(2024, 12, 9, 17, 0),
        "duracion": "5h",
        "aerolinea": "Air Canada",
        "precio": 400
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "AM1616",
        "ciudad_origen": "Mexico City",
        "ciudad_destino": "Guadalajara",
        "fecha_salida": datetime(2024, 12, 2, 16, 0),
        "fecha_llegada": datetime(2024, 12, 2, 18, 0),
        "duracion": "2h",
        "aerolinea": "Aeromexico",
        "precio": 180
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "LH1717",
        "ciudad_origen": "Frankfurt",
        "ciudad_destino": "Berlin",
        "fecha_salida": datetime(2024, 12, 11, 11, 0),
        "fecha_llegada": datetime(2024, 12, 11, 12, 30),
        "duracion": "1h 30m",
        "aerolinea": "Lufthansa",
        "precio": 150
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "VA1818",
        "ciudad_origen": "Melbourne",
        "ciudad_destino": "Perth",
        "fecha_salida": datetime(2024, 12, 4, 8, 0),
        "fecha_llegada": datetime(2024, 12, 4, 12, 0),
        "duracion": "4h",
        "aerolinea": "Virgin Australia",
        "precio": 350
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "JL1919",
        "ciudad_origen": "Tokyo",
        "ciudad_destino": "Osaka",
        "fecha_salida": datetime(2024, 12, 3, 6, 0),
        "fecha_llegada": datetime(2024, 12, 3, 7, 0),
        "duracion": "1h",
        "aerolinea": "Japan Airlines",
        "precio": 200
    },
    {
        "_id": ObjectId(),
        "nro_vuelo": "PR2020",
        "ciudad_origen": "Manila",
        "ciudad_destino": "Cebu",
        "fecha_salida": datetime(2024, 12, 3, 6, 0),
        "fecha_llegada": datetime(2024, 12, 3, 8, 0),
        "duracion": "2h",
        "aerolinea": "Philippine Airlines",
        "precio": 100
    }]
#db.vuelos.insert_many(vuelos)

#INSERT PAQUETES
paquetes = [
    {
        "_id": ObjectId(),
        "nombre": "Aventura en Cancún",
        "descripcion": "Paquete todo incluido en Cancún con excursiones a playas y zonas arqueológicas.",
        "precio": 1200,
        "ciudad": "Cancún",
        "fechas": [datetime(2024, 11, 20), datetime(2025, 1, 15)],
        "noches": 5,
        "vuelo": {
            "nro_vuelo": "AA1001",
            "ciudad_origen": "Miami",
            "ciudad_destino": "Cancún",
            "fecha_salida": datetime(2024, 11, 20, 8, 0),
            "fecha_llegada": datetime(2024, 11, 20, 10, 30),
            "duracion": "2h 30m",
            "aerolinea": "American Airlines"
        },
        "hotel": {
            "nombre": "Hotel Playa Cancún",
            "direccion": "Av. Kukulcán, Zona Hotelera, Cancún",
            "estrellas": 5,
            "habitacion": "doble",
            "alojamiento": "hotel"
        },
        "precio_total": 1500
    },
    {
        "_id": ObjectId(),
        "nombre": "Escapada a San Juan",
        "descripcion": "Descubre la belleza de Puerto Rico con alojamiento y vuelo directo.",
        "precio": 800,
        "ciudad": "San Juan",
        "fechas": [datetime(2024, 11, 15), datetime(2025, 2, 10)],
        "noches": 4,
        "vuelo": {
            "nro_vuelo": "DL202",
            "ciudad_origen": "New York",
            "ciudad_destino": "San Juan",
            "fecha_salida": datetime(2024, 11, 15, 15, 0),
            "fecha_llegada": datetime(2024, 11, 15, 19, 0),
            "duracion": "4h",
            "aerolinea": "Delta Airlines"
        },
        "hotel": {
            "nombre": "San Juan Beach Resort",
            "direccion": "Isla Verde Ave, San Juan",
            "estrellas": 4,
            "habitacion": "simple",
            "alojamiento": "hotel"
        },
        "precio_total": 1100
    },
    {
        "_id": ObjectId(),
        "nombre": "Experiencia Bogotá",
        "descripcion": "Paquete cultural en Bogotá con tours por la ciudad y visita a museos.",
        "precio": 900,
        "ciudad": "Bogotá",
        "fechas": [datetime(2024, 11, 21), datetime(2025, 3, 10)],
        "noches": 3,
        "vuelo": {
            "nro_vuelo": "CM303",
            "ciudad_origen": "Panama City",
            "ciudad_destino": "Bogotá",
            "fecha_salida": datetime(2024, 11, 21, 7, 30),
            "fecha_llegada": datetime(2024, 11, 21, 9, 0),
            "duracion": "1h 30m",
            "aerolinea": "Copa Airlines"
        },
        "hotel": {
            "nombre": "Bogotá Plaza Hotel",
            "direccion": "Calle 100 #18A-30, Bogotá",
            "estrellas": 5,
            "habitacion": "doble",
            "alojamiento": "hotel"
        },
        "precio_total": 1150
    },
    {
        "_id": ObjectId(),
        "nombre": "Escapada Romántica en París",
        "descripcion": "Un paquete para disfrutar de la ciudad del amor en París.",
        "precio": 2000,
        "ciudad": "París",
        "fechas": [datetime(2024, 12, 1), datetime(2025, 2, 28)],
        "noches": 5,
        "vuelo": {
            "nro_vuelo": "AF404",
            "ciudad_origen": "New York",
            "ciudad_destino": "París",
            "fecha_salida": datetime(2024, 12, 1, 16, 0),
            "fecha_llegada": datetime(2024, 12, 2, 6, 0),
            "duracion": "8h",
            "aerolinea": "Air France"
        },
        "hotel": {
            "nombre": "Hotel des Arts",
            "direccion": "Montmartre, París",
            "estrellas": 5,
            "habitacion": "doble",
            "alojamiento": "hotel"
        },
        "precio_total": 2400
    },
    {
        "_id": ObjectId(),
        "nombre": "Relax en Playa del Carmen",
        "descripcion": "Disfruta de un viaje de relax en la Riviera Maya, con hermosos atardeceres y playas tranquilas.",
        "precio": 1500,
        "ciudad": "Playa del Carmen",
        "fechas": [datetime(2024, 12, 5), datetime(2025, 3, 15)],
        "noches": 6,
        "vuelo": {
            "nro_vuelo": "AV301",
            "ciudad_origen": "Bogotá",
            "ciudad_destino": "Playa del Carmen",
            "fecha_salida": datetime(2024, 12, 5, 10, 0),
            "fecha_llegada": datetime(2024, 12, 5, 12, 30),
            "duracion": "3h 30m",
            "aerolinea": "Avianca"
        },
        "hotel": {
            "nombre": "Gran Porto Playa del Carmen",
            "direccion": "Av. 5ta, Playa del Carmen",
            "estrellas": 4,
            "habitacion": "doble",
            "alojamiento": "hotel"
        },
        "precio_total": 2100
    },
    {
        "_id": ObjectId(),
        "nombre": "Aventura en Costa Rica",
        "descripcion": "Disfruta de la naturaleza, volcanes y playas en Costa Rica.",
        "precio": 1300,
        "ciudad": "San José",
        "fechas": [datetime(2024, 12, 10), datetime(2025, 1, 25)],
        "noches": 5,
        "vuelo": {
            "nro_vuelo": "AA250",
            "ciudad_origen": "Los Angeles",
            "ciudad_destino": "San José",
            "fecha_salida": datetime(2024, 12, 10, 12, 0),
            "fecha_llegada": datetime(2024, 12, 10, 14, 0),
            "duracion": "4h",
            "aerolinea": "American Airlines"
        },
        "hotel": {
            "nombre": "Hotel Costa Rica",
            "direccion": "Av. Central, San José",
            "estrellas": 3,
            "habitacion": "simple",
            "alojamiento": "hotel"
        },
        "precio_total": 1500
    },
    {
        "_id": ObjectId(),
        "nombre": "Vacaciones en Punta Cana",
        "descripcion": "Relájate en las playas más hermosas de Punta Cana con todo incluido.",
        "precio": 1400,
        "ciudad": "Punta Cana",
        "fechas": [datetime(2024, 12, 15), datetime(2025, 3, 15)],
        "noches": 7,
        "vuelo": {
            "nro_vuelo": "B6A500",
            "ciudad_origen": "Boston",
            "ciudad_destino": "Punta Cana",
            "fecha_salida": datetime(2024, 12, 15, 9, 30),
            "fecha_llegada": datetime(2024, 12, 15, 13, 30),
            "duracion": "4h",
            "aerolinea": "JetBlue"
        },
        "hotel": {
            "nombre": "Hotel Bahia Punta Cana",
            "direccion": "Av. Bavaro, Punta Cana",
            "estrellas": 4,
            "habitacion": "doble",
            "alojamiento": "hotel"
        },
        "precio_total": 1900
    },
    {
        "_id": ObjectId(),
        "nombre": "Turismo en Buenos Aires",
        "descripcion": "Disfruta de las principales atracciones de Buenos Aires en este paquete de 4 noches.",
        "precio": 750,
        "ciudad": "Buenos Aires",
        "fechas": [datetime(2024, 12, 1), datetime(2025, 2, 15)],
        "noches": 4,
        "vuelo": {
            "nro_vuelo": "AR1061",
            "ciudad_origen": "Rio de Janeiro",
            "ciudad_destino": "Buenos Aires",
            "fecha_salida": datetime(2024, 12, 1, 8, 30),
            "fecha_llegada": datetime(2024, 12, 1, 10, 0),
            "duracion": "2h",
            "aerolinea": "Aerolineas Argentinas"
        },
        "hotel": {
            "nombre": "Hotel Obelisco",
            "direccion": "Av. Corrientes 800, Buenos Aires",
            "estrellas": 3,
            "habitacion": "doble",
            "alojamiento": "hotel"
        },
        "precio_total": 950
    },
     {
        "_id": ObjectId(),
        "nombre": "Tour por el Amazonas",
        "descripcion": "Recorre la selva del Amazonas en una experiencia única de ecoturismo.",
        "precio": 1600,
        "ciudad": "Manaos",
        "fechas": [datetime(2024, 12, 15), datetime(2025, 2, 28)],
        "noches": 5,
        "vuelo": {
            "nro_vuelo": "G3A123",
            "ciudad_origen": "São Paulo",
            "ciudad_destino": "Manaos",
            "fecha_salida": datetime(2024, 12, 15, 10, 0),
            "fecha_llegada": datetime(2024, 12, 15, 13, 0),
            "duracion": "3h",
            "aerolinea": "Gol Airlines"
        },
        "hotel": {
            "nombre": "Amazon Jungle Hotel",
            "direccion": "Av. Amazonas, Manaos",
            "estrellas": 4,
            "habitacion": "simple",
            "alojamiento": "cabaña"
        },
        "precio_total": 1800
    },
    {
        "_id": ObjectId(),
        "nombre": "Maravillas de Machu Picchu",
        "descripcion": "Una visita única a Machu Picchu con guía privado.",
        "precio": 1100,
        "ciudad": "Cusco",
        "fechas": [datetime(2024, 12, 10), datetime(2025, 2, 20)],
        "noches": 4,
        "vuelo": {
            "nro_vuelo": "LA302",
            "ciudad_origen": "Lima",
            "ciudad_destino": "Cusco",
            "fecha_salida": datetime(2024, 12, 10, 8, 0),
            "fecha_llegada": datetime(2024, 12, 10, 9, 0),
            "duracion": "1h",
            "aerolinea": "LATAM Airlines"
        },
        "hotel": {
            "nombre": "Hotel Cusco Plaza",
            "direccion": "Calle Saphi 847, Cusco",
            "estrellas": 3,
            "habitacion": "doble",
            "alojamiento": "hotel"
        },
        "precio_total": 1400
    },
    {
        "_id": ObjectId(),
        "nombre": "Aventura en las Islas Galápagos",
        "descripcion": "Paquete de ecoturismo en las Islas Galápagos, con visitas guiadas a las islas más importantes.",
        "precio": 2200,
        "ciudad": "Puerto Ayora",
        "fechas": [datetime(2024, 11, 28), datetime(2025, 1, 5)],
        "noches": 6,
        "vuelo": {
            "nro_vuelo": "TAM202",
            "ciudad_origen": "Quito",
            "ciudad_destino": "Puerto Ayora",
            "fecha_salida": datetime(2024, 11, 28, 10, 0),
            "fecha_llegada": datetime(2024, 11, 28, 12, 30),
            "duracion": "2h 30m",
            "aerolinea": "Avianca"
        },
        "hotel": {
            "nombre": "Galápagos Eco-Lodge",
            "direccion": "Isla Santa Cruz, Galápagos",
            "estrellas": 4,
            "habitacion": "doble",
            "alojamiento": "cabaña"
        },
        "precio_total": 2800
    },
    {
        "_id": ObjectId(),
        "nombre": "Rumbo a las Maldivas",
        "descripcion": "Escápate a las Maldivas, disfruta de sus playas paradisíacas y un resort de lujo.",
        "precio": 3000,
        "ciudad": "Malé",
        "fechas": [datetime(2024, 12, 10), datetime(2025, 1, 5)],
        "noches": 7,
        "vuelo": {
            "nro_vuelo": "QR829",
            "ciudad_origen": "Doha",
            "ciudad_destino": "Malé",
            "fecha_salida": datetime(2024, 12, 10, 12, 0),
            "fecha_llegada": datetime(2024, 12, 10, 18, 30),
            "duracion": "6h 30m",
            "aerolinea": "Qatar Airways"
        },
        "hotel": {
            "nombre": "Anantara Veli Maldives Resort",
            "direccion": "Dhigu Island, Malé",
            "estrellas": 5,
            "habitacion": "doble",
            "alojamiento": "resort"
        },
        "precio_total": 3700
    },
    {
        "_id": ObjectId(),
        "nombre": "Safari en Sudáfrica",
        "descripcion": "Un safari inolvidable en Sudáfrica, explorando la fauna en su hábitat natural.",
        "precio": 2500,
        "ciudad": "Johannesburgo",
        "fechas": [datetime(2024, 12, 20), datetime(2025, 2, 28)],
        "noches": 5,
        "vuelo": {
            "nro_vuelo": "SAA101",
            "ciudad_origen": "Londres",
            "ciudad_destino": "Johannesburgo",
            "fecha_salida": datetime(2024, 12, 20, 19, 0),
            "fecha_llegada": datetime(2024, 12, 21, 8, 30),
            "duracion": "11h 30m",
            "aerolinea": "South African Airways"
        },
        "hotel": {
            "nombre": "Safari Lodge",
            "direccion": "Kruger National Park, Sudáfrica",
            "estrellas": 5,
            "habitacion": "doble",
            "alojamiento": "cabaña"
        },
        "precio_total": 3000
    },
    {
        "_id": ObjectId(),
        "nombre": "Turismo en Tokio",
        "descripcion": "Un paquete turístico para disfrutar de Tokio y su cultura única.",
        "precio": 1800,
        "ciudad": "Tokio",
        "fechas": [datetime(2024, 12, 10), datetime(2025, 1, 15)],
        "noches": 6,
        "vuelo": {
            "nro_vuelo": "NH801",
            "ciudad_origen": "Los Angeles",
            "ciudad_destino": "Tokio",
            "fecha_salida": datetime(2024, 12, 10, 14, 0),
            "fecha_llegada": datetime(2024, 12, 11, 18, 30),
            "duracion": "12h 30m",
            "aerolinea": "All Nippon Airways"
        },
        "hotel": {
            "nombre": "Park Hotel Tokyo",
            "direccion": "Shiodome, Tokio",
            "estrellas": 5,
            "habitacion": "doble",
            "alojamiento": "hotel"
        },
        "precio_total": 2100
    },
    {
        "_id": ObjectId(),
        "nombre": "Cultura en Marrakech",
        "descripcion": "Conoce la cultura y arquitectura de Marrakech en un viaje inolvidable.",
        "precio": 1300,
        "ciudad": "Marrakech",
        "fechas": [datetime(2024, 12, 15), datetime(2025, 1, 30)],
        "noches": 4,
        "vuelo": {
            "nro_vuelo": "AT601",
            "ciudad_origen": "Madrid",
            "ciudad_destino": "Marrakech",
            "fecha_salida": datetime(2024, 12, 15, 9, 0),
            "fecha_llegada": datetime(2024, 12, 15, 10, 30),
            "duracion": "1h 30m",
            "aerolinea": "Royal Air Maroc"
        },
        "hotel": {
            "nombre": "Riad Dar Anika",
            "direccion": "Marrakech Medina, Marruecos",
            "estrellas": 4,
            "habitacion": "doble",
            "alojamiento": "riad"
        },
        "precio_total": 1500
    },
    {
        "_id": ObjectId(),
        "nombre": "Relájate en Bali",
        "descripcion": "Disfruta del paraíso tropical de Bali, con playas, templos y una cultura única.",
        "precio": 1700,
        "ciudad": "Denpasar",
        "fechas": [datetime(2024, 12, 10), datetime(2025, 1, 10)],
        "noches": 6,
        "vuelo": {
            "nro_vuelo": "GA881",
            "ciudad_origen": "Singapur",
            "ciudad_destino": "Denpasar",
            "fecha_salida": datetime(2024, 12, 10, 11, 30),
            "fecha_llegada": datetime(2024, 12, 10, 14, 30),
            "duracion": "2h",
            "aerolinea": "Garuda Indonesia"
        },
        "hotel": {
            "nombre": "The Mulia Bali",
            "direccion": "Nusa Dua, Bali",
            "estrellas": 5,
            "habitacion": "doble",
            "alojamiento": "resort"
        },
        "precio_total": 2000
    },
    {
        "_id": ObjectId(),
        "nombre": "Escapada a París",
        "descripcion": "Disfruta de los encantos de París, desde la Torre Eiffel hasta los museos más famosos.",
        "precio": 2200,
        "ciudad": "París",
        "fechas": [datetime(2024, 12, 1), datetime(2025, 1, 15)],
        "noches": 5,
        "vuelo": {
            "nro_vuelo": "AF115",
            "ciudad_origen": "Buenos Aires",
            "ciudad_destino": "París",
            "fecha_salida": datetime(2024, 12, 1, 22, 0),
            "fecha_llegada": datetime(2024, 12, 2, 15, 30),
            "duracion": "13h 30m",
            "aerolinea": "Air France"
        },
        "hotel": {
            "nombre": "Le Meurice",
            "direccion": "228 Rue de Rivoli, París",
            "estrellas": 5,
            "habitacion": "doble",
            "alojamiento": "hotel"
        },
        "precio_total": 2600
    }
]
#db.paquetes.insert_many(paquetes)

def insertar_cliente(data):
    db.clientes.insert_one(data)
def insertar_hotel(data):
    db.hotel.insert_one(data)
def insertar_reserva(data):
    db.reserva.insert_one(data)

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
#def view_all_documents():
    db = connect_mongodb()
    collections = db.list_collection_names()  # Obtiene todas las colecciones en la base de datos

    for collection in collections:
        print(f"\nDocumentos en la colección '{collection}':")
        documents = db[collection].find()  # Obtiene todos los documentos de la colección
        for doc in documents:
            print(doc)
#view_all_documents()
#eliminar()


def imprimir_prolijo(data, indent=0):
    """
    Función recursiva para imprimir un diccionario de forma prolija, incluyendo los elementos anidados.
    """
    for clave, valor in data.items():
        if isinstance(valor, dict):
            # Si el valor es un diccionario, llama a la función recursivamente
            print(" " * indent + f"{clave}:")
            imprimir_prolijo(valor, indent + 4)  # Aumenta la indentación para subniveles
        elif isinstance(valor, list):
            # Si el valor es una lista, recorre cada elemento
            print(" " * indent + f"{clave}:")
            for item in valor:
                if isinstance(item, dict):
                    # Si el item de la lista es un diccionario, llama recursivamente
                    imprimir_prolijo(item, indent + 4)
                else:
                    print(" " * (indent + 4) + str(item))  # Imprime el valor de la lista
        else:
            # Si el valor es un tipo simple (como int, str, etc.), lo imprime directamente
            print(" " * indent + f"{clave}: {valor}")

#CONSULTAS
#vuelos
def consultar_vuelos(origen,destino):
    vuelos = list(db.vuelos.find({"ciudad_origen": origen, "ciudad_destino": destino}))
    
    if not vuelos:
        print("No hay vuelos disponibles de", origen, "a", destino)
        return  # Sale si no hay vuelos

    for i, vuelo in enumerate(vuelos, 1):
        # Imprimir el vuelo actual
        print(f"<< {i}. VUELO >>")
        print(f"Nro de vuelo: {vuelo['nro_vuelo']}")
        print(f"Origen: {vuelo['ciudad_origen']}")
        print(f"Destino: {vuelo['ciudad_destino']}")
        print(f"Fecha de salida: {vuelo['fecha_salida'].strftime('%d/%m/%Y %H:%M')}")
        print(f"Fecha de llegada: {vuelo['fecha_llegada'].strftime('%d/%m/%Y %H:%M')}")
        print(f"Duración: {vuelo['duracion']}")
        print(f"Aerolínea: {vuelo['aerolinea']}")
        print(f"Precio: ${vuelo['precio']}")
        print("-" * 40)  # Línea separadora
        
        # Preguntar si desea reservar
        respuesta = input("¿Desea reservar este vuelo? (si/no): ").strip().lower()
        if respuesta == "si":
            print("Procesando la reserva del vuelo...")
            return vuelo  # Salimos de la función y retornamos el vuelo reservado
        
        print("Mostrando el siguiente vuelo...\n")
    
    print("No hay más vuelos disponibles.")
    return None
def consultar_hotel(ciudad):
    hotel = list(db.hotel.find({"direccion.ciudad": ciudad}))
    
    if not hotel:
        print("No hay alojamientos disponibles en", ciudad)
        return 

    for i, hotel in enumerate(hotel, 1):
       
        print(f"<< {i}. ALOJAMIENTO >>")
        print(f"nombre: {hotel['nombre']}")
        print(f"Tipo de alojamiento: {hotel['tipo_alojamiento']}")
        print(f"Direccion: {hotel['direccion']['calle']}, {hotel['direccion']['numero']}, {hotel['direccion']['ciudad']}, {hotel['direccion']['pais']},{hotel['direccion']['zona']} ")
        print(f"Estrellas: {hotel['nEstrellas']}")
        print(f"Precio: ${hotel['precio']}")
        if hotel['disponibilidad']:
            print(f"El hotel {hotel['nombre']} Hay disponibilidad.")
        else:
            print(f"El hotel {hotel['nombre']} No hay disponibilidad.")
        print("-" * 40)  # Línea separadora
        
        # Preguntar si desea reservar
        respuesta = input("¿Desea reservar este alojamiento? (si/no): ").strip().lower()
        if respuesta == "si":
            print("Procesando la reserva del alojamiento...")
            return hotel # Salimos de la función y retornamos el vuelo reservado
        
        print("Mostrando el siguiente alojamiento...\n")
    
    print("No hay más alojamiento disponibles.")
    return None
def consultar_paquete(ciudad):
    paquetes = list(db.paquetes.find({"ciudad": ciudad}))
    
    if not paquetes:
        print("No hay paquetes disponibles en", ciudad)
        return 

    for i, paquetes in enumerate(paquetes, 1):
        print(f"<< {i}. PAQUETE DE ALOJAMIENTO >>")
        print(f"ID: {paquetes['_id']}")
        print(f"Nombre: {paquetes['nombre']}")
        print(f"Descripción: {paquetes['descripcion']}")
        print(f"Precio individual: ${paquetes['precio']}")
        print(f"Ciudad: {paquetes['ciudad']}")
        print("Fechas: ")
        for fecha in paquetes["fechas"]:
            print(f"    - {fecha.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Noches: {paquetes['noches']}")

        print("\nVuelo:")
        vuelo = paquetes["vuelo"]
        print(f"    Número de vuelo: {vuelo['nro_vuelo']}")
        print(f"    Ciudad origen: {vuelo['ciudad_origen']}")
        print(f"    Ciudad destino: {vuelo['ciudad_destino']}")
        print(f"    Fecha salida: {vuelo['fecha_salida'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"    Fecha llegada: {vuelo['fecha_llegada'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"    Duración: {vuelo['duracion']}")
        print(f"    Aerolínea: {vuelo['aerolinea']}")

        print("\nHotel:")
        hotel = paquetes["hotel"]
        print(f"    Nombre: {hotel['nombre']}")
        print(f"    Dirección: {hotel['direccion']}")
        print(f"    Estrellas: {hotel['estrellas']}")
        print(f"    Habitación: {hotel['habitacion']}")
        print(f"    Alojamiento: {hotel['alojamiento']}")

        print(f"\nPrecio Total: ${paquetes['precio_total']}\n")
       
        print("-" * 40)  # Línea separadora
        
        # Preguntar si desea reservar
        respuesta = input("¿Desea reservar este paquete? (si/no): ").strip().lower()
        if respuesta == "si":
            print("Procesando la reserva del paquete...")
            return paquetes 
        
        print("Mostrando el siguiente paquete...\n")
    
    print("No hay más alojamiento disponibles.")
    return None


def consultar_reserva():
    ultima_reserva = db.reserva.find({}, {"_id": 0,"resumen._id": 0,}).sort("_id", -1).limit(1)
    for doc in ultima_reserva:
        print("<< RESUMEN DE TU RESERVA >>")
        imprimir_prolijo(doc)