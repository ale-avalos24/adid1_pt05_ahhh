def tablas_de_multiplicar():
    num = int(input("Ingrese un número para mostrar su tabla de multiplicar (1 al 10): "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")