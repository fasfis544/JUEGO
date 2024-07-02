import pygame
from carpeta_pygame import *
from preguntas import lista

'''
A. Analizar detenidamente el set de datos (puede agregarle más preguntas si así
lo desea).
B. Crear una pantalla de inicio, con 3 (tres) botones, “Jugar”, “Ver Puntajes”,
“Salir”, la misma deberá tener alguna imagen cubriendo completamente el
fondo y tener un sonido de fondo. Al apretar el botón jugar se iniciará el juego.
Opcional: Agregar un botón para activar/desactivar el sonido de fondo.
C. Crear 2 botones uno con la etiqueta “Pregunta”, otro con la etiqueta “Reiniciar”
D. Imprimir el Puntaje: 000 donde se va a ir acumulando el puntaje de las
respuestas correctas. Cada respuesta correcta suma 10 puntos.
E. Al hacer clic en el botón “Pregunta” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic en este botón pasa a la siguiente
pregunta.
F. Al hacer clic en una de las tres palabras que representa una de las tres
opciones, si es correcta, debe sumar el puntaje, reproducir un sonido de
respuesta correcta y dejar de mostrar las otras opciones.
G. Solo tiene 2 intentos para acertar la respuesta correcta y sumar puntos, si
agotó ambos intentos, deja de mostrar las opciones y no suma puntos. Al
elegir una respuesta incorrecta se reproducirá un sonido indicando el error y
se ocultará esa opción, obligando al usuario a elegir una de las dos restantes.
H. Al hacer clic en el botón “Reiniciar” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el puntaje.
I. Una vez terminado el juego se deberá pedirle el nombre al usuario, guardar
ese nombre con su puntaje en un archivo, y volver a la pantalla de inicio.
J. Al ingresar a la pantalla “Ver Puntajes”, se deberá mostrar los 3 (tres) mejores
puntajes ordenados de mayor a menor, junto con sus nombres de usuario
correspondientes. Debe haber un botón para volver al menú principal.
'''

intentos = 2
puntaje = 0
mejor_puntaje = 0
nombre_usuario = ""
score = guardar_mejores()
lista_preguntas = 0
pregunta_mostrar = lista [lista_preguntas]

pygame.init() #Se inicializa pygame
pygame.display.set_caption("P R E G U N T A D O S")
config_pantalla = [1280, 720]
screen = pygame.display.set_mode(config_pantalla) #Se crea una ventana
imagen_pantalla = pygame.image.load("EXAMENES/imagen.png") # 512x512
imagen_pantalla_2 = pygame.image.load('EXAMENES\imagen2.jpg')
imagen_pantalla_3 = pygame.image.load ('EXAMENES\image.png')
imagen_pantalla_4 = pygame.image.load ('EXAMENES\champions.jpg')

rect_boton_jugar = pygame.Rect(200, 300, 290, 70)
rect_boton_puntaje = pygame.Rect(200, 400, 290, 70)
rect_boton_salir = pygame.Rect(200, 500, 290, 70)
rect_boton_reiniciar = pygame.Rect(20, 30, 290, 70)

rect_boton_preguntados = pygame.Rect(970, 30, 290, 70)
rect_boton_respuesta1 = pygame.Rect(180, 550, 290, 70)
rect_boton_respuesta2 = pygame.Rect(510, 550, 290, 70)
rect_boton_respuesta3 = pygame.Rect(840, 550, 290, 70)
rect_boton_pregunta = pygame.Rect(0, 440, 1280, 70)


rect_boton_puntaje2 = pygame.Rect(970, 130, 290, 70)

rect_boton_ingresar_nombre = pygame.Rect(510, 70, 290, 70)
rect_boton_tupuntaje = pygame.Rect(510, 400, 290, 70)
rect_boton_salirpuntaje = pygame.Rect(970, 30, 290, 70)

font = pygame.font.SysFont("Arial Narrow", 50)
text_start = font.render("Start", True, (5, 13, 252))
text_puntaje = font.render("Puntaje", True, (5, 13, 252))
text_salir = font.render("Salir", True, (5, 13, 252))
text_preguntados = font.render("cambio pregunta", True, (247, 252, 247))
text_reiniciar = font.render("Reiniciar", True, (247, 252, 247))


