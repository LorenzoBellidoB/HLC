abecedario: tuple = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z")

def cifradoCesar(cifrado: str, clave: int):
    posicion = abecedario.index(cifrado)
    posicionCifrada = posicion + clave
    letraCifrado = abecedario[posicionCifrada]
    return letraCifrado