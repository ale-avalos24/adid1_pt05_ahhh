def sumar():
    try:
        n = int(input("Ingresa la cantidad de numeros a sumar: "))
        suma = 0

        for i in range(n):
            numero = float(input(f"Ingrese el numero {i+1}: "))
            suma = suma + numero

        print(f"La suma de los {n} números ingresados es: {suma} ")

    except ValueError:
        print("Por favor, ingrese un número válido.")
