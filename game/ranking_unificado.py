import os
import pygame
from consts.constantes import *

# ===== FUNCIONES PRINCIPALES DE MANEJO DE PUNTAJES =====

def cargar_puntajes(archivo="puntajes.txt"):
    """Carga los puntajes desde archivo"""
    puntajes = []
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if ':' in linea:
                    partes = linea.split(':')
                    if len(partes) == 2 and partes[1].strip().isdigit():
                        puntajes.append([partes[0].strip(), int(partes[1].strip())])
    return puntajes

def guardar_puntajes(puntajes, archivo="puntajes.txt"):
    """Guarda los puntajes en archivo"""
    with open(archivo, 'w', encoding='utf-8') as f:
        for nombre, puntaje in puntajes:
            f.write(f"{nombre}:{puntaje}\n")

def ordenar_puntajes(puntajes):
    """Ordena los puntajes de mayor a menor usando bubble sort"""
    n = len(puntajes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if puntajes[j][1] < puntajes[j + 1][1]:
                puntajes[j], puntajes[j + 1] = puntajes[j + 1], puntajes[j]
    return puntajes

def agregar_puntaje(nombre, puntaje, archivo="puntajes.txt"):
    """Agrega un nuevo puntaje y mantiene solo el top 5"""
    puntajes = cargar_puntajes(archivo)
    puntajes.append([nombre, puntaje])
    puntajes = ordenar_puntajes(puntajes)[:5]
    guardar_puntajes(puntajes, archivo)
    return puntajes

def obtener_top_puntajes(archivo="puntajes.txt"):
    """Obtiene los top 5 puntajes"""
    return ordenar_puntajes(cargar_puntajes(archivo))[:5]

def limpiar_nombre(nombre):
    """Limpia y formatea el nombre del jugador"""
    nombre = nombre.strip().upper()
    return nombre[:15] if nombre else "ANONIMO"

def es_top_puntaje(puntaje, archivo="puntajes.txt"):
    """Verifica si el puntaje califica para el top 5"""
    puntajes = obtener_top_puntajes(archivo)
    return len(puntajes) < 5 or puntaje > puntajes[-1][1]

# ===== FUNCIONES DE VISUALIZACIÓN =====

def mostrar_ranking(ventana, fuente):
    """Muestra el ranking en pantalla - compatible con pantallas.py"""
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

def dibujar_puntajes(ventana, puntajes_top, fuente_grande, fuente, fuente_pequena):
    """Dibuja la tabla de mejores puntajes - compatible con estados.py"""
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

# ===== FUNCIONES DE COMPATIBILIDAD =====

def cargar_ranking():
    """Función de compatibilidad para estados.py"""
    puntajes = obtener_top_puntajes()
    return [puntaje[1] for puntaje in puntajes]  # Solo los números

def guardar_puntuacion_con_nombre(nombre, puntuacion):
    """Función de compatibilidad - usa el sistema principal"""
    nombre_limpio = limpiar_nombre(nombre)
    return agregar_puntaje(nombre_limpio, puntuacion)