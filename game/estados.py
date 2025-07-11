import pygame
from consts.constantes import *
from game.ranking_unificado import es_top_puntaje
from playerdata.enemigos import capybaras
from playerdata.nave import crear_nave_inicial
from game.ranking_unificado import cargar_ranking

def crear_estado_inicial():
    """Crea el estado inicial del juego"""
    return {
        "nave": crear_nave_inicial(), #Crea la nave
        "capybara_lista": capybaras(), #Crea la lista de capybaras
        "balas_lista": [], #Crea la lista de balas
        "puntuacion": 0,
        "vidas": 3,
        "game_over": False, #Indica si el juego ha terminado
        "tiempo_ultimo_disparo": 0, #Tiempo del ultimo disparo, para controlar la frecuencia de disparo
        "estado_pantalla": "jugando",  # "jugando", "game_over", "entrada_nombre", "puntajes"
        "nombre_jugador": "", # Esto es para la pantalla de entrada de nombre
        "puntajes_top": [],
        "es_record": False # Si es true significa que el jugador ha obtenido un nuevo record
    }

def verificar_record(puntuacion):
    """Verifica si la puntuación es un record"""
    ranking = cargar_ranking()
    return len(ranking) < 5 or (len(ranking) > 0 and puntuacion > min(ranking))

def manejar_entrada_nombre(event, nombre_jugador):
    """Maneja la entrada de texto para el nombre"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            return "guardar"
        elif event.key == pygame.K_BACKSPACE:
            return nombre_jugador[:-1]
        elif len(nombre_jugador) < 10:
            if event.unicode.isalpha() or event.unicode.isspace():
                return nombre_jugador + event.unicode.upper()
    return nombre_jugador

def dibujar_game_over(ventana, fondo_img, estado, fuente, fuente_pequena):
    """Dibuja la pantalla de game over"""
    ventana.blit(fondo_img, (0, 0))
    
    texto_game_over = fuente.render("GAME OVER", True, RED)
    ventana.blit(texto_game_over, (WIDTH // 2 - 100, HEIGHT // 2 - 80))
    
    texto_puntuacion_final = fuente.render(f"Puntuacion Final: {estado['puntuacion']}", True, WHITE)
    ventana.blit(texto_puntuacion_final, (WIDTH // 2 - 120, HEIGHT // 2 - 30))
    
    if es_top_puntaje(estado["puntuacion"]):
        texto_record = fuente_pequena.render("¡NUEVO RECORD!", True, YELLOW)
        ventana.blit(texto_record, (WIDTH // 2 - 80, HEIGHT // 2 + 10))
    
    texto_reiniciar = fuente_pequena.render("R: Reiniciar", True, WHITE)
    ventana.blit(texto_reiniciar, (WIDTH // 2 - 60, HEIGHT // 2 + 40))
    
    texto_puntajes = fuente_pequena.render("T: Ver puntajes", True, WHITE)
    ventana.blit(texto_puntajes, (WIDTH // 2 - 80, HEIGHT // 2 + 65))

def dibujar_entrada_nombre(ventana, nombre_jugador, puntuacion, fuente_grande, fuente, fuente_pequena):
    """Dibuja la pantalla de entrada de nombre"""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    ventana.blit(overlay, (0, 0))
    
    texto_titulo = fuente_grande.render("¡NUEVO RECORD!", True, YELLOW)
    rect_titulo = texto_titulo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    ventana.blit(texto_titulo, rect_titulo)
    
    texto_puntos = fuente.render(f"Puntuacion: {puntuacion}", True, WHITE)
    ventana.blit(texto_puntos, (WIDTH // 2 - 100, HEIGHT // 2 - 60))
    
    texto_instruccion = fuente.render("Ingresa tu nombre:", True, WHITE)
    rect_instruccion = texto_instruccion.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    ventana.blit(texto_instruccion, rect_instruccion)
    
    nombre_display = nombre_jugador + "_" if len(nombre_jugador) < 15 else nombre_jugador
    texto_nombre = fuente.render(nombre_display, True, GREEN)
    rect_nombre = texto_nombre.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    pygame.draw.rect(ventana, WHITE, rect_nombre.inflate(20, 10), 2)
    ventana.blit(texto_nombre, rect_nombre)
    
    texto_enter = fuente_pequena.render("ENTER: Confirmar", True, WHITE)
    rect_enter = texto_enter.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
    ventana.blit(texto_enter, rect_enter)
    
    texto_esc = fuente_pequena.render("ESC: Cancelar", True, WHITE)
    rect_esc = texto_esc.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 95))
    ventana.blit(texto_esc, rect_esc)

def dibujar_puntajes(ventana, puntajes_top, fuente_grande, fuente, fuente_pequena):
    """Dibuja la tabla de mejores puntajes"""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    ventana.blit(overlay, (0, 0))
    
    texto_titulo = fuente_grande.render("MEJORES PUNTAJES", True, YELLOW)
    rect_titulo = texto_titulo.get_rect(center=(WIDTH // 2, 100))
    ventana.blit(texto_titulo, rect_titulo)
    
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
    
    texto_continuar = fuente_pequena.render("R: Jugar de nuevo    ESC: Salir", True, WHITE)
    rect_continuar = texto_continuar.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    ventana.blit(texto_continuar, rect_continuar)
