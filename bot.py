from db import getComerciales,getClientes,getGuias,getResponsables,getViajero,getPaises,getActividades,insertViaje
from random import randrange, choice
import pandas as pd 

def main():
    clientes=getClientes()
    comerciales=getComerciales()
    guias=getGuias()
    responsables=getResponsables()
    viajeros=getViajero()
    paises=getPaises()
    actividades=getActividades()
    viajes_default=''
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

        numero_viajeros=randrange(2,12)
        
        viaje_viajeros=[]
        for viajeros_x in range(numero_viajeros):
            viajero=choice(viajeros)
            viajero_id=viajero[0]
            viaje_viajeros.append(viajero_id)
        
        viaje_insert_data={
            'cliente_id':cliente_id,
            'reponsable_id':responsable_id,
            'comercial_id':comercial_id,
            'pais':pais_id,
            'aforo':df['Aforo'][ind],
            'destino':df['Destino'][ind],
            'importe':df['Importe'][ind],
            'fecha':df['Fecha'][ind]}
        insertViaje(viaje_insert_data)





        






    







main()