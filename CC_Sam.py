import string
from langdetect import detect

ALFABETO = string.ascii_lowercase + string.digits

def algoritmo_descifrado(texto_cifrado, clave_descifrado):
    """Esta funcion descifra el texto a partir de una clave de descifrado"""
    texto_plano = ""
    for letra in texto_cifrado:
        if letra not in ALFABETO:
            texto_plano += letra
        else:
            indice_letra_cifrada = ALFABETO.index(letra)
            indice_letra_descifrada = indice_letra_cifrada - clave_descifrado
            texto_plano += ALFABETO[indice_letra_descifrada]
    return texto_plano

def fuerza_bruta(texto_cifrado):
    """Esta accion realiza fuerza bruta sobre el texto cifrado interceptado"""
    espacio_clave = range(len(ALFABETO))
    for clave in espacio_clave:
        texto_plano = algoritmo_descifrado(texto_cifrado, clave)
        lenguaje = detect(texto_plano)
        # identificamos si el lenguaje de texto plano es español
        if lenguaje == 'es':
            print(f"El texto descifrado es: {texto_plano}")
            print(f"La clave de descifrado es :{clave}")
            return

if __name__ == "__main__":
    # Leer el texto cifrado del usuario
    texto_cifrado = input("Por favor introduce el texto cifrado: ").lower()
    # Leer la clave de descifrado
    #clave_descifrado = int(input("Por favor introduce la clave de descifrado: "))
    # invocamos el metodo de descifrado
    #texto_plano = algoritmo_descifrado(texto_cifrado, clave_descifrado)
    #print(texto_plano)
   
    fuerza_bruta(texto_cifrado)


#texto cifrado: lzav lz bu tluzhql kl wyblihz
# El texto descifrado es: esto es un mensaje de pruebas
# La clave de descifrado es :7