text_pregunta = font.render(str(lista[lista_preguntas]['pregunta']), True, (247, 252, 247))

text_salirpuntaje = font.render("Menu", True, (247, 252, 247))

text_ingrese_su_name = font.render('Name:', True, (247, 252, 247))

text_respuesta1 = font.render(str(lista[lista_preguntas]['a']), True, (247, 252, 247))
text_respuesta2 = font.render(str(lista[lista_preguntas]['b']), True, (247, 252, 247))
text_respuest3 = font.render(str(lista[lista_preguntas]['c']), True, (247, 252, 247))

respuesta_correcta1 = 'a'
respuesta_correcta2 = 'b'
respuesta_correcta3 = 'c'

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("EXAMENES/to-frighten-121407.mp3")
sonido_fondo.set_volume(0.08)
sonido_incorrecto = pygame.mixer.Sound("EXAMENES\musicaincorrecta.mp3")
sonido_correcto = pygame.mixer.Sound('EXAMENES\musicacorrecta.mp3')
sonido_fondo.play(-1)

esta_jugando = 'inicio'
running = True



while running:
    
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (event.type == pygame.TEXTINPUT):
            tecla_ingresada = event.text
            nombre_usuario += tecla_ingresada
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                datos_jugador = {'nombre':nombre_usuario, 'puntaje':puntaje}
                score ['top_mejores'].append (datos_jugador)
                llevar_a_json(score)
                print (score)
                puntaje = 0
                nombre_usuario = ''
                esta_jugando = 'inicio'

        if event.type == pygame.MOUSEBUTTONDOWN:
            if esta_jugando == 'inicio':
                print(f"Mouse down: {event.pos}")
                if rect_boton_jugar.collidepoint(event.pos):
                    lista_preguntas = 0
                    esta_jugando = 'jugando'
                #print("Apreto start")
            
                if rect_boton_puntaje.collidepoint(event.pos):
                    esta_jugando = 'puntaje'
                    
                if rect_boton_salir.collidepoint(event.pos):
                    running = False

            if esta_jugando == 'puntaje':
                if rect_boton_salirpuntaje.collidepoint(event.pos):
                    mejor_puntaje = nombre_usuario_render
                    puntaje = 0
                    nombre_usuario = ""
                    lista_preguntas = 0
                    esta_jugando = 'inicio'
                
                
            if esta_jugando == 'jugando':
                cambiar_pregunta = False
                if rect_boton_reiniciar.collidepoint(event.pos):
                    puntaje = 0
                    lista_preguntas = -1
                    cambiar_pregunta = True

                if rect_boton_preguntados.collidepoint(event.pos):
                    cambiar_pregunta = True
                        
                if rect_boton_respuesta1.collidepoint(event.pos):
                    if respuesta_correcta1 == pregunta_mostrar['correcta']:
                        sonido_correcto.play()
                        cambiar_pregunta = True
                        puntaje += 10
                    else:
                        sonido_incorrecto.play()
                        intentos -= 1

                if rect_boton_respuesta2.collidepoint(event.pos):
                    if respuesta_correcta2 == pregunta_mostrar ['correcta']:
                        sonido_correcto.play()
                        cambiar_pregunta = True
                        puntaje += 10
                    else:
                        sonido_incorrecto.play()
                        intentos -= 1
                if rect_boton_respuesta3.collidepoint(event.pos):
                    if respuesta_correcta3 == pregunta_mostrar ['correcta']:
                        sonido_correcto.play()
                        cambiar_pregunta = True
                        puntaje += 10
                    else:
                        sonido_incorrecto.play()
                        intentos -= 1
                        
                if intentos == 0:

                    intentos = 2
                    cambiar_pregunta = True

                if cambiar_pregunta == True:
                    if lista_preguntas < len(lista)-1:
                        lista_preguntas += 1
                        pregunta_mostrar = lista [lista_preguntas]
                        text_respuesta1 = font.render(str(lista[lista_preguntas]['a']), True, (247, 252, 247))
                        text_respuesta2 = font.render(str(lista[lista_preguntas]['b']), True, (247, 252, 247))
                        text_respuest3 = font.render(str(lista[lista_preguntas]['c']), True, (247, 252, 247))
                        text_pregunta = font.render(str(lista[lista_preguntas]['pregunta']), True, (247, 252, 247))
                    else:
                        if lista_preguntas == 9:
                            esta_jugando = 'puntaje'
                        print ('termino preguntados')

        if esta_jugando == 'inicio':
                
                screen.blit(imagen_pantalla, (0,0))# Se pinta el fondo de la ventana
                pygame.draw.rect(screen, (245, 255, 107), rect_boton_jugar, border_radius=15)
                pygame.draw.rect(screen, (245, 255, 107), rect_boton_puntaje, border_radius=15)
                pygame.draw.rect(screen, (245, 255, 107), rect_boton_salir, border_radius=15)
                screen.blit(text_start, (300, 320))
                screen.blit(text_puntaje, (290,420))    
                screen.blit(text_salir, (300, 520))
    
        elif esta_jugando == 'jugando':
                text_puntaje2 = font.render(f'PUNTAJE:{str(puntaje)}', True, (247, 252, 247))
                screen.blit(imagen_pantalla_2, (0,0))
                screen.blit (imagen_pantalla_3, (470,50 ))
                pygame.draw.rect(screen, (5, 13, 252), rect_boton_preguntados, border_radius=15)
                pygame.draw.rect(screen, (5, 13, 252), rect_boton_reiniciar, border_radius=15)
                
                pygame.draw.rect(screen, (5, 13, 252), rect_boton_respuesta1, border_radius=15)
                pygame.draw.rect(screen, (5, 13, 252), rect_boton_respuesta2, border_radius=15)
                pygame.draw.rect(screen, (5, 13, 252), rect_boton_respuesta3, border_radius=15)
                pygame.draw.rect(screen, (5, 13, 252), rect_boton_pregunta, border_radius=15)

                pygame.draw.rect(screen, (5, 13, 252), rect_boton_puntaje2, border_radius=15)

                screen.blit(text_preguntados, (975, 50))
                screen.blit(text_reiniciar, (50, 50))
                screen.blit(text_respuesta1, (180, 550))
                screen.blit(text_respuesta2, (510, 550))
                screen.blit(text_respuest3, (840, 550))
                screen.blit(text_pregunta, (400, 455))
                screen.blit(text_puntaje2, (975, 150))

        elif esta_jugando == 'puntaje':
            screen.blit (imagen_pantalla_4, (0,0))
            pygame.draw.rect(screen, (5, 13, 252), rect_boton_respuesta1, border_radius=15)
            pygame.draw.rect(screen, (5, 13, 252), rect_boton_respuesta2, border_radius=15)
            pygame.draw.rect(screen, (5, 13, 252), rect_boton_respuesta3, border_radius=15)
            pygame.draw.rect(screen, (5, 13, 252), rect_boton_tupuntaje, border_radius=15)
            pygame.draw.rect(screen, (5, 13, 252), rect_boton_salirpuntaje, border_radius=15)
            pygame.draw.rect(screen, (5, 13, 252), rect_boton_ingresar_nombre, border_radius=15)
            
            text_puntaje2 = font.render(f'PUNTAJE:{str(puntaje)}', True, (247, 252, 247))
            acumulador_x = 0
            acumulador_puesto = 0
            
            for dato_jugador in score["top_mejores"]:
                bubble_sort_puntaje(score ["top_mejores"])
                acumulador_puesto += 1
                dato_jugador_render = font.render(f"{acumulador_puesto -1 } - {dato_jugador['nombre']}: {dato_jugador['puntaje']}", True, (255, 255, 255))
                if acumulador_puesto <= 4:
                    screen.blit(dato_jugador_render, (200 + acumulador_x, 550 ))
                acumulador_x += 330
                

            screen.blit(text_ingrese_su_name,(580, 38))
            nombre_usuario_render = font.render(nombre_usuario, True, (247, 252, 247))
            
            screen.blit(text_puntaje2, (550, 415))
            screen.blit(text_salirpuntaje,(1065, 50))
            screen.blit(nombre_usuario_render,(570, 80))
            
    pygame.display.flip()# Muestra los cambios en  la pantalla

pygame.quit() # Fin