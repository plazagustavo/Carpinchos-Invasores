import pygame
from consts.constantes import *

def iniciar_musica():
    """Inicia la música del juego"""
    pygame.mixer.music.load(ARCHIVOS['musica'])
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def iniciar_musica_menu():
    """Inicia la música del menú"""
    pygame.mixer.music.load(ARCHIVOS['menu_musica'])
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
