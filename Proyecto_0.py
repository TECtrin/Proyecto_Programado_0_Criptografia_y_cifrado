#0 Menu
continuar = True
while continuar:
    try:
        print("\n"*30)
        print(" ___  ___   _______  __   __   __    __ ")
        print("|   \/   | |   ____||  \ |  | |  |  |  |")
        print("|  \  /  | |  |__   |   \|  | |  |  |  |")
        print("|  |\/|  | |   __|  |    `  | |  |  |  |")
        print("|  |  |  | |  |____ |  |\   | |  `--´  |")
        print("|__|  |__| |_______||__| \__|  \______/ ")
        print("")
        print("Bienvenido al codificador/decodificador.")
        print("1. Cifrado César")
        print("2. Cifrado monoalfabético con palabra clave")
        print("3. Cifrado Vigenère")
        print("4. Cifrado PlayFair modificado")
        print("5. Cifrado Rail Fence")
        print("")
        cifrado = input("Escriba el número correspondiente del cifrado a utilizar: ")
        
        if cifrado == "1":
            texto = input("Escriba el mensaje: ")
            desplazamiento = int(input("Escriba el desplazamiento: "))
            n = input("Para codificar un mensaje escriba 1, para decodificar, escriba 2: ")
            if n == "1":
                print("El mensaje codificado es: ", cesarCod(texto, desplazamiento))
            elif n == "2":
                print("El mensaje decodificado es: ", cesarDec(texto, desplazamiento))
            continuar = False

        elif cifrado == "2":
            texto = input("Escriba el mensaje: ")
            palabra = input("Escriba la palabra clave: ")
            n = input("Para codificar un mensaje escriba 1, para decodificar, escriba 2: ")
            if n == "1":
                print("El mensaje codificado es: ", monoCod(texto, palabra))
            elif n == "2":
                print("El mensaje decodificado es: ", monoDec(texto, palabra))
            continuar = False
            
        elif cifrado == "3":
            texto = input("Escriba el mensaje: ")
            palabra = input("Escriba la palabra clave: ")
            n = input("Para codificar un mensaje escriba 1, para decodificar, escriba 2: ")
            if n == "1":
                print("El mensaje codificado es: ", vigenereCod(texto, palabra))
            elif n == "2":
                print("El mensaje decodificado es: ", vigenerDec(texto, palabra))
            continuar = False
                
        elif cifrado == "4":
            texto = input("Escriba el mensaje: ")
            palabra = input("Escriba palabra clave: ")
            n = input("Para codificar un mensaje escriba 1, para decodificar, escriba 2: ")
            if n == "1":
                print("El mensaje codificado es: ", playfairCod(texto, palabra))
            elif n == "2":
                print("El mensaje decodificado es: ", playfairDec(texto, palabra))
            continuar = False
                
        elif cifrado == "5":
            texto = input("Escriba el mensaje: ")
            n = input("Para codificar un mensaje escriba 1, para decodificar, escriba 2: ")
            if n == "1":
                print("El mensaje codificado es: ", railfenceCod(texto))
            elif n == "2":
                print("El mensaje decodificado es: ", railfenceDec(texto))
            continuar = False
        
        else:
            print("ERROR: Opcion invalida")
        
    except Exception as e:
        print("ERROR", e)
              
#1. Cifrado César


#2. Cifrado monoalfabético con palabra clave
def str_limpio(str):
    str = str.lower()
    str = str.replace("á", "a")
    str = str.replace("é", "e")
    str = str.replace("í", "i")
    str = str.replace("ó", "o")
    str = str.replace("ú", "u")
    str = str.replace("ü", "u")
    #if not str.isalpha():
    #    raise ValueError("El mensaje solo puede contener letras")
    return str

def eliminar_repetidos(str):
    resultado = ""
    for letra in str:
        if letra not in resultado:
            resultado += letra
    return resultado

def construir_alfabeto_cifrado(palabra):
    alfabeto_original = "abcdefghijklmnñopqrstuvwxyz"
    alfabeto_cifrado = ""
    for letra in palabra:
        if letra in alfabeto_original:
            alfabeto_original = alfabeto_original.replace(letra, "")
            alfabeto_cifrado = alfabeto_cifrado + letra
    alfabeto_cifrado = alfabeto_cifrado + alfabeto_original
    return alfabeto_cifrado

def cifrado(texto,alfabeto_cifrado):
    alfabeto_original = "abcdefghijklmnñopqrstuvwxyz"
    mapeo = dict(zip(alfabeto_original,alfabeto_cifrado))
    texto_codificado = ""
    for letra in texto:
        if letra in mapeo:
            texto_codificado += mapeo[letra]
        else:
            texto_codificado += letra
    return texto_codificado

