import pygame
from consts.constantes import *

def crear_nave_inicial():
    """Crea la nave inicial del jugador"""
    # X, Centra la nave, Y Coloca la nave en la parte inferior
    return pygame.Rect(WIDTH // 2 - NAVE_ANCHO // 2, HEIGHT - NAVE_ALTO - 10, NAVE_ANCHO, NAVE_ALTO)

def movimiento_nave(nave):
    """Mueve la nave según las teclas presionadas"""
    # Detectar las teclas presionadas, TRUE si la tecla es presionada
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and nave.x > 0: # Verificar ←, y solo se mueve si nave.x > 0
        nave.x -= 5 # Mueve la nave hacia la izquierda 5 pixeles
    if keys[pygame.K_RIGHT] and nave.x < WIDTH - NAVE_ANCHO: # Verificar →
        nave.x += 5
    if keys[pygame.K_UP] and nave.y > 0: # Verificar ↑
        nave.y -= 5
    if keys[pygame.K_DOWN] and nave.y < HEIGHT - NAVE_ALTO: # Verificar ↓
        nave.y += 5

def cargar_recursos_golpe():
    """Carga los recursos relacionados con el daño"""
    ultimo_golpe = 0
    es_invulnerable = False
    return ultimo_golpe, es_invulnerable
