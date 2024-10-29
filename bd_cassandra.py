from gevent import monkey
monkey.patch_all()
from cassandra.cluster import Cluster

def connect_cassandra():
    cluster = Cluster(['127.0.0.1']) #ip de docker
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

    # Crear tabla de clientes
    session.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente UUID PRIMARY KEY,
        nombre text,
        direccion text,
        telefono text,
        email text
    );
    """)

    # Crear tabla de reservas
    session.execute("""
    CREATE TABLE IF NOT EXISTS reservas (
        id_reserva UUID PRIMARY KEY,
        id_cliente UUID,
        fecha_reserva date,
        estado text
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
