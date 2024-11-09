import pyodbc

def connect_sql_server():
    connection = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'  # Cambia según tu configuración
        'DATABASE=agencia_viajes;'  # Base de datos SQL Server
        'UID=user_despegar;'  # Cambia 'tu_usuario' por tu usuario
        'PWD=diegopablo;'  # Cambia 'tu_contraseña' por tu contraseña
    )
    return connection

def create_tables_sql_server():
    connection = connect_sql_server()
    cursor = connection.cursor()

    # Crear tabla de paises
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='PAIS' AND xtype='U')
    CREATE TABLE PAIS (
        id_pais int PRIMARY KEY,
        nombre NVARCHAR(20),
        continente NVARCHAR(15),
        codigo_pais NVARCHAR(5)  -- Corregido de 'narchar' a 'NVARCHAR'
    );
    """)
    
    # Crear tabla de ciudades
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='CIUDAD' AND xtype='U')
    CREATE TABLE CIUDAD (
        id_ciudad int  PRIMARY KEY,
        id_pais int,
        nombre NVARCHAR(20),
        codigo_postal NVARCHAR(5),  -- Corregido de 'narchar' a 'NVARCHAR'
        CONSTRAINT FK_Ciudad_Pais FOREIGN KEY (id_pais) REFERENCES PAIS (id_pais)
    );
    """)
    
    # Confirmar la creación de las tablas
    connection.commit()
    cursor.close()
    connection.close()


def insert_data_sql_server():
    connection = connect_sql_server()
    cursor = connection.cursor()
    #cursor.execute("DBCC CHECKIDENT ('PAIS', RESEED, 0);")
    cursor.execute("""
    INSERT INTO PAIS (id_pais, nombre, continente, codigo_pais) 
    VALUES 
        (1,'Argentina', 'América del Sur', 'ARG'),
        (2,'España', 'Europa', 'ESP'),
        (3,'Estados Unidos', 'América Norte', 'USA'),
        (4,'Francia', 'Europa', 'FRA'),
        (5,'Australia', 'Oceanía', 'AUS');
        """)

    

    connection.commit()
    cursor.close()
    connection.close()

def insert_data_sql_server2():
    connection = connect_sql_server()
    cursor = connection.cursor()
    #cursor.execute("DBCC CHECKIDENT ('CIUDAD', RESEED, 0);")
    cursor.execute("""
    INSERT INTO CIUDAD (id_ciudad, id_pais, nombre, codigo_postal) 
    VALUES 
        (1,1, 'Buenos Aires', 'C1000'),
        (2,2, 'Madrid', '28001'),
        (3,3, 'Nueva York', '10001'),
        (4,4, 'París', '75001'),
        (5,5, 'Sídney', '2000');
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
