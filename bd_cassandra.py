from gevent import monkey
monkey.patch_all()
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

def connect_cassandra():
    print("llegue")
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
                where tipo = %s 
                        """, (tipo))
    

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
