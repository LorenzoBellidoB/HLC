def codigo_Barras(codigo):
    # Inicializo la variable que returnare para saber si el codigo de barras es correcto
    correcto = False

    # Compruebo que el código introducido se encuentra en el margen
    if len(codigo) > 13:
        return correcto
    
    # Si el código es menor a 8 le añado "0" hasta llegar a 8 caracteres
    if len(codigo) < 8:
        codigo = '0' * (8 - len(codigo)) + codigo

    # Si el código es menor a 13 le añado "0" hasta llegar a 13 caracteres
    elif len(codigo) <= 13:
        codigo = '0' * (13 - len(codigo)) + codigo
    print(codigo)

    # Saco el número de control
    numeroControl = int(codigo[-1])

    # Inicializo la suma de los digitos
    suma = 0

    # Nueva longitud sin el digito de control
    nuevaLongitud = len(codigo)-1

    # Bucle para recorrer los digitos del codigo
    for i in range(nuevaLongitud):
        numero = int(codigo[i])
        # Compruebo si la posicion es par (lo multiplico por 1) o impar (lo multiplico por 3) y lo sumo con lo anterior
        if i % 2 == 0:
            suma += numero
        else:
            suma += numero * 3

    # Compuebo que la suma más el numero de control sean módulo de 10 para que el código de barras este correcto
    if (numeroControl + suma) % 10 == 0:
        correcto = True

    
    return correcto

