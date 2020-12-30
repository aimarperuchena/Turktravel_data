from db import getComerciales,getClientes,getGuias,getResponsables,getViajero,getPaises,getActividades,insertViaje,selectViajeInsertado
from db import insertGuiaActividad,insertarViajeros
from random import randrange, choice
import pandas as pd 

from datetime import datetime
def main():
    clientes=getClientes()
    comerciales=getComerciales()
    guias=getGuias()
    responsables=getResponsables()
    viajeros=getViajero()
    paises=getPaises()
    actividades=getActividades()
    df_viajes = pd.read_csv('viaje_data.csv','*')
    df = pd.DataFrame(df_viajes, columns = ['Aforo', 'Destino', 'Importe', 'Fecha']) 
    for ind in df.index: 
        cliente=choice(clientes)
        cliente_id=cliente[0]

        #SELECCIONAR COMERCIAL
        comercial=choice(comerciales)
        comercial_id=comercial[0]

        #SELECCIONAR RESPONSABLE
        responsable=choice(responsables)
        responsable_id=responsable[0]

        #SELECCIONAR PAIS
        pais=choice(paises)
        pais_id=pais[0]

        
        
        
        
        
        

        viaje_insert_data={
            'cliente_id':cliente_id,
            'responsable_id':responsable_id,
            'comercial_id':comercial_id,
            'pais_id':pais_id,
            'aforo':df['Aforo'][ind],
            'destino':df['Destino'][ind],
            'importe':df['Importe'][ind],
            'fecha':df['Fecha'][ind]}
        insertViaje(viaje_insert_data)
        viaje_id=selectViajeInsertado()
        viaje_id=viaje_id[0]

        #INSERTAR VIAJES A REALIZAR
        numero_actividades=randrange(1,12)
        for actividades_x in range(numero_actividades):
            actividad=choice(actividades)
            actividad_id=actividad[0]
            guia=choice(guias)
            guia_id=guia[0]
            next_date=pd.to_datetime(df['Fecha'][ind]) + pd.DateOffset(days=actividades_x)
            fecha_actividad=next_date.strftime("%d/%m/%Y")
            insertGuiaActividad(actividad_id,guia_id, fecha_actividad,viaje_id)



        #SELECCIONAR VIAJEROS ALEATORIOS
        
        
        for viajeros_x in range(df['Aforo'][ind]):
            viajero=choice(viajeros)
            viajero_id=viajero[0]
            insertarViajeros(viaje_id, viajero_id)
        print('VIAJE: '+str(df['Destino'][ind]))
    print('TERMINADO')        

        
        

        
       
        
        





        






    







main()