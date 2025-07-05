import pygame
from consts.constantes import *

def dibujar_vidas(ventana, vidas, fuente, corazon_img):
    """Dibuja las vidas en pantalla con corazones sin superposición"""
    # Posición del texto de vidas
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, WHITE)
    ventana.blit(texto_vidas, (WIDTH - 120, 10))
    
    # Dibujar corazones debajo del texto para evitar superposición
    for i in range(vidas):
        x_pos = WIDTH - 120 + (i * 25)
        y_pos = 40  # Debajo del texto
        ventana.blit(corazon_img, (x_pos, y_pos))
