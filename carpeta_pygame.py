import pygame
import json
imagen_pantalla = pygame.image.load("EXAMENES/imagen.png") # 512x512
imagen_pantalla_2 = pygame.image.load('EXAMENES\imagen2.jpg')
imagen_pantalla_3 = pygame.image.load ('EXAMENES\image.png')
imagen_pantalla_4 = pygame.image.load ('EXAMENES\champions.jpg')
# Lista de preguntas
lista = [
    {"pregunta": "¿Cuál es la moneda de México?", "a": "Peso", "b": "Dólar", "c": "Euro", "correcta": "a"},
    {"pregunta": "¿De qué color es la bandera de Japón?", "a": "Azul y Amarilla", "b": "Blanca y Roja", "c": "Celeste y Blanca", "correcta": "b"},
    {"pregunta": "¿Aguante el Valorant?", "a": "Sí", "b": "No", "c": "Nerfeen a Iso", "correcta": "c"},
    {"pregunta": "¿Quién pintó Las Meninas?", "a": "Francisco de Goya", "b": "Diego Velázquez", "c": "Salvador Dalí", "correcta": "b"}
]


def guardar_mejores()-> list:
    '''escribimos la tabla de mejores en un .json'''
    with open ('EXAMENES\juegos.json', 'r') as w:
        datos = json.load(w)
    return datos
score = guardar_mejores()
print(score)


def bubble_sort_puntaje(score):
    '''por el metodo de bubble sort conseguimos el mejor puntaje de la tabla'''
    for i in range(len(score)-1):
        for j in range(i+1, len(score)):
            if score[i]['puntaje'] < score[j]['puntaje']:
                aux = score[i]
                score[i] = score[j]
                score[j] = aux

def llevar_a_json(lista:list):
    '''transferimos los datos del json'''
    with open(f"EXAMENES\puntuaciones.json", "w") as archivo:
        json.dump(lista, archivo, indent= 4,ensure_ascii= False)