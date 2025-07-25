import pygame
import random
from consts.constantes import *

def capybaras():
    """Crea una lista de capybaras"""
    capy_lista = []
    for i in range(5):
        capy_dict = {
            # Rectangulo del capy, x para que no se salga de la pantalla, y = 0 
            "rect": pygame.Rect(random.randint(0, WIDTH - ANCHO_CAPYBARA), 0, ANCHO_CAPYBARA, ALTO_CAPYBARA),
            "velocidad": random.randint(2, 8),
            "color": random.choice([(139, 69, 19), (160, 82, 45), (205, 133, 63)]),
        }
        capy_lista.append(capy_dict)
    return capy_lista

def actualizar_capybaras(capybara_lista):
    """Actualiza la posición de los capybaras"""
    capybara_filtrados = []
    for capy in capybara_lista:
        if capy["rect"].y + capy["rect"].height < HEIGHT: # si capy no sale de la pantalla
            capy["rect"].y += capy["velocidad"] # desplazamiento hacia abajo
            capybara_filtrados.append(capy) 

    if len(capybara_filtrados) <= 2: # Cuantos capybaras siguen visibles en la pantalla
        nuevos_capybaras = capybaras() # se crean nuevos
        capybara_filtrados.extend(nuevos_capybaras)
    
    return capybara_filtrados
