import pygame
from consts.constantes import *

def crear_bala(nave_x, nave_y):
    """Crea una nueva bala"""
    bala = {
        "rect": pygame.Rect(nave_x + NAVE_ANCHO // 2 - BALA_ANCHO // 2, nave_y, BALA_ANCHO, BALA_ALTO),
        "velocidad": BALA_VELOCIDAD
    }
    return bala

def actualizar_balas(balas_lista):
    """Actualiza la posición de las balas"""
    balas_filtradas = []
    for bala in balas_lista:
        bala["rect"].y -= bala["velocidad"]
        if bala["rect"].y > 0:
            balas_filtradas.append(bala)
    return balas_filtradas

def dibujar_balas(ventana, balas_lista):
    """Dibuja las balas en pantalla"""
    for bala in balas_lista:
        pygame.draw.rect(ventana, YELLOW, bala["rect"])
