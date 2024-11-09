# Importar las funciones desde los archivos

import bd_cassandra
import bd_mongo

import bd_sql_server

#def run_cassandra_operations():
#    bd_cassandra.create_tables_cassandra()
#    bd_cassandra.insert_data_cassandra()
#    bd_cassandra.query_data_cassandra()



def run_mongo_operations():
    bd_mongo.login()
    bd_mongo.operaciones()
    bd_mongo.view_all_documents()
    
    

#def run_sql_server_operations():
 #  bd_sql_server.create_tables_sql_server()
 #  bd_sql_server.insert_data_sql_server()
 #  bd_sql_server.query_data_sql_server()

if __name__ == "__main__":
    bd_sql_server.connect_sql_server()
    bd_cassandra.connect_cassandra()
    bd_cassandra.create_tables_cassandra()
    bd_cassandra.insertar_contador_destino("2024-11-01","Colombia")
    bd_cassandra.insertar_contador_destino("2024-11-02","Colombia")
    bd_cassandra.insertar_contador_destino("2024-11-02","Brasil")
    bd_cassandra.insertar_contador_destino("2024-11-08","Brasil")
    #bd_sql_server.create_tables_sql_server() --> si es la primera vez q te conectas a server sacale el comment
    #bd_sql_server.insert_data_sql_server()
    #bd_sql_server.insert_data_sql_server2()
    """while True:
        print("Comencemos... Elige tu caso de uso")
        print("1.login\n2. Agregar alojamiento \n3. Hacer una reserva\n4. Ver casos de uso\n5. Deseo terminar")
        opcion = input("Selecciona: ")
        if opcion == "1":
            bd_mongo.login()
        elif opcion == "2":
            bd_mongo.insertar_hotel()
        elif opcion == "3":
            print()
        elif opcion == "4":
            print()
        else:
            break
        
    aca iria el triple comilla

    #Ejecutar las operaciones de MongoDB
    print("\nOperaciones en MongoDB:")
    run_mongo_operations()
"""
    # Ejecutar las operaciones de SQL Server
    #print("\nOperaciones en SQL Server:")
    #run_sql_server_operations()

     # Ejecutar las operaciones de Cassandra
    #print("Operaciones en Cassandra:")
    #run_cassandra_operations()

#DEPENDE EL CASO DE USO USO UNA HERRAMIENTA U LA OTRA, DEPENDE 

#clientes -- mongo xq no se vuelve a modificar su datos
# ciudad y paises -- cassandra y hoteles tmb
# reservas sql