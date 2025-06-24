# Configuración de pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Configuración de gameplay
CANTIDAD_ENEMIGOS = 5
VELOCIDAD_JUGADOR = 3
VELOCIDAD_ENEMIGO = 4
DESCENSO_ENEMIGO = 100 # averiguar que es!
VELOCIDAD_BALA = 15
VIDAS_INICIALES = 3

# Estados del juego
ESTADO_INTRO = 0
ESTADO_MENU = 1
ESTADO_JUGANDO = 2
ESTADO_GAME_OVER = 3
ESTADO_INGRESO_NOMBRE = 4
ESTADO_RANKING = 5

# Configuración de colisiones
DISTANCIA_COLISION_BALA = 27
DISTANCIA_COLISION_JUGADOR = 50

# Configuración de audio
VOLUMEN_MUSICA = 0.3

# Límites del jugador
LIMITE_JUGADOR_X = 736
LIMITE_JUGADOR_Y = 536

# Configuración de la introducción
TIEMPO_INTRO = 12000  # 6 segundos en milisegundos
VELOCIDAD_TEXTO_INTRO = 50  # Velocidad de aparición del texto

# Historia y textos de la introducción
HISTORIA_INTRO = [
    "Cansados de ser explotados por los humanos\n",
    'los "capys" se rebelan para dominar el mundo\n',
    "comenzando por Nordelta.\n",
    "Tu eres la unica persona que se resiste a su.......\n",
    "¿adorable apatía?\n",
    "como sea, tienes una sola mision\n",
    "¡DEBES DETENER LA AMENAZA CARPINCHO!\n"
]

# Rutas de archivos
ARCHIVOS = {
    
    'img_intro': "assets/images/fondos/capys_agresivos.jpeg",
    'icono': "assets/images/models/capybara.png",
    'fondo': "assets/images/fondos/nordelta_recorte.jpg",
    'fondo_menu': "assets/images/fondos/f15.jpeg",
    'img_game_over': "assets/images/fondos/capy_galactico.jpeg",
    'img_jugador': "assets/images/models/avion.png",
    'img_bala': "assets/images/models/bala.png",
    'img_enemigo': "assets/images/models/carpincho.png",
    'sonido_bala': 'assets/sounds/disparo.mp3',
    'sonido_colision': 'assets/sounds/Golpe.mp3',
    'sonido_vida_perdida': 'assets/sounds/vida_perdida.mp3',
    'musica': 'assets/sounds/space_zero_ost.mp3',
    'fuente': 'assets/fonts/gotic.ttf'
}