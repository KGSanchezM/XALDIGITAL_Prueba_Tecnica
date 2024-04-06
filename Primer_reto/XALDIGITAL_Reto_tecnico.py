import pandas as pd
import requests
import datetime

def obtener_respuestas():
    # URL de la API
    url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
    response = requests.get(url)

    # Convertimos los datos recibidos en un DataFrame
    data = response.json()
    respuestas = pd.DataFrame(data)
    respuestas.head()
    respuestas = pd.json_normalize(respuestas['items'])
    respuestas.head()
    return respuestas

def cantidad_respuestas_constestadas(respuestas):
    respuestas_contestadas = respuestas['is_answered'].value_counts()[0]
    respuestas_no_contestadas = respuestas['is_answered'].value_counts()[1]
    return int(respuestas_contestadas), int(respuestas_no_contestadas)

def respuesta_menor_cantidad_vista(respuestas):
    menor_vistas = respuestas['view_count'].min()
    respuesta_menor_vistas = respuestas[respuestas['view_count']==menor_vistas]
    return respuesta_menor_vistas

def respuesta_mas_vieja_actual(respuestas):
    fecha_mas_vieja = respuestas['creation_date'].min()
    fecha_mas_actual = respuestas['creation_date'].max()

    fecha_mas_vieja_legible = datetime.datetime.fromtimestamp(fecha_mas_vieja).strftime('%Y-%m-%d')
    fecha_mas_actual_legible = datetime.datetime.fromtimestamp(fecha_mas_actual).strftime('%Y-%m-%d')

    respuesta_mas_vieja = respuestas[respuestas['creation_date']==fecha_mas_vieja]
    respuesta_mas_actual = respuestas[respuestas['creation_date']==fecha_mas_actual]

    return fecha_mas_vieja_legible, respuesta_mas_vieja, fecha_mas_actual_legible, respuesta_mas_actual

def respuesta_owner_mejor_reputacion(respuestas):
    owner_mayor_reputacion = respuestas['owner.reputation'].max()
    respuesta_owner_mayor_reputacion = respuestas[respuestas['owner.reputation']==owner_mayor_reputacion]
    return respuesta_owner_mayor_reputacion

def imprimir_resultados(respuestas_contestadas, respuestas_no_contestadas, respuesta_menor_vistas, fecha_mas_vieja_legible, respuesta_mas_vieja, fecha_mas_actual_legible, respuesta_mas_actual, respuesta_owner_mayor_reputacion):
    # Respuestas del punto 2
    print(f'Respuestas del punto 2\n')
    print(f'El número de respuestas contestadas es {respuestas_contestadas}')
    print(f'El número de respuestas no contestadas es {respuestas_no_contestadas}\n')

    # Respuesta del punto 3
    print('Respuesta del punto 3\n')
    print('La respuesta con menor número de vistas es:\n')
    print(f'{respuesta_menor_vistas["title"]}\n')

    # Respuestas del punto 4
    print('Respuestas del punto 4\n')
    print(f'La respuesta más vieja se hizo el {fecha_mas_vieja_legible} y es:\n')
    print(f'{respuesta_mas_vieja["title"]}\n')
    print(f'La respuesta más actual se hizo el {fecha_mas_actual_legible} y es:\n')
    print(f'{respuesta_mas_actual["title"]}\n')

    # Respuesta del punto 5
    print('Respuesta del punto 5\n')
    print('La respuesta del owner con la mayor reputación es:\n')
    print(f'{respuesta_owner_mayor_reputacion["title"]}\n')

# Ejecutar las funciones
respuestas = obtener_respuestas()
respuestas_contestadas, respuestas_no_contestadas = cantidad_respuestas_constestadas(respuestas)
respuesta_menor_vistas = respuesta_menor_cantidad_vista(respuestas)
fecha_mas_vieja_legible, respuesta_mas_vieja, fecha_mas_actual_legible, respuesta_mas_actual = respuesta_mas_vieja_actual(respuestas)
respuesta_owner_mayor_reputacion = respuesta_owner_mejor_reputacion(respuestas)

# Imprimir los resultados
imprimir_resultados(respuestas_contestadas, respuestas_no_contestadas, respuesta_menor_vistas, fecha_mas_vieja_legible, respuesta_mas_vieja, fecha_mas_actual_legible, respuesta_mas_actual, respuesta_owner_mayor_reputacion)

