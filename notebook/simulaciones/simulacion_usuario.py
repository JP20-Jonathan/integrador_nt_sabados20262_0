import random 
import uuid
import pandas as pd
from faker import Faker


#1. Sembrar semillas para los datos a simular
random.seed(42)
Faker.seed(42)

#2. IdentiFicar los datos a simular con su tipo de dato
#id (texto (UUID)), 
#nombre (texto), 
#correo (texto), 
#contrasena_hash (texto), 
#rol (texto), *****************
#activo (booleano), 
#fecha_registro (fecha y hora).

#3. ESTABLECER UNA CONSTANTE PARA EL NUEMROD E SIMULACIONS
FILAS=400
ROLES=["administrador","empresario","estudiante","profesor"]
FALSITO=Faker("es_CO")

#4. Funcion generadora
def generar_datos(numero_filas=400):
    usuarios=[]
    for _ in range(numero_filas):
        usuarios.append({
            "id":str(uuid.uuid4()),
            "nombre":FALSITO.name(),
            "correo":FALSITO.email(),
            "contrasena_hash":FALSITO.sha256(),
            "activo":random.choice([True,False]),
            "rol":random.choice(ROLES),
            "fecha_registro":FALSITO.date_time_between(start_date="-2y", end_date="now")

        })
    return usuarios

#5.Conviertindo los datos generados en un dataframe con PANDAS
tabla_ordenada_usuarios=pd.DataFrame(generar_datos())

#6. Probar la funcion
print(tabla_ordenada_usuarios)
    