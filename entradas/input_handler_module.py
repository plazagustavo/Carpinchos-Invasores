# input_handler.py
"""
Manejo de eventos de teclado y entrada del usuario
"""
import pygame
from configuracion.consts import VELOCIDAD_JUGADOR, ESTADO_INTRO, ESTADO_MENU, ESTADO_JUGANDO, ESTADO_GAME_OVER, ESTADO_INGRESO_NOMBRE, ESTADO_RANKING
import juego.game_state_module as game_state_module
from juego.game_logic_module import crear_bala
import entradas.input_nombre_module as input_nombre_module
import puntajes.puntajes_module as puntajes_module
import juego.intro_module as intro_module

def manejar_eventos_intro(evento, estado_intro):
    """Maneja los eventos del teclado en la introducción"""
    estado_intro, evento_manejado = intro_module.manejar_evento_intro(estado_intro, evento)
    return estado_intro, evento_manejado

def manejar_eventos_menu(evento):
    """Maneja los eventos del teclado en el menú principal"""
    if evento.key == pygame.K_RETURN:
        game_state_module.reiniciar_juego()
        game_state_module.cambiar_estado(ESTADO_JUGANDO)
    elif evento.key == pygame.K_r:
        game_state_module.cambiar_estado(ESTADO_RANKING)
    elif evento.key == pygame.K_ESCAPE:
        return False  # Salir del juego
    return True

#Cuando el jugador presiona la tecla ESC en el menú principal, la función retorna False,
#lo que indica que el juego debe cerrarse.'''

#Este valor False luego se procesa en la función procesar_eventos() del mismo archivo:

def actualizar_movimiento_jugador():
    """Actualiza el movimiento del jugador basado en las teclas presionadas actualmente"""
    teclas = pygame.key.get_pressed()
    
    # Movimiento horizontal
    if teclas[pygame.K_LEFT]:
        game_state_module.jugador_x_cambio = -VELOCIDAD_JUGADOR
    elif teclas[pygame.K_RIGHT]:
        game_state_module.jugador_x_cambio = VELOCIDAD_JUGADOR
    else:
        game_state_module.jugador_x_cambio = 0
    
    # Movimiento vertical
    if teclas[pygame.K_UP]:
        game_state_module.jugador_y_cambio = -VELOCIDAD_JUGADOR
    elif teclas[pygame.K_DOWN]:
        game_state_module.jugador_y_cambio = VELOCIDAD_JUGADOR
    else:
        game_state_module.jugador_y_cambio = 0

def manejar_eventos_jugando(evento, recursos):
    """Maneja los eventos del teclado durante el juego"""
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_SPACE:
            recursos['sonido_bala'].play()
            game_state_module.balas.append(crear_bala(game_state_module.jugador_x, game_state_module.jugador_y))
    
    return True

def manejar_eventos_game_over(evento):
    """Maneja los eventos del teclado en la pantalla de Game Over"""
    if evento.key == pygame.K_RETURN:
        # Al presionar ENTER en Game Over, intentar guardar el puntaje
        if puntajes_module.es_top_puntaje(game_state_module.puntaje):
            game_state_module.cambiar_estado(ESTADO_INGRESO_NOMBRE)
        else:
            game_state_module.reiniciar_juego()
            game_state_module.cambiar_estado(ESTADO_MENU)
    elif evento.key == pygame.K_ESCAPE:
        game_state_module.cambiar_estado(ESTADO_MENU)

def manejar_eventos_ingreso_nombre(evento):
    """Maneja los eventos del teclado en la pantalla de ingreso de nombre"""
    if input_nombre_module.manejar_evento_nombre(evento):
        nombre_final = input_nombre_module.obtener_nombre()
        game_state_module.establecer_nombre_jugador(nombre_final)
        puntajes_module.agregar_puntaje(nombre_final, game_state_module.puntaje)
        input_nombre_module.inicializar_input()  # Reset para futuras entradas
        game_state_module.cambiar_estado(ESTADO_RANKING)
    return True

def manejar_eventos_ranking(evento):
    """Maneja los eventos del teclado en la pantalla de ranking"""
    if evento.key == pygame.K_RETURN:
        game_state_module.reiniciar_juego()
        game_state_module.cambiar_estado(ESTADO_JUGANDO)
    elif evento.key == pygame.K_ESCAPE:
        game_state_module.cambiar_estado(ESTADO_MENU)



def procesar_eventos(recursos, estado_intro):
    """Procesa todos los eventos del juego según el estado actual"""
    estado_actual = game_state_module.obtener_estado()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False, estado_intro

        # Manejar eventos KEYDOWN
        if evento.type == pygame.KEYDOWN:
            if estado_actual == ESTADO_INTRO:
                estado_intro, evento_manejado = manejar_eventos_intro(evento, estado_intro)
            elif estado_actual == ESTADO_MENU:
                if not manejar_eventos_menu(evento):
                    return False, estado_intro
            elif estado_actual == ESTADO_JUGANDO:
                if not manejar_eventos_jugando(evento, recursos):
                    return False, estado_intro
            elif estado_actual == ESTADO_GAME_OVER:
                manejar_eventos_game_over(evento)
            elif estado_actual == ESTADO_RANKING:
                manejar_eventos_ranking(evento)

        # Manejar eventos de ingreso de nombre (KEYDOWN y TEXTINPUT)
        if estado_actual == ESTADO_INGRESO_NOMBRE:
            if evento.type == pygame.KEYDOWN or evento.type == pygame.TEXTINPUT:
                manejar_eventos_ingreso_nombre(evento)

    # Actualizar movimiento del jugador si estamos jugando
    if estado_actual == ESTADO_JUGANDO:
        actualizar_movimiento_jugador()

    return True, estado_intro

