import pygame
from consts.constantes import *

def crear_estado_inicial():
    """Crea el estado inicial del juego"""
    return {
        "puntuacion": 0,
        "vidas": 3,
        "nombre_jugador": "",
        "es_record": False
    }

def dibujar_entrada_nombre(ventana, nombre_jugador, puntuacion, fuente, fuente_pequena):
    """Dibuja la pantalla para ingresar nombre cuando hay record"""
    ventana.fill(BLACK)
    
    # Título
    texto_titulo = fuente.render("¡NUEVO RECORD!", True, YELLOW)
    ventana.blit(texto_titulo, (WIDTH // 2 - 120, HEIGHT // 2 - 100))
    
    # Puntuación
    texto_puntos = fuente.render(f"Puntuacion: {puntuacion}", True, WHITE)
    ventana.blit(texto_puntos, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
    
    # Instrucción
    texto_instruccion = fuente_pequena.render("Ingresa tu nombre:", True, WHITE)
    ventana.blit(texto_instruccion, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
    
    # Campo de nombre
    nombre_mostrar = nombre_jugador + "_"
    texto_nombre = fuente.render(nombre_mostrar, True, GREEN)
    ventana.blit(texto_nombre, (WIDTH // 2 - 100, HEIGHT // 2 + 10))
    
    # Instrucciones
    texto_enter = fuente_pequena.render("ENTER: Guardar", True, WHITE)
    ventana.blit(texto_enter, (WIDTH // 2 - 60, HEIGHT // 2 + 50))

def manejar_entrada_nombre(event, nombre_jugador):
    """Maneja la entrada de texto para el nombre"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            return "guardar"
        elif event.key == pygame.K_BACKSPACE:
            return nombre_jugador[:-1]
        elif len(nombre_jugador) < 10:
            if event.unicode.isalpha() or event.unicode.isspace():
                return nombre_jugador + event.unicode.upper()
    return nombre_jugador

def verificar_record(puntuacion):
    """Verifica si la puntuación es un record"""
    from game.ranking import cargar_ranking
    ranking = cargar_ranking()
    return len(ranking) < 5 or (len(ranking) > 0 and puntuacion > min(ranking))
