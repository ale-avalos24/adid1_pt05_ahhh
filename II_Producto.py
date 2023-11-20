
def producto():
    try:
        n = int(input("Ingresa la cantidad de números a multiplicar: "))
        producto= 0

        for i in range(n):
            numero = float(input(f"Ingrese el número {i+1}: "))
            producto = producto + numero

        print(f"El producto de los {n} números ingresados es: {producto} ")

    except ValueError:
        print("Por favor, ingrese un número válido.")