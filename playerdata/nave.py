import pygame
from consts.constantes import *

def crear_nave_inicial():
    """Crea la nave inicial del jugador"""
    return pygame.Rect(WIDTH // 2 - NAVE_ANCHO // 2, HEIGHT - NAVE_ALTO - 10, NAVE_ANCHO, NAVE_ALTO)

def movimiento_nave(nave):
    """Mueve la nave según las teclas presionadas"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and nave.x > 0:
        nave.x -= 5
    if keys[pygame.K_RIGHT] and nave.x < WIDTH - NAVE_ANCHO:
        nave.x += 5
    if keys[pygame.K_UP] and nave.y > 0:
        nave.y -= 5
    if keys[pygame.K_DOWN] and nave.y < HEIGHT - NAVE_ALTO:
        nave.y += 5

def cargar_recursos_golpe():
    """Carga los recursos relacionados con el daño"""
    ultimo_golpe = 0
    es_invulnerable = False
    return ultimo_golpe, es_invulnerable
