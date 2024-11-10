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


def reserva():
    print ("-- RESERVAS --\n")
    print("1. Vuelos\n2. Alojamientos\n3. Paquetes Turisticos\n")
    a = int(input("Que desea reservar? "))
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
        reserva = bd_mongo.data_reserva(paquete_reserva)
    else:
        print("--ERROR--")


def pago():
    id = bd_mongo.consultar_id
    monto = bd_mongo.consultar_monto
    print(f"N° de reserva: {id}\nMonto a pagar: {monto}\n")
    print("Seleccione el metodo de pago: \n")
    print("1. Tarjeta de credito\n2. Tarjeta de debito\n 3. Mercado Pago")
    mp = int(input("Seleccioná: "))
    if mp == 1:
        metodo = "Tarjeta de credito"
    elif mp == 2:
        metodo = "Tarjeta de debito"
    elif mp == 3: 
        metodo = "Mercado Pago"
    else:
        print("--ERROR--")
    bd_sql_server.insert_pago(monto,metodo, id) 


#def run_sql_server_operations():
 #  bd_sql_server.create_tables_sql_server()
 #  bd_sql_server.insert_data_sql_server()
 #  bd_sql_server.query_data_sql_server()

if __name__ == "__main__":
   # bd_sql_server.connect_sql_server()
    #bd_cassandra.connect_cassandra()
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
        print("<< BIENVENIDOS A DESPEGAR >> \n")
        print("-" * 40) 
        print("1. Login\n2. Ver casos de uso\n3. Deseo terminar\n")
        opcion = int(input("Seleccioná: "))
        if opcion == 1:
            bd_mongo.login()
            print("-" * 40) 
            print("1. Reservar\n2. Agregar Alojamiento\n")
            menu = int(input("Seleccioná: "))
            if menu == 1:
                reserva()
            elif opcion == 2:
                bd_mongo.data_hotel()
            else:
                print("---SELECCIONA 1 o 2 ---\n")
                break
            bd_mongo.consultar_reserva()
            pago = input("Quiere pagar su reserva? (si/no): ") 
            if pago == 'si':
                pago()
            else:
                print("-- RESERVA CANCELADA --")
                sys.exit()
        elif opcion == 2:
            print("Que caso de uso queres ver? \n 1.¿Cuántas reservas se realizan diariamente en diferentes destinos?\n2.¿Qué tipos de alojamiento son más solicitados por los usuarios?\n3.¿Cuántas propiedades han sido agregadas recientemente en la plataforma?\n4.¿Cuáles son las ciudades más demandadas para alquileres en un país?\n5.¿Cuántas reservas han sido realizadas en destinos tropicales Y han recibido más de 4 estrellas?\n6.¿Qué tipos de alojamiento tienen precios por noche menores a $100 O están ubicados en zonas céntricas\n")
            a = int(input("Selecciona: "))
            if a==1:
                bd_cassandra.caso1()
        else:
            print("-- CIERRE DE SESION --")
            sys.exit()
        
    #aca iria el triple comilla
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
# reservas sql """