import pygame

def cargar_imagen_intro(archivos):
    """Carga solo la imagen de intro"""
    return {"img_intro": pygame.image.load(archivos["img_intro"])}

def crear_estado_intro():
    """Crea el estado inicial de la introducción"""
    return {
        "tiempo_total": 0,
        "texto_mostrado": "",
        "completada": False
    }

def actualizar_intro(estado_intro, delta_time, historia, velocidad, tiempo_total_intro):
    """Actualiza la introducción y muestra el texto progresivamente"""
    if estado_intro["completada"]:
        return estado_intro

    estado_intro["tiempo_total"] += delta_time

    texto_total = "\n".join(historia)

    caracteres = int(estado_intro["tiempo_total"] / velocidad)

    if caracteres < len(texto_total):
        estado_intro["texto_mostrado"] = texto_total[:caracteres]
    else:
        estado_intro["texto_mostrado"] = texto_total
        if estado_intro["tiempo_total"] >= tiempo_total_intro + 4000:
            estado_intro["completada"] = True

    return estado_intro

def manejar_evento_intro(estado_intro, evento):
    """Detecta si el usuario quiere saltar la intro"""
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_SPACE or evento.key == pygame.K_RETURN or evento.key == pygame.K_ESCAPE:
            estado_intro["completada"] = True
    return estado_intro

def renderizar_intro(pantalla, recursos, estado_intro, ancho_pantalla, alto_pantalla):
    """Renderiza la pantalla de introducción"""
    if 'img_intro' in recursos:
        pantalla.blit(recursos['img_intro'], (0, 0))
    
    if 'fuente_menu' in recursos:
        y_pos = 100
        lineas = estado_intro["texto_mostrado"].split('\n')
        for linea in lineas:
            if linea.strip():
                texto = recursos['fuente_menu'].render(linea, True, (255, 255, 255))
                pantalla.blit(texto, (50, y_pos))
                y_pos += 40

    if estado_intro["completada"] and 'fuente_controles' in recursos:
        mensaje = recursos['fuente_controles'].render("Presiona cualquier tecla para continuar...", True, (255, 255, 0))
        pantalla.blit(mensaje, (ancho_pantalla // 2 - mensaje.get_width() // 2, alto_pantalla - 50))

def debe_cambiar_a_menu(estado_intro):
    """Verifica si debe cambiar al menú"""
    return estado_intro["completada"]

def finalizar_intro(estado_juego, nuevo_estado):
    """Finaliza la intro y cambia al siguiente estado"""
    estado_juego["estado"] = nuevo_estado
    return estado_juego
