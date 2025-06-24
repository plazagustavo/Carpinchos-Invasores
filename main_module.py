import pygame
from config_module import ANCHO_PANTALLA, ALTO_PANTALLA, ESTADO_INTRO, ESTADO_MENU, ESTADO_JUGANDO, ESTADO_GAME_OVER, ESTADO_INGRESO_NOMBRE, ESTADO_RANKING
import game_state_module
from resources_module import cargar_recursos, configurar_audio
from renderer_module import mostrar_menu, mostrar_game_over, renderizar_juego, mostrar_ingreso_nombre, mostrar_ranking
from game_logic_module import actualizar_juego
from input_handler_module import procesar_eventos
import input_nombre_module
import intro_module

def inicializar_pygame():
    """Inicializa pygame y configura la ventana principal"""
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Carpinchos Invasores")
    return pantalla

def configurar_juego(recursos):
    """Configura los elementos iniciales del juego"""
    pygame.display.set_icon(recursos['icono'])
    configurar_audio()

def ejecutar_frame(pantalla, recursos, delta_time, estado_intro):
    """Ejecuta un frame completo del juego"""
    estado_actual = game_state_module.obtener_estado()

    if estado_actual == ESTADO_INTRO:
        estado_intro = intro_module.actualizar_intro(estado_intro, delta_time)
        intro_module.renderizar_intro(pantalla, recursos, estado_intro)
        
        # Verificar si debe cambiar al menú
        if intro_module.debe_cambiar_a_menu(estado_intro):
            intro_module.finalizar_intro()
            
    elif estado_actual == ESTADO_MENU:
        mostrar_menu(pantalla, recursos)
    elif estado_actual == ESTADO_JUGANDO:
        actualizar_juego(recursos)
        renderizar_juego(pantalla, recursos)
    elif estado_actual == ESTADO_GAME_OVER:
        mostrar_game_over(pantalla, recursos)
    elif estado_actual == ESTADO_INGRESO_NOMBRE:
        input_nombre_module.actualizar_cursor(delta_time)
        mostrar_ingreso_nombre(pantalla, recursos)
    elif estado_actual == ESTADO_RANKING:
        mostrar_ranking(pantalla, recursos)

    pygame.display.flip()
    return estado_intro

def main():
    """Función principal del juego"""
    # Inicialización
    pantalla = inicializar_pygame()
    recursos = cargar_recursos()  # Esto debe incluir la img_intro
    configurar_juego(recursos)
    game_state_module.inicializar_enemigos()

    # Inicializar el input de nombre
    input_nombre_module.inicializar_input()
    
    # Crear el estado de la introducción
    estado_intro = intro_module.crear_estado_intro()
    game_state_module.cambiar_estado(ESTADO_INTRO)

    # Bucle principal del juego
    juego_activo = True
    reloj = pygame.time.Clock()

#Y finalmente, en el bucle principal del juego en main_module.py:

    while juego_activo:
        delta_time = reloj.tick(60)
        juego_activo, estado_intro = procesar_eventos(recursos, estado_intro)

        #juego_activo = procesar_eventos(recursos)
        estado_intro = ejecutar_frame(pantalla, recursos, delta_time, estado_intro)

    pygame.quit()

if __name__ == "__main__":
    main()