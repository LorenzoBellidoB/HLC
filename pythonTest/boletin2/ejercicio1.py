abecedario: tuple = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z")

def cifradoCesar(cifrado: str, clave: int):
    palabraCifrado = ""
    for letra in cifrado:
        if letra == " ":
            palabraCifrado += " "
        else:
            posicion = abecedario.index(letra)

            if (posicion + clave) >= len(abecedario):
                posicionCifrada = clave - (27%posicion)
                palabraCifrado += abecedario[posicionCifrada]

            else:
                posicionCifrada = posicion + clave
                palabraCifrado += abecedario[posicionCifrada]
    
    return palabraCifrado