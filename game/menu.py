import pygame
from consts.constantes import *

def crear_elementos_menu():
    """Crea todos los elementos del menú con imágenes para los tres botones en disposición vertical"""

    # Tamaño para todos los botones
    boton_ancho = 150
    boton_alto = 50
    espacio_entre_botones = 25
    tamaño_boton = (boton_ancho, boton_alto)

    # Cargar y escalar imágenes de botones
    img_boton_jugar = pygame.image.load(ARCHIVOS['boton_jugar']).convert_alpha() #Carga la imagen y la convierte en una superficie
    img_boton_jugar = pygame.transform.smoothscale(img_boton_jugar, tamaño_boton) #Escala la imagen

    img_boton_ranking = pygame.image.load(ARCHIVOS['boton_ranking']).convert_alpha()
    img_boton_ranking = pygame.transform.smoothscale(img_boton_ranking, tamaño_boton)

    img_boton_salir = pygame.image.load(ARCHIVOS['boton_salir']).convert_alpha()
    img_boton_salir = pygame.transform.smoothscale(img_boton_salir, tamaño_boton)

    # Calcular posición vertical centrada
    total_alto = (boton_alto * 3) + (espacio_entre_botones * 2) # Alto total de los botones y el espacio entre ellos
    y_inicial = (HEIGHT - total_alto) // 2
    x_centro = (WIDTH - boton_ancho) // 2

    # Crear rectángulos para detección de clics
    boton_jugar = pygame.Rect(x_centro, y_inicial, boton_ancho, boton_alto) # Rectangulo de jugar
    boton_ranking = pygame.Rect(x_centro, y_inicial + boton_alto + espacio_entre_botones, boton_ancho, boton_alto) # Rectangulo de ranking
    boton_salir = pygame.Rect(x_centro, y_inicial + (boton_alto + espacio_entre_botones) * 2, boton_ancho, boton_alto) # Rectangulo de salir

    return boton_jugar, boton_ranking, boton_salir, img_boton_jugar, img_boton_ranking, img_boton_salir #img y rectangulos

def dibujar_menu(ventana, boton_jugar, boton_ranking, boton_salir,
                 img_boton_jugar, img_boton_ranking, img_boton_salir,
                 menu_fondo_img):
    """Dibuja la pantalla del menú con botones verticales usando imágenes"""

    ventana.blit(menu_fondo_img, (0, 0)) # Si se pasa una imagen de fondo, la dibuja


    # Dibujar imágenes centradas en sus rectángulos
    ventana.blit(img_boton_jugar, img_boton_jugar.get_rect(center=boton_jugar.center))
    ventana.blit(img_boton_ranking, img_boton_ranking.get_rect(center=boton_ranking.center))
    ventana.blit(img_boton_salir, img_boton_salir.get_rect(center=boton_salir.center))

    mouse_pos = pygame.mouse.get_pos()

    for boton, imagen in [(boton_jugar, img_boton_jugar),
                        (boton_ranking, img_boton_ranking),
                        (boton_salir, img_boton_salir)]:

        if boton.collidepoint(mouse_pos): # si el mouse esta sobre el boton
            imagen_hover = tintar_imagen(imagen, CHOCOLATE_BROWN)  # Aplica un tinte de chocolate brown
            ventana.blit(imagen_hover, imagen_hover.get_rect(center=boton.center))  # Dibuja la imagen con el tinte
        else:
            ventana.blit(imagen, imagen.get_rect(center=boton.center)) # sino lo dibuja normal



def manejar_click_menu(pos_mouse, boton_jugar, boton_ranking, boton_salir):
    """Maneja los clics en el menú"""
    # Verificar si se hizo clic en alguno de los botones, de ser asi retorne el string correspondiente
    if boton_jugar.collidepoint(pos_mouse):
        return "jugar" 
    elif boton_ranking.collidepoint(pos_mouse):
        return "ranking"
    elif boton_salir.collidepoint(pos_mouse):
        return "salir"
    return None # si no se hizo clic en ninguno de los botones

def tintar_imagen(imagen, color):
    """Devuelve una copia de la imagen con un tinte de color aplicado"""
    imagen_tintada = imagen.copy()
    tint_surface = pygame.Surface(imagen.get_size(), pygame.SRCALPHA) # Crear superficie con transparencia
    tint_surface.fill(color) # Llenar superficie con color
    imagen_tintada.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT) # Aplicar tinte en cada pixel
    return imagen_tintada
