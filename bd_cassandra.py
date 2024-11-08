from gevent import monkey
monkey.patch_all()
from cassandra.cluster import Cluster

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

    #Crear tabla de reservas general -- esta capaz la pasamos a mongo
    #session.execute("""
    """CREATE TABLE IF NOT EXISTS reservas_general (
        id_reserva UUID PRIMARY KEY,
        id_cliente UUID,
        tipo_servicio text, 
        destino text, 
        fecha_reserva date,
        estado text,
        monto_Total double, 
        nombre_cliente text, 
    );
    """
    #""")

    session.execute("""
    CREATE TABLE IF NOT EXISTS reservas_por_destino (
    fecha date,
    destino text,
    reservas int,
    PRIMARY KEY (fecha, destino)
    );
    """)
    session.execute("""
    CREATE TABLE IF NOT EXISTS alojamientos_solicitados (
    tipo_alojamiento text,
    cantidad int,
    PRIMARY KEY (tipo_alojamiento, cantidad)
    ) with clustering order by (cantidad ASC);
    """)
    session.execute("""
    CREATE TABLE IF NOT EXISTS ciudades_demandadas (
    pais text,
    ciudad text,
    cantidad int
    PRIMARY KEY (pais, ciudad, cantidad)
    with clustering order by (cantidad ASC)
    );
    """)

def insert_data_cassandra():
    session = connect_cassandra()

    # Insertar datos en clientes
    session.execute("""
    INSERT INTO clientes (id_cliente, nombre, direccion, telefono, email)
    VALUES (uuid(), 'Juan Pérez', 'Calle Falsa 123', '12345678', 'juan@example.com');
    """)

    # Insertar datos en reservas
    session.execute("""
    INSERT INTO reservas (id_reserva, id_cliente, fecha_reserva, estado)
    VALUES (uuid(), uuid(), '2024-10-23', 'confirmada');
    """)

def query_data_cassandra():
    session = connect_cassandra()
    rows = session.execute("SELECT * FROM reservas")
    for row in rows:
        print(row)
