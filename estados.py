import pygame
from consts.constantes import *
from puntajes_module import *
from playerdata.enemigos import capybaras
from playerdata.nave import crear_nave_inicial


def crear_estado_inicial():
    """Crea el estado inicial del juego"""
    return {
        "nave": crear_nave_inicial(),
        "capybara_lista": capybaras(),
        "balas_lista": [],
        "puntuacion": 0,
        "vidas": 3,
        "game_over": False,
        "tiempo_ultimo_disparo": 0,
        "estado_pantalla": "jugando",  # "jugando", "game_over", "entrada_nombre", "puntajes"
        "nombre_jugador": "",
        "puntajes_top": []
    }

def dibujar_game_over(ventana, fondo_img, estado, fuente, fuente_pequena):
    """Dibuja la pantalla de game over"""
    ventana.blit(fondo_img, (0, 0))
    
    texto_game_over = fuente.render("GAME OVER", True, RED)
    ventana.blit(texto_game_over, (WIDTH // 2 - 100, HEIGHT // 2 - 80))
    
    texto_puntuacion_final = fuente.render(f"Puntuacion Final: {estado['puntuacion']}", True, WHITE)
    ventana.blit(texto_puntuacion_final, (WIDTH // 2 - 120, HEIGHT // 2 - 30))
    
    # Mostrar diferentes opciones según si es puntaje alto o no
    if es_top_puntaje(estado["puntuacion"]):
        texto_record = fuente_pequena.render("¡NUEVO RECORD!", True, YELLOW)
        ventana.blit(texto_record, (WIDTH // 2 - 80, HEIGHT // 2 + 10))
    
    texto_reiniciar = fuente_pequena.render("R: Reiniciar", True, WHITE)
    ventana.blit(texto_reiniciar, (WIDTH // 2 - 60, HEIGHT // 2 + 40))
    
    texto_puntajes = fuente_pequena.render("T: Ver puntajes", True, WHITE)
    ventana.blit(texto_puntajes, (WIDTH // 2 - 80, HEIGHT // 2 + 65))

def dibujar_entrada_nombre(ventana, nombre_jugador, fuente_grande, fuente, fuente_pequena):
    """Dibuja la pantalla de entrada de nombre"""
    # Fondo semi-transparente
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    ventana.blit(overlay, (0, 0))
    
    # Título
    texto_titulo = fuente_grande.render("¡NUEVO RECORD!", True, YELLOW)
    rect_titulo = texto_titulo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    ventana.blit(texto_titulo, rect_titulo)
    
    # Instrucción
    texto_instruccion = fuente.render("Ingresa tu nombre:", True, WHITE)
    rect_instruccion = texto_instruccion.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    ventana.blit(texto_instruccion, rect_instruccion)
    
    # Campo de nombre
    nombre_display = nombre_jugador + "_" if len(nombre_jugador) < 15 else nombre_jugador
    texto_nombre = fuente.render(nombre_display, True, GREEN)
    rect_nombre = texto_nombre.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    # Dibujar rectángulo alrededor del nombre
    pygame.draw.rect(ventana, WHITE, rect_nombre.inflate(20, 10), 2)
    ventana.blit(texto_nombre, rect_nombre)
    
    # Instrucciones
    texto_enter = fuente_pequena.render("ENTER: Confirmar", True, WHITE)
    rect_enter = texto_enter.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
    ventana.blit(texto_enter, rect_enter)
    
    texto_esc = fuente_pequena.render("ESC: Cancelar", True, WHITE)
    rect_esc = texto_esc.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 85))
    ventana.blit(texto_esc, rect_esc)

def dibujar_puntajes(ventana, puntajes_top, fuente_grande, fuente, fuente_pequena):
    """Dibuja la tabla de mejores puntajes"""
    # Fondo semi-transparente
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    ventana.blit(overlay, (0, 0))
    
    # Título
    texto_titulo = fuente_grande.render("MEJORES PUNTAJES", True, YELLOW)
    rect_titulo = texto_titulo.get_rect(center=(WIDTH // 2, 100))
    ventana.blit(texto_titulo, rect_titulo)
    
    # Puntajes
    y_pos = 180
    for i, entrada in enumerate(puntajes_top):
        nombre = entrada[0]
        puntaje = entrada[1]
        color = YELLOW if i == 0 else WHITE
        texto_posicion = fuente.render(f"{i+1}.", True, color)
        texto_nombre = fuente.render(nombre, True, color)
        texto_puntaje = fuente.render(str(puntaje), True, color)
        
        ventana.blit(texto_posicion, (200, y_pos))
        ventana.blit(texto_nombre, (250, y_pos))
        ventana.blit(texto_puntaje, (450, y_pos))
        
        y_pos += 40
    
    # Instrucciones
    texto_continuar = fuente_pequena.render("R: Jugar de nuevo    ESC: Salir", True, WHITE)
    rect_continuar = texto_continuar.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    ventana.blit(texto_continuar, rect_continuar)
