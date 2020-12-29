import pyodbc 
databaseName = 'Turktravel'
username = 'sa'
password = 'Laboratorio01,'
server = 'WINDOWSSERVER1'
driver= '{SQL Server}'
CONNECTION_STRING = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+databaseName+';UID='+username+';PWD='+ password




def getClientes():
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cliente") 
    rows = cursor.fetchall() 
    conn.close()
    return rows

def getComerciales():
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Comercial") 
    rows = cursor.fetchall() 
    conn.close()
    return rows

def getGuias():
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Guia") 
    rows = cursor.fetchall() 
    conn.close()
    return rows

def getResponsables():
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Responsable") 
    rows = cursor.fetchall() 
    conn.close()
    return rows

def getViajero():
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Viajero") 
    rows = cursor.fetchall() 
    conn.close()
    return rows

def getPaises():
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pais") 
    rows = cursor.fetchall() 
    conn.close()
    return rows

def getActividades():
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Actividades") 
    rows = cursor.fetchall() 
    conn.close()
    return rows

def insertViaje(data):
    row_id = ''
    conn = pyodbc.connect(CONNECTION_STRING)
    try:
        with conn.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `viaje` (`aforo`, `destino`,`) VALUES ( %s,%s)"
            cursor.execute(sql, (data, sport_id))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            conn.commit()
            row_id = cursor.lastrowid
    except Exception as e:
        print('INSERT TEAM')
        print(e)
        


    finally:

        return row_id