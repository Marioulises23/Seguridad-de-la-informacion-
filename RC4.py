# Python3 program for the RC4 algorithm

# Función para cifrar un texto con una clave usando RC4
def encryption(n, input_text, input_key_number):
    global key, plain_text

    # Convertimos el texto plano a binario
    plain_text = text_to_binary(input_text)
   
    # Convertimos la clave a binario
    key = number_string_to_binary(input_key_number)

    # Mostrar el texto plano separado en bloques de 8 bits
    print("Texto plano")
    for i in range(0, len(plain_text), n):
        print(plain_text[i:i+n], end=' ')
    print("")

    # Mostrar la clave en binario separada en bloques de 8 bits
    print("Clave: ")
    for i in range(0, len(key), n):
        print(key[i:i+n], end=' ')
    print("")

    print("Bits : ", n)

    # Vector de estado S con valores de 0 a 2^n - 1
    S = [i for i in range(0, 2**n)]

    print("\nMatriz de estado S inicial:")
    print(S)

    # Dividimos la clave binaria en bloques de n bits
    key_list = [key[i:i + n] for i in range(0, len(key), n)]

    # Convertimos cada bloque de clave de binario a entero
    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2)

    # Dividimos el texto plano en bloques de n bits y lo convertimos a enteros
    global pt
    pt = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]
    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)

    # Si la clave es más corta que S, la repetimos hasta igualar la longitud
    diff = int(len(S) - len(key_list))
    if diff != 0:
        for i in range(0, diff):
            key_list.append(key_list[i])

    # KSA - Key Scheduling Algorithm: mezcla S usando la clave
    def KSA():
        j = 0
        N = len(S)
        for i in range(0, N):
            j = (j + S[i] + key_list[i]) % N
            S[i], S[j] = S[j], S[i]

    KSA()

    print("\nMatriz de permutación S después de KSA:")
    print(S)

    # PGRA - Pseudo-Random Generation Algorithm: genera flujo de clave
    def PGRA():
        N = len(S)
        i = j = 0
        global key_stream
        key_stream = []

        for k in range(0, len(pt)):
            i = (i + 1) % N
            j = (j + S[i]) % N
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % N
            key_stream.append(S[t])

    PGRA()

    # XOR entre flujo de clave y texto plano para obtener texto cifrado
    def XOR():
        global cipher_text
        cipher_text = []
        for i in range(len(pt)):
            c = key_stream[i] ^ pt[i]
            cipher_text.append(c)

    XOR()

    # Convertimos el texto cifrado a binario
    encrypted_to_bits = ""
    for i in cipher_text:
        encrypted_to_bits += '0' * (n - len(bin(i)[2:])) + bin(i)[2:]

    print("---------------------------------------------------------")
    # Mostrar texto cifrado en bloques de 8 bits
    print("Cipher text:")
    for i in range(0, len(encrypted_to_bits), n):
        print(encrypted_to_bits[i:i+n], end=' ')
    print()


# Función para descifrar el texto cifrado usando RC4
def decryption(n):
    # Repetimos la inicialización del vector S
    S = [i for i in range(0, 2**n)]

    print("\nMatriz de estado S inicial:")
    print(S)

    # Dividimos la clave en bloques de n bits y los convertimos a enteros
    key_list = [key[i:i + n] for i in range(0, len(key), n)]
    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2)

    # Recuperamos el texto plano original en formato de enteros
    global pt
    pt = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]
    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)

    # Repetimos la clave si es necesario
    diff = int(len(S) - len(key_list))
    if diff != 0:
        for i in range(0, diff):
            key_list.append(key_list[i])

    # KSA otra vez
    def KSA():
        j = 0
        N = len(S)
        for i in range(0, N):
            j = (j + S[i] + key_list[i]) % N
            S[i], S[j] = S[j], S[i]

    KSA()
    
    print("\nMatriz de permutación S después de KSA:")
    print(S)

    # PGRA otra vez para generar el mismo flujo de clave
    def do_PGRA():
        N = len(S)
        i = j = 0
        global key_stream
        key_stream = []

        for k in range(0, len(pt)):
            i = (i + 1) % N
            j = (j + S[i]) % N
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % N
            key_stream.append(S[t])

    do_PGRA()

    # Aplicamos XOR entre el flujo de clave y el texto cifrado
    def do_XOR():
        global original_text
        original_text = []
        for i in range(len(cipher_text)):
            p = key_stream[i] ^ cipher_text[i]
            original_text.append(p)

    do_XOR()

    # Convertimos el resultado descifrado a binario
    decrypted_to_bits = ""
    for i in original_text:
        decrypted_to_bits += '0' * (n - len(bin(i)[2:])) + bin(i)[2:]

    print(" ")
    print("\nTexto descifrado:")
    for i in range(0, len(decrypted_to_bits), n):
        print(decrypted_to_bits[i:i+n], end=' ')
    print()

    # Convertimos de binario a texto y lo mostramos
    recovered_text = binary_to_text(decrypted_to_bits)
    print("Texto recuperado:", recovered_text)


# Convierte un texto a  binario
def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

# Convierte una cadena binaria a texto
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

# Convierte una cadena numérica a binario (4 bits por dígito)
def number_string_to_binary(number_string):
    return ''.join(format(int(digit), '04b') for digit in number_string)


# Entrada del usuario
input_text = input("Ingrese el texto a cifrar: ")
input_key_number = input("Ingrese la clave (solo números): ")
n = int(input("Ingrese el valor de n (por ejemplo, 8): "))

# Ejecutamos el cifrado y descifrado
encryption(n, input_text, input_key_number)
print("---------------------------------------------------------")
decryption(n)

