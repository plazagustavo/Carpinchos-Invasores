import os
from consts.constantes import *

def cargar_ranking():
    """Carga el ranking desde el archivo txt"""
    ranking = []
    if os.path.exists("ranking.txt"):
        archivo = open("ranking.txt", "r")
        for linea in archivo:
            if linea.strip():
                puntos = int(linea.strip())
                ranking.append(puntos)
        archivo.close()
    return ranking

def cargar_ranking_con_nombres():
    """Carga el ranking con nombres desde el archivo txt"""
    ranking = []
    if os.path.exists("ranking_nombres.txt"):
        archivo = open("ranking_nombres.txt", "r")
        for linea in archivo:
            if ":" in linea:
                partes = linea.strip().split(":")
                if len(partes) == 2:
                    nombre = partes[0]
                    puntos = int(partes[1])
                    ranking.append([nombre, puntos])
        archivo.close()
    return ranking

def guardar_puntuacion(puntuacion):
    """Guarda una nueva puntuación en el ranking"""
    ranking = cargar_ranking()
    ranking.append(puntuacion)
    ranking.sort(reverse=True)
    ranking = ranking[:10]
    
    archivo = open("ranking.txt", "w")
    for puntos in ranking:
        archivo.write(str(puntos) + "\n")
    archivo.close()

def guardar_puntuacion_con_nombre(nombre, puntuacion):
    """Guarda una nueva puntuación con nombre"""
    ranking = cargar_ranking_con_nombres()
    ranking.append([nombre, puntuacion])
    ranking.sort(key=lambda x: x[1], reverse=True)
    ranking = ranking[:10]
    
    archivo = open("ranking_nombres.txt", "w")
    for nombre_jugador, puntos in ranking:
        archivo.write(f"{nombre_jugador}:{puntos}\n")
    archivo.close()

def mostrar_ranking(ventana, fuente):
    """Muestra el ranking en pantalla"""
    ranking = cargar_ranking_con_nombres()
    ventana.fill(BLACK)
    
    # Título
    texto_titulo = fuente.render("MEJORES PUNTUACIONES", True, WHITE)
    ventana.blit(texto_titulo, (WIDTH // 2 - 150, 100))
    
    # Mostrar puntuaciones
    y = 150
    if len(ranking) == 0:
        texto = fuente.render("No hay puntuaciones aun", True, WHITE)
        ventana.blit(texto, (WIDTH // 2 - 120, y))
    else:
        for i, entrada in enumerate(ranking[:10]):
            nombre = entrada[0]
            puntos = entrada[1]
            color = YELLOW if i == 0 else WHITE
            texto = fuente.render(f"{i+1}. {nombre}: {puntos}", True, color)
            ventana.blit(texto, (WIDTH // 2 - 150, y))
            y += 30
    
    # Instrucción para volver
    texto_volver = fuente.render("Presiona M para volver al menu", True, YELLOW)
    ventana.blit(texto_volver, (WIDTH // 2 - 150, HEIGHT - 50))
