import pygame
from consts.constantes import *

def cargar_sonidos():
    """Carga y devuelve los sonidos del juego"""
    sonidos = {
        "disparo": pygame.mixer.Sound(ARCHIVOS['sonido_bala']),
        "colision": pygame.mixer.Sound(ARCHIVOS['sonido_colision']),
        "game_over": pygame.mixer.Sound(ARCHIVOS['sonido_vida_perdida'])
    }
    return sonidos
    
def cargar_imagenes():
    """Carga y devuelve las imágenes del juego"""
    imagenes = {
        "nave": pygame.transform.scale(
            pygame.image.load(ARCHIVOS['img_jugador']).convert_alpha(), PLAYER_SIZE),
        "capybara": pygame.transform.scale(
            pygame.image.load(ARCHIVOS['img_enemigo']).convert_alpha(), CAPYBARA_SIZE),
        "fondo": pygame.transform.scale(
            pygame.image.load(ARCHIVOS['fondo']).convert(), (WIDTH, HEIGHT)),
        "menu_fondo": pygame.transform.scale(
            pygame.image.load(ARCHIVOS['menu_fondo']).convert(), (WIDTH, HEIGHT)),
        "intro": pygame.transform.scale(
            pygame.image.load(ARCHIVOS['img_intro']).convert(), (WIDTH, HEIGHT)),
        "corazon": pygame.transform.scale(
            pygame.image.load(ARCHIVOS['img_corazon']).convert_alpha(), (20, 20)),
        "boton_jugar":  pygame.transform.scale(
            pygame.image.load(ARCHIVOS['boton_jugar']).convert_alpha(), (200, 50))

    }
    return imagenes
    
def cargar_fuentes():
    """Carga y devuelve las fuentes del juego"""
    fuentes = {
        "normal": pygame.font.Font(None, 36),
        "pequena": pygame.font.Font(None, 24),
        "grande": pygame.font.Font(None, 48),
        "menu": pygame.font.Font("assets/fonts/gotic.ttf", 24),
        "controles": pygame.font.Font(None, 24)
    }
    return fuentes