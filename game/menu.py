import pygame
from consts.constantes import *

def crear_elementos_menu():
    """Crea todos los elementos del menú con imágenes para los tres botones en disposición vertical"""

    # Tamaño uniforme para todos los botones
    boton_ancho = 150
    boton_alto = 50
    espacio_entre_botones = 25
    tamaño_boton = (boton_ancho, boton_alto)

    # Cargar y escalar imágenes de botones
    img_boton_jugar = pygame.image.load(ARCHIVOS['boton_jugar']).convert_alpha()
    img_boton_jugar = pygame.transform.smoothscale(img_boton_jugar, tamaño_boton)

    img_boton_ranking = pygame.image.load(ARCHIVOS['boton_ranking']).convert_alpha()
    img_boton_ranking = pygame.transform.smoothscale(img_boton_ranking, tamaño_boton)

    img_boton_salir = pygame.image.load(ARCHIVOS['boton_salir']).convert_alpha()
    img_boton_salir = pygame.transform.smoothscale(img_boton_salir, tamaño_boton)

    # Calcular posición vertical centrada
    total_alto = (boton_alto * 3) + (espacio_entre_botones * 2)
    y_inicial = (HEIGHT - total_alto) // 2
    x_centro = (WIDTH - boton_ancho) // 2

    # Crear rectángulos para detección de clics
    boton_jugar = pygame.Rect(x_centro, y_inicial, boton_ancho, boton_alto)
    boton_ranking = pygame.Rect(x_centro, y_inicial + boton_alto + espacio_entre_botones, boton_ancho, boton_alto)
    boton_salir = pygame.Rect(x_centro, y_inicial + (boton_alto + espacio_entre_botones) * 2, boton_ancho, boton_alto)

    return boton_jugar, boton_ranking, boton_salir, img_boton_jugar, img_boton_ranking, img_boton_salir

def dibujar_menu(ventana, boton_jugar, boton_ranking, boton_salir,
                 img_boton_jugar, img_boton_ranking, img_boton_salir,
                 menu_fondo_img):
    """Dibuja la pantalla del menú con botones verticales usando imágenes"""
    
    if menu_fondo_img:
        ventana.blit(menu_fondo_img, (0, 0))
    else:
        ventana.fill(BLACK)

    # Dibujar imágenes centradas en sus rectángulos
    ventana.blit(img_boton_jugar, img_boton_jugar.get_rect(center=boton_jugar.center))
    ventana.blit(img_boton_ranking, img_boton_ranking.get_rect(center=boton_ranking.center))
    ventana.blit(img_boton_salir, img_boton_salir.get_rect(center=boton_salir.center))

    mouse_pos = pygame.mouse.get_pos()

    for boton, imagen in [(boton_jugar, img_boton_jugar),
                        (boton_ranking, img_boton_ranking),
                        (boton_salir, img_boton_salir)]:

        if boton.collidepoint(mouse_pos):
            imagen_hover = tintar_imagen(imagen, CHOCOLATE_BROWN) 
            ventana.blit(imagen_hover, imagen_hover.get_rect(center=boton.center))
        else:
            ventana.blit(imagen, imagen.get_rect(center=boton.center))



def manejar_click_menu(pos_mouse, boton_jugar, boton_ranking, boton_salir):
    """Maneja los clics en el menú"""
    if boton_jugar.collidepoint(pos_mouse):
        return "jugar"
    elif boton_ranking.collidepoint(pos_mouse):
        return "ranking"
    elif boton_salir.collidepoint(pos_mouse):
        return "salir"
    return None

def tintar_imagen(imagen, color):
    """Devuelve una copia de la imagen con un tinte de color aplicado"""
    imagen_tintada = imagen.copy()
    tint_surface = pygame.Surface(imagen.get_size(), pygame.SRCALPHA)
    tint_surface.fill(color)
    imagen_tintada.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return imagen_tintada
