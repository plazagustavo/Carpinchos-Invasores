import pygame

def detectar_colision_balas_enemigos(balas_lista, capybara_lista):
    """Detecta colisiones entre balas y capybaras"""
    balas_restantes = []
    capybaras_restantes = []
    puntos = 0
    
    for bala in balas_lista:
        bala_colisiono = False
        for capy in capybara_lista:
            if bala["rect"].colliderect(capy["rect"]):
                puntos += 10
                bala_colisiono = True
                break
        
        if not bala_colisiono:
            balas_restantes.append(bala)
    
    for capy in capybara_lista:
        capy_colisiono = False
        for bala in balas_lista:
            if bala["rect"].colliderect(capy["rect"]):
                capy_colisiono = True
                break
        
        if not capy_colisiono:
            capybaras_restantes.append(capy)
    
    return balas_restantes, capybaras_restantes, puntos

def detectar_colision_nave_enemigos(nave, capybara_lista):
    """Detecta si la nave colisiona con algún capybara"""
    for capy in capybara_lista:
        if nave.colliderect(capy["rect"]):
            return True
    return False
