import pyodbc

def connect_sql_server():
    connection = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'  # Cambia según tu configuración
        'DATABASE=agencia_viajes;'  # Base de datos SQL Server
        'UID=tu_usuario;'  # Cambia 'tu_usuario' por tu usuario
        'PWD=tu_contraseña;'  # Cambia 'tu_contraseña' por tu contraseña
    )
    return connection

def create_tables_sql_server():
    connection = connect_sql_server()
    cursor = connection.cursor()

    # Crear tabla de clientes
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='clientes' AND xtype='U')
    CREATE TABLE clientes (
        id_cliente INT IDENTITY PRIMARY KEY,
        nombre NVARCHAR(100),
        direccion NVARCHAR(255),
        telefono NVARCHAR(15),
        email NVARCHAR(100)
    );
    """)

    # Crear tabla de reservas
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='reservas' AND xtype='U')
    CREATE TABLE reservas (
        id_reserva INT IDENTITY PRIMARY KEY,
        id_cliente INT,
        fecha_reserva DATE,
        estado NVARCHAR(50),
        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
    );
    """)

    connection.commit()
    cursor.close()
    connection.close()

def insert_data_sql_server():
    connection = connect_sql_server()
    cursor = connection.cursor()

    # Insertar datos en clientes
    cursor.execute("""
    INSERT INTO clientes (nombre, direccion, telefono, email)
    VALUES ('Juan Pérez', 'Calle Falsa 123', '12345678', 'juan@example.com');
    """)

    # Insertar datos en reservas
    cursor.execute("""
    INSERT INTO reservas (id_cliente, fecha_reserva, estado)
    VALUES (1, '2024-10-23', 'confirmada');
    """)

    connection.commit()
    cursor.close()
    connection.close()

def query_data_sql_server():
    connection = connect_sql_server()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM reservas")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