def descifrado(texto,alfabeto_cifrado):
    alfabeto_original = "abcdefghijklmnñopqrstuvwxyz"
    mapeo = dict(zip(alfabeto_cifrado,alfabeto_original))
    texto_descodificado = ""
    for letra in texto:
        if letra in mapeo:
            texto_descodificado += mapeo[letra]
        else:
            texto_descodificado += letra
    return texto_descodificado

def monoCod(texto,palabra):
    """
    Codifica un texto usando un cifrado monoalfabetico
    """
    texto = str_limpio(texto)
    palabra = eliminar_repetidos(str_limpio(palabra))
    alfabeto_cifrado = construir_alfabeto_cifrado(palabra)
    return cifrado(texto,alfabeto_cifrado)

def monoDec(texto,palabra):
    """
    Decodifica un texto usando un cifrado monoalfabetico
    """
    texto = str_limpio(texto)
    palabra = eliminar_repetidos(str_limpio(palabra))
    alfabeto_cifrado = construir_alfabeto_cifrado(palabra)
    return descifrado(texto,alfabeto_cifrado)

#3. Cifrado Vigenère
def vigenereCod(texto, palabra):
    """Subrutina principal del método Vigenère de codificación. Toma el texto
    y la palabra, y mediante el uso de subrutinas, codifica el texto ingresado.
    Entradas:
    -texto: palabra o frase que se quiere codificar.
    -palabra: palabra clave con la que se va a codificar.
    Salidas:
    El mensaje codificado.
    Restricciones: Solo se aceptan Strings, solo se aceptan letras del alfabeto
    permitido y espacios."""
    
    texto = limpiarTextos(texto)
    palabra = limpiarTextos(palabra)

    palabraCifrada = prepararCifrar(texto, palabra)
    mensajeEncriptado = cifrar(texto, palabraCifrada)
    
    print("Texto limpio: ",texto)
    print("Palabra limpia: ",palabra)
    print("Palabra preparada: ", palabraCifrada)

    print("El mensaje encriptado es: ", mensajeEncriptado)


def limpiarTextos(entrada):
    """Función que se encarga de limpiar tanto el texto como la palabra dada
    por el usuario. Quita acentos y símbolos no incluidos en el alfabeto.
    Entradas:
    -texto: texto escrito por el usuario. Lo que se codificará.
    -palabra: palabra clave dada por el usuario.
    Salidas:
    Retorna el texto y la palabra sin acentos ni símbolos no aceptados.
    Restricciones: ninguna."""
    
    entrada_limpia = ""
    
    entrada = entrada.lower()
    entrada = entrada.replace("á", "a")
    entrada = entrada.replace("é", "e")
    entrada = entrada.replace("í", "i")
    entrada = entrada.replace("ó", "o")
    entrada = entrada.replace("ö", "o")
    entrada = entrada.replace("ú", "u")
    entrada = entrada.replace("ü", "u")
    
    for letra in entrada:
        if letra.isalpha() or letra == " ":
            entrada_limpia += letra
        else:
            raise ValueError("Sólo se permiten letras y espacios.")
    
    return entrada_limpia

def prepararCifrar(texto, palabra):
    """Subrutina que prepara la palabra clave para poder hacer el encriptado.
    Entradas:
    -palabra: la palabra clave.
    -texto: el texto que se va a encriptar.
    Salidas:
    La palabra cñave acomodada a lo largo del texto, lista para cifrar.
    Restricciones: ninguna."""
    
    palabraPreparada = ""
    j = 0
    for i in range (len(texto)):
        if texto[i] != " ":
            palabraPreparada += palabra[j]
            j += 1
            if j == len(palabra):
                j = 0
        else:
            palabraPreparada += " "

    return palabraPreparada

def cifrar(texto, palabraCifrada):
    """Subrutina que encripta el mensaje haciendo la suma de los valores de las letras.
    Entradas:
    -texto: el texto que se va a cifrar
    -palabraCifrada: la palabra preparada para cifrar el texto.
    Salidas:
    El mensaje encriptado.
    Restricciones: ninguna"""
    
    mensajeEncriptado = ""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"

    for i in range(len(texto)):
        if texto[i] != " ":
            LetraTexto = alfabeto.index(texto[i])
            LetraPalabra = alfabeto.index(palabraCifrada[i])
            NuevaLetra = LetraTexto + LetraPalabra
            
            if NuevaLetra < len(alfabeto):
                mensajeEncriptado += alfabeto[NuevaLetra]
            else:
                NuevaLetra = (NuevaLetra % 27)
                mensajeEncriptado += alfabeto[NuevaLetra]

        else:
            mensajeEncriptado += " "

    return mensajeEncriptado

