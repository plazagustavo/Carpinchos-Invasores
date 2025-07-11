import pygame
from consts.constantes import *

def inicializar_pygame():
    """Inicializa pygame y carga recursos"""
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Carpinchos Invasores')
    icono = pygame.image.load(ARCHIVOS["icono"])
    pygame.display.set_icon(icono)
    
    ventana = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    return ventana, clock
