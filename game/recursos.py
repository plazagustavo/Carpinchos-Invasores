import pygame
from consts.constantes import *

def cargar_recursos():
    """Carga todas las imágenes y sonidos (sin try/except)"""
    # Cargar sonidos
    sonido_disparo = pygame.mixer.Sound(ARCHIVOS['sonido_bala'])
    sonido_colision = pygame.mixer.Sound(ARCHIVOS['sonido_colision'])
    sonido_game_over = pygame.mixer.Sound(ARCHIVOS['sonido_vida_perdida'])
    
    # Cargar imágenes
    nave_img = pygame.image.load(ARCHIVOS['img_jugador']).convert_alpha()
    nave_img = pygame.transform.scale(nave_img, PLAYER_SIZE)
    
    capy_img = pygame.image.load(ARCHIVOS['img_enemigo']).convert_alpha()
    capy_img = pygame.transform.scale(capy_img, CAPYBARA_SIZE)
    
    fondo_img = pygame.image.load(ARCHIVOS['fondo']).convert()
    fondo_img = pygame.transform.scale(fondo_img, (WIDTH, HEIGHT))
    
    # Cargar imagen de fondo del menú
    menu_fondo_img = pygame.image.load(ARCHIVOS['menu_fondo']).convert()
    menu_fondo_img = pygame.transform.scale(menu_fondo_img, (WIDTH, HEIGHT))
    
    # Cargar imagen de intro
    intro_img = pygame.image.load(ARCHIVOS['img_intro']).convert()
    intro_img = pygame.transform.scale(intro_img, (WIDTH, HEIGHT))
    
    # Cargar imagen de corazón
    corazon_img = pygame.image.load(ARCHIVOS['img_corazon']).convert_alpha()
    corazon_img = pygame.transform.scale(corazon_img, (20, 20))
    
    # Fuentes
    fuente = pygame.font.Font(None, 36)
    fuente_pequena = pygame.font.Font(None, 24)
    fuente_grande = pygame.font.Font(None, 48)
    fuente_menu = pygame.font.Font(None, 30)
    fuente_controles = pygame.font.Font(None, 24)
    
    return sonido_disparo, sonido_colision, sonido_game_over, nave_img, capy_img, fondo_img, menu_fondo_img, intro_img, corazon_img, fuente, fuente_pequena, fuente_grande, fuente_menu, fuente_controles
