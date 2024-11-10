# Importar las funciones desde los archivos
import itertools
import bd_cassandra
import bd_mongo
import sys
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
    #bd_cassandra.create_tables_cassandra()
    #bd_cassandra.insertar_contador_destino("2024-11-01","Colombia")
    #bd_cassandra.insertar_contador_destino("2024-11-02","Colombia")
    #bd_cassandra.insertar_contador_destino("2024-11-02","Brasil")
    #bd_cassandra.insertar_contador_destino("2024-11-08","Brasil")
    #bd_sql_server.create_tables_sql_server() #--> si es la primera vez q te conectas a server sacale el comment
    #bd_sql_server.insert_data_sql_server()
    #bd_sql_server.insert_data_sql_server2()
    #bd_sql_server.insert_pago(500.40,"tarjeta de debito", "12")
    #bd_sql_server.insert_pago(500.40,"tarjeta de debito", "12425")
    while True:
        print("Comencemos... Elige tu caso de uso")
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
                print ("--- VUELOS ---\n")
                origen = input("Origen: ")
                destino = input ("Destino: ")
                vuelos_reserva = bd_mongo.consultar_vuelos(origen,destino)
                reserva = bd_mongo.data_reserva(vuelos_reserva) #FALTA AGREGAR AL CLIENTE EN ESTOOOO EL ID, XQ ESTA MAL EL FLUJO DEL USUARIO
            elif a == 2:
                print ("--- ALOJAMIENTOS ---\n")
                ciudad = input ("En que ciudad se quiere alojar? ")
                hoteles_reserva= bd_mongo.consultar_hotel(ciudad)
                reserva = bd_mongo.data_reserva(hoteles_reserva)
                

            elif a == 3:
                print ("--- PAQUETES TURISTICOS ---\n")
                ciudad = input ("En que ciudad quiere el paquete? ")
                paquete_reserva = bd_mongo.consultar_paquete(ciudad)
                reserva = (bd_mongo.data_reserva(paquete_reserva))
            resumen_reserva = bd_mongo.consultar_reserva()
            pago = input("Quiere confirmar su reserva? (si/no)")
        elif opcion == "4":
            print("Que caso de uso queres ver? \n 1.¿Cuántas reservas se realizan diariamente en diferentes destinos?\n2.¿Qué tipos de alojamiento son más solicitados por los usuarios?\n3.¿Cuántas propiedades han sido agregadas recientemente en la plataforma?\n4.¿Cuáles son las ciudades más demandadas para alquileres en un país?\n5.¿Cuántas reservas han sido realizadas en destinos tropicales Y han recibido más de 4 estrellas?\n6.¿Qué tipos de alojamiento tienen precios por noche menores a $100 O están ubicados en zonas céntricas\n")
            a = int(input("Selecciona: "))
            if a==1:
                bd_cassandra.caso1()
        else:
            sys.exit()
        
    #aca iria el triple comilla
"""
    #Ejecutar las operaciones de MongoDB
    print("\nOperaciones en MongoDB:")
    run_mongo_operations()

    # Ejecutar las operaciones de SQL Server
    #print("\nOperaciones en SQL Server:")
    #run_sql_server_operations()

     # Ejecutar las operaciones de Cassandra
    #print("Operaciones en Cassandra:")
    #run_cassandra_operations()

#DEPENDE EL CASO DE USO USO UNA HERRAMIENTA U LA OTRA, DEPENDE 

#clientes -- mongo xq no se vuelve a modificar su datos
# ciudad y paises -- cassandra y hoteles tmb
# reservas sql """