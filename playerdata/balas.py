import pygame
from consts.constantes import *

def crear_bala(nave_x, nave_y):
    """Crea una nueva bala"""
    # nave_x posiciona la bala en el centro de la nave, 2 - BALA_ANCHO corrige posicion de la bala, nave_y posiciona la bala sale de la parte superior de la nave
    bala = {
        "rect": pygame.Rect(nave_x + NAVE_ANCHO // 2 - BALA_ANCHO // 2, nave_y, BALA_ANCHO, BALA_ALTO),
        "velocidad": BALA_VELOCIDAD
    }
    return bala

def actualizar_balas(balas_lista):
    """Actualiza la posición de las balas"""
    balas_filtradas = []
    for bala in balas_lista:
        bala["rect"].y -= bala["velocidad"] # Resta eje y para que la bala suba
        if bala["rect"].y > 0: # si es < 0 la bala sale de la pantalla entonces se elimina  
            balas_filtradas.append(bala) # para que la bala no se elimine se agrega a la lista para q la vuelva a dibujar  # balas = actualizar_balas(balas)
    return balas_filtradas

def dibujar_balas(ventana, balas_lista):
    """Dibuja las balas en pantalla"""
    for bala in balas_lista:
        pygame.draw.rect(ventana, YELLOW, bala["rect"])