def vigenerDec(texto, palabra):
    """Función que decodifica un texto encriptado a partir de una palabra clave.
    Entrada:
    -textoEncriptado: texto codificado.
    -palabra: palabra clave dada por el usuario.
    Salidas:
    Mensaje decodifcado.
    Restricciones:
    Ambos deben ser strings.
    Sólo pueden contener letras del alfabeto permitido y espacios.

    """

    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    mensajeDes = ""
    
    texto = limpiarTextos(texto)
    palabra = limpiarTextos(palabra)

    palabraPreparada = prepararCifrar(texto, palabra)

    for i in range(len(texto)):
        if texto[i] != " ":
            LetraTexto = alfabeto.index(texto[i])
            LetraPalabra = alfabeto.index(palabraPreparada[i])
            NuevaLetra = LetraTexto - LetraPalabra

            if NuevaLetra >= 0:
                mensajeDes += alfabeto[NuevaLetra]
            else:
                NuevaLetra = 27 + NuevaLetra
                mensajeDes += alfabeto[NuevaLetra]
        else:
            mensajeDes += " "

    return mensajeDes

#4. Cifrado PlayFair modificado


#5. Cifrado Rail Fence
def railfenceCod(texto):
    """
    Función que codifica un texto usando el cifrado Rail Fence, el cual busca codificarlo en forma de zigzag.
    Entradas y restricciones:
    -texto: Un string con el mensaje a codificar.
    Salidas:
    -texto_final: Un string con el mensaje codificado.
    """
    # Paso 1: Ajustar el mensaje a un múltiplo de 4
    longitud_mensaje = len(texto)
    while longitud_mensaje % 4 != 0:
        texto += " "
        longitud_mensaje += 1

    # Paso 2: Cambiar espacios en blanco por guiones
    texto = texto.replace(" ", "-")

    # Paso 3: Crear el zigzag
    num_lineas = 3
    rail = ['' for _ in range(num_lineas)]
    direccion_abajo = False
    fila = 0

    for char in texto:
        rail[fila] += char
        if fila == 0 or fila == num_lineas - 1:
            direccion_abajo = not direccion_abajo
        fila += 1 if direccion_abajo else -1

    # Concatenar las filas
    texto_cifrado = ''.join(rail)

    # Paso 4: Agrupar el texto en grupos de 5 caracteres
    texto_final = ' '.join(texto_cifrado[i:i + 5] for i in range(0, len(texto_cifrado), 5))

    return texto_final

def railfenceDec(texto_cifrado):
    """
    Función que decodifica un texto usando el cifrado Rail Fence, el cual fue codificado en forma de zigzag.
    Entradas y restricciones:
    -texto_cifrado: Un string con el mensaje codificado en Rail Fence.
    Salidas:
    -mensaje_decodificado: Un string con el mensaje decodificado.
    """
    # Paso 1: Eliminar espacios
    texto_cifrado = texto_cifrado.replace(" ", "")
    longitud_mensaje = len(texto_cifrado)

    # Paso 2: Crear una matriz vacía para el rail fence
    num_lineas = 3  # Número de niveles o "líneas"
    rail = [['\n' for _ in range(longitud_mensaje)] for _ in range(num_lineas)]

    # Paso 3: Marcar los lugares donde las letras deben ir en el rail
    dir_abajo = False
    fila, col = 0, 0

    for i in range(longitud_mensaje):
        if fila == 0 or fila == num_lineas - 1:
            dir_abajo = not dir_abajo  # Cambiar dirección (zigzag)

        rail[fila][col] = '*'
        col += 1

        fila += 1 if dir_abajo else -1

    # Paso 4: Llenar la matriz con los caracteres del texto cifrado
    index = 0
    for i in range(num_lineas):
        for j in range(longitud_mensaje):
            if rail[i][j] == '*' and index < longitud_mensaje:
                rail[i][j] = texto_cifrado[index]
                index += 1

    # Paso 5: Leer la matriz en el orden del zigzag para decodificar
    mensaje_decodificado = []
    fila, col = 0, 0
    for i in range(longitud_mensaje):
        if fila == 0 or fila == num_lineas - 1:
            dir_abajo = not dir_abajo  # Cambiar dirección (zigzag)

        if rail[fila][col] != '\n':
            mensaje_decodificado.append(rail[fila][col])
            col += 1

        fila += 1 if dir_abajo else -1

    # Paso 6: Reemplazar los guiones por espacios y eliminar guiones finales
    mensaje_decodificado = ''.join(mensaje_decodificado).replace("-", " ").rstrip()

    return mensaje_decodificado
