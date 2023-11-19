def calcular_promedio():
    numeros = []
    num = 0
    while num != -1:
        num = float(input("Ingrese los numeros que desee promediar (utilizar -1 para calcular el promedio): "))
        if num != -1:
            numeros.append(num)
    if numeros:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números es: {promedio}")
    else:
        print("No se ingresaron números.")