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
    print("Bienvenido a despegar.")
    
    telefonos = []
#hacer reserva o crear hotel
    while True:
        telefono = input("Ingresa teléfono: ")
        telefonos.append(telefono)  # Agregar el teléfono a la lista
        continuar = input("¿Deseas agregar otro teléfono? (sí/no): ").strip().lower()
        if continuar != 'si':
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
    "telefono": telefonos,  
    "email": input("Ingresa tu email: ")
    }
    bd_mongo.insertar_cliente(data)

        





def run_mongo_operations():
    login()
    bd_mongo.view_all_documents
    
    

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


#DEPENDE EL CASO DE USO USO UNA HERRAMIENTA U LA OTRA, DEPENDE 

#clientes -- mongo xq no se vuelve a modificar su datos
# ciudad y paises -- cassandra y hoteles tmb
# reservas sql