import pygame
import sys
from consts.constantes import *
from game.menu import crear_elementos_menu, dibujar_menu, manejar_click_menu
from game.inicializacion import inicializar_pygame
from game.recursos import cargar_sonidos, cargar_imagenes, cargar_fuentes
from game.musica import iniciar_musica, iniciar_musica_menu
from game.pantallas import mostrar_ranking, dibujar_game_over_simple, dibujar_juego
from game.estados import *
from puntajes_module import *
from playerdata.enemigos import actualizar_capybaras
from playerdata.nave import movimiento_nave, cargar_recursos_golpe
from playerdata.balas import crear_bala, actualizar_balas
from game.colisiones import detectar_colision_balas_enemigos, detectar_colision_nave_enemigos
from intro import *

def ejecutar_juego():
    """Función principal del juego"""
    # Inicializar
    ventana, clock = inicializar_pygame()
    
    #Cargar recursos
    sonidos = cargar_sonidos()
    imagenes = cargar_imagenes()
    fuentes = cargar_fuentes()

    sonido_disparo = sonidos["disparo"]
    sonido_colision = sonidos["colision"]
    sonido_game_over = sonidos["game_over"]

    nave_img = imagenes["nave"]
    capy_img = imagenes["capybara"]
    fondo_img = imagenes["fondo"]
    menu_fondo_img = imagenes["menu_fondo"]
    intro_img = imagenes["intro"]
    corazon_img = imagenes["corazon"]

    fuente = fuentes["normal"]
    fuente_pequena = fuentes["pequena"]
    fuente_grande = fuentes["grande"]
    fuente_menu = fuentes["menu"]
    fuente_controles = fuentes["controles"]



    ultimo_golpe, es_invulnerable = cargar_recursos_golpe()
    # Crear elementos del menú
    boton_jugar, boton_ranking, boton_salir, texto_boton_jugar, texto_boton_ranking, texto_boton_salir = crear_elementos_menu()
    
    # Estados del juego
    estado_juego = "menu"
    iniciar_musica_menu()
    
    # Estado de intro
    estado_intro = crear_estado_intro()
    recursos_intro = {
        'img_intro': intro_img,
        'fuente_menu': fuente_menu,
        'fuente_controles': fuente_controles
    }
    
    historia = [
        "En el año 2087, los carpinchos han invadido la Tierra...",
        "Solo tú puedes detenerlos con tu nave espacial.",
        "¡Prepárate para la batalla final!"
    ]
    
    # Estado del juego
    estado = crear_estado_inicial()
    
    # Tiempo anterior para delta_time
    tiempo_anterior = pygame.time.get_ticks()
    
    # Loop principal
    jugar = True
    while jugar:
        tiempo_actual = pygame.time.get_ticks()
        delta_time = tiempo_actual - tiempo_anterior
        tiempo_anterior = tiempo_actual
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugar = False
            
            # Manejar eventos de intro
            if estado_juego == "intro":
                estado_intro = manejar_evento_intro(estado_intro, event)
                if debe_cambiar_a_menu(estado_intro):
                    estado_juego = "jugando"
                    estado = crear_estado_inicial()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if estado_juego == "menu":
                    accion = manejar_click_menu(event.pos, boton_jugar, boton_ranking, boton_salir)
                    if accion == "jugar":
                        pygame.mixer.music.stop()
                        iniciar_musica()
                        estado_juego = "intro"
                        estado_intro = crear_estado_intro()
                    elif accion == "ranking":
                        estado_juego = "ranking"
                    elif accion == "salir":
                        jugar = False
            
            if event.type == pygame.KEYDOWN:
                # Disparar
                if event.key == pygame.K_SPACE and estado_juego == "jugando":
                    if tiempo_actual - estado["tiempo_ultimo_disparo"] > 200:
                        bala = crear_bala(estado["nave"].x, estado["nave"].y)
                        estado["balas_lista"].append(bala)
                        sonido_disparo.play()
                        estado["tiempo_ultimo_disparo"] = tiempo_actual
                
                # Game Over - Reiniciar
                elif event.key == pygame.K_r and estado["estado_pantalla"] == "game_over":
                    estado_juego = "jugando"
                    estado = crear_estado_inicial()
                    iniciar_musica()
                
                # Game Over - Ingresar nombre para record
                elif event.key == pygame.K_n and estado["estado_pantalla"] == "game_over" and es_top_puntaje(estado["puntuacion"]):
                    estado["estado_pantalla"] = "entrada_nombre"
                    estado["nombre_jugador"] = ""
                
                # Volver al menú desde game over
                elif event.key == pygame.K_m and estado["estado_pantalla"] == "game_over":
                    estado_juego = "menu"
                    pygame.mixer.music.stop()
                    iniciar_musica_menu()
                
                # Volver al menú desde ranking
                elif event.key == pygame.K_m and estado_juego == "ranking":
                    estado_juego = "menu"
                    pygame.mixer.music.stop()
                    iniciar_musica_menu()
                
                # Entrada de nombre
                elif estado["estado_pantalla"] == "entrada_nombre":
                    if event.key == pygame.K_RETURN:
                        nombre = limpiar_nombre(estado["nombre_jugador"])
                        agregar_puntaje(nombre, estado["puntuacion"])
                        estado["estado_pantalla"] = "puntajes"
                        estado["puntajes_top"] = obtener_top_puntajes()
                    elif event.key == pygame.K_ESCAPE:
                        estado["estado_pantalla"] = "game_over"
                    elif event.key == pygame.K_BACKSPACE:
                        estado["nombre_jugador"] = estado["nombre_jugador"][:-1]
                    elif len(estado["nombre_jugador"]) < 15:
                        if event.unicode.isalpha() or event.unicode.isspace():
                            estado["nombre_jugador"] += event.unicode
                
                # Puntajes - Salir
                elif estado["estado_pantalla"] == "puntajes":
                    if event.key == pygame.K_r:
                        estado_juego = "jugando"
                        estado = crear_estado_inicial()
                        iniciar_musica()
                    elif event.key == pygame.K_ESCAPE:
                        estado_juego = "menu"
                        iniciar_musica_menu()
        
        # Actualizar intro
        if estado_juego == "intro":
            estado_intro = actualizar_intro(estado_intro, delta_time, historia, 50, 3000)
        
        # Lógica del juego
        if estado_juego == "jugando" and not estado["game_over"]:
            # Movimiento de la nave
            movimiento_nave(estado["nave"])
            
            # Actualizar balas
            estado["balas_lista"] = actualizar_balas(estado["balas_lista"])
            
            # Actualizar capybaras
            estado["capybara_lista"] = actualizar_capybaras(estado["capybara_lista"])
            
            # Colisiones balas con capybaras
            estado["balas_lista"], estado["capybara_lista"], puntos = detectar_colision_balas_enemigos(estado["balas_lista"], estado["capybara_lista"])
            estado["puntuacion"] += puntos
            if puntos > 0:
                sonido_colision.play()
            
            # Colisión nave con capybaras
            if detectar_colision_nave_enemigos(estado["nave"], estado["capybara_lista"])and not es_invulnerable:
                estado["vidas"] -= 1
                sonido_game_over.play()
                es_invulnerable = True
                ultimo_golpe = tiempo_actual

                # Verificar si se acabaron las vidas
                if estado["vidas"] <= 0:
                    estado["game_over"] = True
                    pygame.mixer.music.stop()
                    estado["estado_pantalla"] = "game_over"
        
        # Vuelve invulnerable al jugador por 2 segundos al ser golpeado
        if es_invulnerable:

            if tiempo_actual - ultimo_golpe > TIEMPO_INVULNERABLE:
                es_invulnerable = False

        # Dibujar según el estado
        if estado_juego == "intro":
            renderizar_intro(ventana, recursos_intro, estado_intro, WIDTH, HEIGHT)
            pygame.display.flip()
        
        elif estado_juego == "menu":
            dibujar_menu(ventana, boton_jugar, boton_ranking, boton_salir, texto_boton_jugar, texto_boton_ranking, texto_boton_salir, menu_fondo_img)
            pygame.display.flip()
        
        elif estado_juego == "ranking":
            mostrar_ranking(ventana, fuente)
            pygame.display.flip()
        
        elif estado_juego == "jugando":
            if estado["estado_pantalla"] == "jugando":
                dibujar_juego(ventana, fondo_img, nave_img, estado, capy_img, corazon_img, fuente, fuente_pequena, tiempo_actual, es_invulnerable)
            
            elif estado["estado_pantalla"] == "game_over":
                dibujar_game_over_simple(ventana, fondo_img, estado, fuente, fuente_pequena)
            
            elif estado["estado_pantalla"] == "entrada_nombre":
                dibujar_entrada_nombre(ventana, estado["nombre_jugador"], fuente_grande, fuente, fuente_pequena)
            
            elif estado["estado_pantalla"] == "puntajes":
                dibujar_puntajes(ventana, estado["puntajes_top"], fuente_grande, fuente, fuente_pequena)
            
            pygame.display.flip()
        
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()
