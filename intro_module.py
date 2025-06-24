import pygame
from consts import (
    TIEMPO_INTRO, VELOCIDAD_TEXTO_INTRO, HISTORIA_INTRO, 
    ANCHO_PANTALLA, ALTO_PANTALLA, ESTADO_MENU, ARCHIVOS
)
import game_state_module

def cargar_imagen_intro():
    """Carga solo la imagen de intro y retorna un diccionario simple"""
    return {'img_intro': pygame.image.load(ARCHIVOS['img_intro'])}

def crear_estado_intro():
    """Crea el estado inicial de la introducción"""
    return {
        'tiempo_total': 0, #los dos primeros son 'acumuladores de "strings" e "int"
        'texto_mostrado': "",
        'completada': False
    }

def actualizar_intro(estado_intro, delta_time):
    """Actualiza cuánto texto mostrar según el tiempo que pasó"""
    if estado_intro['completada']:
        return estado_intro
    
    estado_intro['tiempo_total'] += delta_time
    todo_el_texto = "\n".join(HISTORIA_INTRO)
    caracteres_a_mostrar = int(estado_intro['tiempo_total'] / VELOCIDAD_TEXTO_INTRO)
    
    if caracteres_a_mostrar < len(todo_el_texto):
        estado_intro['texto_mostrado'] = todo_el_texto[:caracteres_a_mostrar]
    else:
        estado_intro['texto_mostrado'] = todo_el_texto
        if estado_intro['tiempo_total'] >= TIEMPO_INTRO + 4000:
            estado_intro['completada'] = True
    
    return estado_intro

def manejar_evento_intro(estado_intro, evento):
    """Detecta si el usuario quiere saltar la introducción"""
    if evento.type == pygame.KEYDOWN:
        estado_intro['completada'] = True
        return estado_intro, True
    return estado_intro, False

def procesar_lineas_texto(texto_mostrado):
    """Convierte el texto en líneas usando bucle for en lugar de list comprehension"""
    # Reemplazar puntos y comas por saltos de línea
    texto_procesado = texto_mostrado.replace(';', '.\n')
    lineas_brutas = texto_procesado.split('\n')
    
    # Usar bucle for para procesar las líneas
    lineas_finales = []
    for linea in lineas_brutas:
        linea_limpia = linea.strip()
        if linea_limpia:  # Solo agregar líneas que no estén vacías
            lineas_finales.append(linea_limpia)
    
    return lineas_finales

def renderizar_intro(pantalla, recursos, estado_intro):
    """Dibuja la introducción en pantalla"""
    if 'img_intro' in recursos:
        pantalla.blit(recursos['img_intro'], (0, 0))
    else:
        pantalla.fill((0, 0, 0))
    
    # Procesar líneas usando la nueva función
    lineas = procesar_lineas_texto(estado_intro['texto_mostrado'])
    
    y_inicio = 40
    for i, linea in enumerate(lineas):
        texto_surface = recursos['fuente_menu'].render(linea, True, (0, 0, 0))
        texto_rect = texto_surface.get_rect(center=(ANCHO_PANTALLA // 2, y_inicio + i * 80))
        pantalla.blit(texto_surface, texto_rect)

    # Instrucciones para continuar
    if estado_intro['tiempo_total'] > 2000:
        instruccion = recursos['fuente_controles'].render("Presiona cualquier tecla para continuar", True, (0, 0, 0))
        rect_instruccion = instruccion.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA - 50))
        pantalla.blit(instruccion, rect_instruccion)

def intro_completada(estado_intro):
    """Dice si la introducción ya terminó"""
    return estado_intro['completada']

def finalizar_intro():
    """Termina la introducción y va al menú"""
    game_state_module.cambiar_estado(ESTADO_MENU)

def debe_cambiar_a_menu(estado_intro):
    """Dice si hay que cambiar al menú principal"""
    return estado_intro['completada']