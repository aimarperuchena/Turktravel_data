import pyodbc 
import numpy as np
from decimal import Decimal
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
    
    importe =data['importe'].item()
    
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    val=[np.int16(data['aforo']).item(),data['destino'],data['cliente_id'],data['responsable_id'],data['comercial_id'],data['pais_id'],importe,data['fecha']]
    sql="INSERT INTO viaje (aforo, destino,cliente_id,responsable_id, comercial_id,pais_id,importe,fecha) VALUES (?,?,?,?,?,?,?,?) "
    cursor.execute(sql,val)    
    cursor.execute("SELECT @@IDENTITY AS ID;")
    print('Id of inserted record is:{}'.format(cursor.fetchone()[0]))
    
    conn.commit()
    
    conn.close()  
  

def selectViajeInsertado():
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    cursor.execute("SELECT max(id) FROM Viaje") 
    rows = cursor.fetchone() 
    conn.close()
    return rows  

def insertGuiaActividad(actividad_id, guia_id,fecha_actividad, viaje_id):
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    val=[actividad_id, guia_id, viaje_id,fecha_actividad]
    sql="INSERT INTO viaje_actividad (actividad_id, guia_id, viaje_id, fecha) VALUES (?,?,?,?) "
    cursor.execute(sql,val)    
    conn.commit()
    conn.close()  

def insertarViajeros(viaje_id, viajero_id):
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    val=[viajero_id, viaje_id]
    sql="INSERT INTO viaje_viajero (viajero_id, viaje_id) VALUES (?,?) "
    cursor.execute(sql,val)    
    conn.commit()
    conn.close()  