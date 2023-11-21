from math import factorial
    
def obt_factorial():
    num = int(input("Ingrese el numero a sacar factorial: "))
    res = factorial(num)
    print("\nEl factorial de {} es igual a {}".format(num, res))