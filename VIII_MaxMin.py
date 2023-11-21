def maxymin():
    cant = int(input("Ingrese la cantidad de numeros a ingresar: "))
    conjunto = list()

    for i in range(cant):
        num = int(input("Ingrese un valor: ")) 
        conjunto.append(num)
    
    conjunto.sort()
    print("El maximo de la funcion es: ", conjunto[0])
    print("El minimo de la funcion es: ", conjunto[-1])