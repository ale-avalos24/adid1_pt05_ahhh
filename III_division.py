def division_dos_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 == 0:
        while num2 == 0:
            print("No se puede dividir entre cero.")
            num2 = float(input("Ingrese el segundo número: "))
            
    resultado = num1 / num2
    print(f"La división de {num1} entre {num2} es: {resultado}")