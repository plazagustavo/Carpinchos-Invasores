import pygame
from consts.constantes import *
from game.ranking_unificado import obtener_top_puntajes, es_top_puntaje
from playerdata.balas import dibujar_balas
from game.vidas import dibujar_vidas

def mostrar_ranking(ventana, fuente):
    """Muestra el ranking en pantalla usando puntajes_module"""
    puntajes = obtener_top_puntajes()
    ventana.fill(BLACK)
    
    # Título
    texto_titulo = fuente.render("MEJORES PUNTUACIONES", True, WHITE)
    ventana.blit(texto_titulo, (WIDTH // 2 - 150, 100))
    
    # Mostrar puntuaciones
    y = 150
    if len(puntajes) == 0:
        texto = fuente.render("No hay puntuaciones aun", True, WHITE)
        ventana.blit(texto, (WIDTH // 2 - 120, y))
    else:
        for i, entrada in enumerate(puntajes):
            nombre = entrada[0]
            puntos = entrada[1]
            color = YELLOW if i == 0 else WHITE
            texto = fuente.render(f"{i+1}. {nombre}: {puntos}", True, color)
            ventana.blit(texto, (WIDTH // 2 - 150, y))
            y += 30
    
    # Instrucción para volver
    texto_volver = fuente.render("Presiona M para volver al menu", True, YELLOW)
    ventana.blit(texto_volver, (WIDTH // 2 - 150, HEIGHT - 50))

def dibujar_game_over_simple(ventana, fondo_img, estado, fuente, fuente_pequena):
    """Dibuja la pantalla de game over simple"""
    ventana.blit(fondo_img, (0, 0))
    
    # Pantalla de Game Over
    texto_game_over = fuente.render("GAME OVER", True, RED)
    ventana.blit(texto_game_over, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    
    texto_puntuacion_final = fuente.render(f"Puntuacion Final: {estado['puntuacion']}", True, WHITE)
    ventana.blit(texto_puntuacion_final, (WIDTH // 2 - 120, HEIGHT // 2))
    
    # Mostrar si es record
    if es_top_puntaje(estado["puntuacion"]):
        texto_record = fuente_pequena.render("¡NUEVO RECORD! Presiona N para ingresar nombre", True, YELLOW)
        ventana.blit(texto_record, (WIDTH // 2 - 200, HEIGHT // 2 + 30))
    
    texto_reiniciar = fuente_pequena.render("R: Reiniciar", True, WHITE)
    ventana.blit(texto_reiniciar, (WIDTH // 2 - 60, HEIGHT // 2 + 60))
    
    texto_menu = fuente_pequena.render("M: Menu", True, WHITE)
    ventana.blit(texto_menu, (WIDTH // 2 - 40, HEIGHT // 2 + 85))

def dibujar_juego(ventana, fondo_img, nave_img, estado, capy_img, corazon_img, fuente, fuente_pequena, tiempo, es_invulnerable):
    """Dibuja todos los elementos del juego"""
    # Dibujar fondo
    ventana.blit(fondo_img, (0, 0))
    
    # Dibuja la nave si el jugador no es golpeado o si los segundos son pares (esto provoca que parpadee)

    if not es_invulnerable or (tiempo%2) == 0:

        ventana.blit(nave_img, (estado["nave"].x, estado["nave"].y))
    
    # Dibujar capybaras
    for capy in estado["capybara_lista"]:
        ventana.blit(capy_img, (capy["rect"].x, capy["rect"].y))
    
    # Dibujar balas
    dibujar_balas(ventana, estado["balas_lista"])
    
    # Mostrar puntuación
    texto_puntos = fuente.render(f"Puntos: {estado['puntuacion']}", True, WHITE)
    ventana.blit(texto_puntos, (10, 10))
    
    # Mostrar vidas con corazones (usar las vidas reales del estado)
    dibujar_vidas(ventana, estado["vidas"], fuente, corazon_img)
    
    # Mostrar controles
    texto_espacio = fuente_pequena.render("ESPACIO: Disparar", True, WHITE)
    ventana.blit(texto_espacio, (10, HEIGHT - 60))
    
    texto_flechas = fuente_pequena.render("Flechas: Mover", True, WHITE)
    ventana.blit(texto_flechas, (10, HEIGHT - 35))
