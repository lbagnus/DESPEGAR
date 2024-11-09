# Importar las funciones desde los archivos
import itertools
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
    bd_cassandra.connect_cassandra()
    while True:
        print("<< BIENVENIDOS A DESPEGAR >>\n")
        print("Comencemos... Elige tu caso de uso\n")
        print("1. Login\n2. Agregar alojamiento \n3. Hacer una reserva\n4. Ver casos de uso\n5. Deseo terminar")
        opcion = input("Selecciona: ")
        if opcion == "1":
            bd_mongo.login()
        elif opcion == "2":
            bd_mongo.data_hotel()
        elif opcion == "3":
            print("Que queres reservar? \n 1. Vuelos \n 2. Alojamiento \n 3. Paquete Turistico \n")
            a = int(input("Selecciona: "))
            if a == 1:
                origen = input("Origen: ")
                destino = input ("Destino: ")
                vuelos_reserva = bd_mongo.consultar_vuelos(origen,destino)
                reserva = bd_mongo.data_reserva(vuelos_reserva) #FALTA AGREGAR AL CLIENTE EN ESTOOOO EL ID, XQ ESTA MAL EL FLUJO DEL USUARIO
            elif a == 2:
                ciudad = input ("En que ciudad se quiere alojar? ")
                hoteles_reserva= bd_mongo.consultar_hotel(ciudad)
                reserva = bd_mongo.data_reserva(hoteles_reserva)
                
            resumen_reserva = bd_mongo.consultar_reserva()
            pago = input("Quiere confirmar su reserva? (si/no)")
        elif opcion == "4":
            print()
        else:
            break
        
    

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