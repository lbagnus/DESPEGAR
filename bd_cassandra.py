from gevent import monkey
monkey.patch_all()
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from datetime import datetime
from datetime import datetime, timedelta
import datetime
import datetime
from cassandra.util import Date

def connect_cassandra():
    cluster = Cluster(['localhost'])
    session = cluster.connect()


    # Crear Keyspace si no existe
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS agencia_viajes 
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
    """)
    
    session.set_keyspace('agencia_viajes')

    return session

def create_tables_cassandra():
    session = connect_cassandra()

    session.execute("""
    CREATE TABLE IF NOT EXISTS reservas_por_destino (
        fecha date,
        destino text,
        reservas counter,
        PRIMARY KEY (fecha, destino)
    );
""")
    session.execute("""
    CREATE TABLE IF NOT EXISTS alojamientos_solicitados (
    tipo_alojamiento text,
    cantidad counter,
    PRIMARY KEY (tipo_alojamiento)
    ) ;
    """)
    session.execute("""
    CREATE TABLE IF NOT EXISTS ciudades_demandadas (
        pais text,
        ciudad text,
        cantidad counter,
        PRIMARY KEY (pais, ciudad)
    ) WITH CLUSTERING ORDER BY (ciudad ASC);
    """)

def insertar_contador_destino(fecha, destino):
    session = connect_cassandra()
    
    # Incrementa el contador directamente, lo creará si no existe
    session.execute("""
        UPDATE reservas_por_destino
        SET reservas = reservas + 1
        WHERE fecha = %s AND destino = %s
    """, (fecha, destino))

def insertar_alojamientos_solicitados(tipo):
    session = connect_cassandra()
    session.execute("""
    UPDATE alojamientos_solicitados
    SET cantidad = cantidad + 1
    WHERE tipo_alojamiento = %s
    """, (tipo,))
    

def insertar_ciudades_demandadas(pais,ciudad):
    session = connect_cassandra()
    session.execute("""
                UPDATE ciudades_demandadas
                SET cantidad = cantidad + 1
                where pais = %s and ciudad = %s 
                        """,(pais, ciudad))

def query_data_cassandra():
    session = connect_cassandra()
    rows = session.execute("SELECT * FROM reservas")
    for row in rows:
        print(row)


def formato_fecha(cassandra_date):
    if cassandra_date is not None:
        # Si es un objeto 'Date' de Cassandra
        if isinstance(cassandra_date, Date):
            # Convertir a una fecha estándar si aún no lo es
            return str(cassandra_date)  # Convierte directamente a string en formato 'YYYY-MM-DD'
        elif isinstance(cassandra_date, datetime.date):
            # Si ya es un objeto datetime.date de Python, simplemente lo formateamos
            return cassandra_date.strftime("%Y-%m-%d")
        elif isinstance(cassandra_date, str):
            return cassandra_date
    return "Fecha no disponible"


def caso1():
    session = connect_cassandra()
    
    # Ejecutar la consulta y obtener los resultados
    rows = session.execute("""SELECT * FROM reservas_por_destino""")
    
    # Imprimir los resultados de manera más legible
    print(f"{'Fecha':<15}{'Destino':<20}{'Reservas':<10}")
    print("-" * 50)
    for row in rows:
        fecha_formateada = formato_fecha(row.fecha)  # Convertir la fecha a un formato legible
        print(f"{fecha_formateada:<15}{row.destino:<20}{row.reservas:<10}")
    
    # Cerrar la conexión
    session.shutdown()

def caso2():
    session = connect_cassandra()
    rows = session.execute("""SELECT * FROM alojamientos_solicitados""")
    alojamiento = ""
    max = 0

    for row in rows :
        if row.cantidad > max: 
            max = row.cantidad
            alojamiento = row.tipo_alojamiento
            
    print(f"El tipo alojamiento {alojamiento} es el más demandado, con {max} cantidad de reservas")

def caso4():
    session = connect_cassandra()
    rows = session.execute("""SELECT * FROM ciudades_demandadas""")
    ciudades_ordenadas = sorted(rows, key=lambda x: x.cantidad, reverse=True)

    for ciudad in ciudades_ordenadas[:3]:  # Las tres ciudades más demandadas
        print(f"Ciudad: {ciudad.ciudad}, Cantidad: {ciudad.cantidad}")






