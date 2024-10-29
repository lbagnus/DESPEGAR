# Importar las funciones desde los archivos
import bd_cassandra
import bd_mongo
from bson import ObjectId
import bd_sql_server

#def run_cassandra_operations():
#    bd_cassandra.create_tables_cassandra()
#    bd_cassandra.insert_data_cassandra()
#    bd_cassandra.query_data_cassandra()

def login():
    print("Bienvenido a la aplicación.")
    rol = int(input("¿Eres cliente o inquilino? (1 para cliente/ 2 parainquilino): ")).strip().lower()
    
    if rol == 1:  # Suponiendo que rol es un número entero
    # Crear la lista para los números de teléfono
        telefonos = []

        while True:
            telefono = input("Ingresa teléfono: ")
            telefonos.append(telefono)  # Agregar el teléfono a la lista

            # Preguntar si desea agregar otro número
            continuar = input("¿Deseas agregar otro teléfono? (sí/no): ").strip().lower()
            if continuar != 'sí':
                break

        data = {
        "_id": ObjectId(),  # Generar un nuevo ObjectId
        "nombre": input("Ingresa tu nombre y apellido: "),
        "direccion": {
            "calle": input("Ingresa tu calle: "),
            "numero": input("Ingresa el número: "),
            "ciudad": input("Ingresa la ciudad: "),
            "pais": input("Ingresa tu país: ")
        },
        "telefono": telefonos,  # Asignar la lista de teléfonos
        "email": input("Ingresa tu email: ")
        }
        bd_mongo.insertar_cliente(data)

        print("Comencemos hacer tu reserva!")

        servicio = input("Queres reservar un vuelo, un hotel o un paquete?:")
        if (servicio == "Vuelo" or "vuelo" or "VUELO"):
            print("Los vuelos disponibles son:"+ bd_mongo.consultar_vuelos)
            realizar_reserva



def insert_inquilino(data):
    # Aquí va tu lógica para insertar en MongoDB la información del inquilino
    bd_mongo.insert_inquilino(data)  # Suponiendo que tienes esta función en tu archivo bd_mongo.py
    print("Inquilino insertado correctamente.")

def run_mongo_operations():
    rol, user_data = login()
    
    if user_data is None:
        return  # Si el rol es inválido, salimos

    if rol == "cliente":
        insert_cliente(user_data)
    elif rol == "inquilino":
        insert_inquilino(user_data)


def run_mongo_operations():
    bd_mongo.insert_data_mongodb()
    

#def run_sql_server_operations():
 #  bd_sql_server.create_tables_sql_server()
 #  bd_sql_server.insert_data_sql_server()
 #  bd_sql_server.query_data_sql_server()

if __name__ == "__main__":
    # Ejecutar las operaciones de Cassandra
    #print("Operaciones en Cassandra:")
    #run_cassandra_operations()

    #Ejecutar las operaciones de MongoDB
    print("\nOperaciones en MongoDB:")
    run_mongo_operations()

    # Ejecutar las operaciones de SQL Server
    #print("\nOperaciones en SQL Server:")
    #run_sql_server_operations()
