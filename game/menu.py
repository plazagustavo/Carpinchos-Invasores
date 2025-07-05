import pygame
from consts.constantes import *

def crear_elementos_menu():
    """Crea todos los elementos del menú"""
    fuente_inicio = pygame.font.Font(None, 30)
    
    # Botones horizontales en la parte inferior
    boton_ancho = 150
    boton_alto = 50
    espacio_entre_botones = 20
    y_botones = HEIGHT - 100
    
    # Calcular posiciones para centrar los 3 botones
    total_ancho = (boton_ancho * 3) + (espacio_entre_botones * 2)
    x_inicial = (WIDTH - total_ancho) // 2
    
    boton_jugar = pygame.Rect(x_inicial, y_botones, boton_ancho, boton_alto)
    boton_ranking = pygame.Rect(x_inicial + boton_ancho + espacio_entre_botones, y_botones, boton_ancho, boton_alto)
    boton_salir = pygame.Rect(x_inicial + (boton_ancho + espacio_entre_botones) * 2, y_botones, boton_ancho, boton_alto)
    
    texto_boton_jugar = fuente_inicio.render("Jugar", True, WHITE)
    texto_boton_ranking = fuente_inicio.render("Ranking", True, WHITE)
    texto_boton_salir = fuente_inicio.render("Salir", True, WHITE)
    
    return boton_jugar, boton_ranking, boton_salir, texto_boton_jugar, texto_boton_ranking, texto_boton_salir

def dibujar_menu(ventana, boton_jugar, boton_ranking, boton_salir, texto_boton_jugar, texto_boton_ranking, texto_boton_salir, menu_fondo_img=None):
    """Dibuja la pantalla del menú"""
    if menu_fondo_img:
        ventana.blit(menu_fondo_img, (0, 0))
    else:
        ventana.fill(BLACK)
    
    # Botones horizontales
    pygame.draw.rect(ventana, GREEN, boton_jugar)
    pygame.draw.rect(ventana, BLUE, boton_ranking)
    pygame.draw.rect(ventana, RED, boton_salir)
    
    # Texto de los botones centrado
    rect_jugar = texto_boton_jugar.get_rect(center=boton_jugar.center)
    rect_ranking = texto_boton_ranking.get_rect(center=boton_ranking.center)
    rect_salir = texto_boton_salir.get_rect(center=boton_salir.center)
    
    ventana.blit(texto_boton_jugar, rect_jugar)
    ventana.blit(texto_boton_ranking, rect_ranking)
    ventana.blit(texto_boton_salir, rect_salir)

def manejar_click_menu(pos_mouse, boton_jugar, boton_ranking, boton_salir):
    """Maneja los clics en el menú"""
    if boton_jugar.collidepoint(pos_mouse):
        return "jugar"
    elif boton_ranking.collidepoint(pos_mouse):
        return "ranking"
    elif boton_salir.collidepoint(pos_mouse):
        return "salir"
    return None
