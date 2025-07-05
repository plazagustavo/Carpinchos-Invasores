import os

def cargar_puntajes(archivo="puntajes.txt"):
    puntajes = []
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f: #con 'r' el archivo debe existir
            for linea in f:
                linea = linea.strip()
                if ':' in linea:
                    partes = linea.split(':') #reemplace la ',' por un ':'
                    if len(partes) == 2 and partes[1].strip().isdigit():# verificacion de que sean 2 lineas y el puntaje sea un digito
                        puntajes.append([partes[0].strip(), int(partes[1].strip())]) #gurada en lista vacia
    return puntajes

def guardar_puntajes(puntajes, archivo="puntajes.txt"):
    with open(archivo, 'w', encoding='utf-8') as f:
        for nombre, puntaje in puntajes: #recorre la lista puntajes
            f.write(f"{nombre}:{puntaje}\n") #modificacion de ',' por ':' sino, hay inconsistencia
#f es el archivo abierto y write le indica el texto a guradar

def ordenar_puntajes(puntajes):
    n = len(puntajes)
    for i in range(n):
        for j in range(0, n - i - 1): # En cada pasada se coloca el mayor puntaje al principio
            if puntajes[j][1] < puntajes[j + 1][1]: #compara los puntajes en la posición actual y la siguiente
                puntajes[j], puntajes[j + 1] = puntajes[j + 1], puntajes[j] #intercambia las posiciones directamente
    return puntajes

def agregar_puntaje(nombre, puntaje, archivo="puntajes.txt"):
    puntajes = cargar_puntajes(archivo) #Carga los puntajes existentes desde el archivo (funcion mas arriba)
    puntajes.append([nombre, puntaje]) #Agrega el nuevo puntaje a la lista, como un nuevo par
    puntajes = ordenar_puntajes(puntajes)[:5] #Ordena la lista de puntajes hasta el 5 mediante slicing
    guardar_puntajes(puntajes, archivo) #guarda el puntaje sobrescribiendo el contenido anterior
    return puntajes

def obtener_top_puntajes(archivo="puntajes.txt"):
    return ordenar_puntajes(cargar_puntajes(archivo))[:5] # se puede considerar un caso de funciones anidadas.

def limpiar_nombre(nombre):
    nombre = nombre.strip().upper()
    return nombre[:15] if nombre else "ANONIMO"


def es_top_puntaje(puntaje, archivo="puntajes.txt"):
    puntajes = obtener_top_puntajes(archivo) #devuelve la lista de los 5 puntajes más altos actuales.
    return len(puntajes) < 5 or puntaje > puntajes[-1][1] #puntaje es el [1] de la lista ya guardada
#a su vez [-1] se refiere al ultimo elemento de la lista y [1] a su segundo indice, o sea, el numero /valor
