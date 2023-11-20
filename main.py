import I_Suma
import II_Producto
import III_division
import iv_factorial
import V_Tablas_multiplicar
import VI_cubo_y_cuadrado
import VII_Promedio


#iv_factorial.factorial()
print("-----------------------")
print(" Bienvenido al menú")
print("-----------------------")

print("1. Suma de n números")
print("2. Producto de números")
print("3. División de números")
print("4. Factorial de un número")
print("5. Tablas de multiplicar")
print("6. Cubo y cuadrado de un número")
print("7. Cálculo de promedio")

try:
    opcion = int(input("Ingresa la opción que deseas realizar (1-7): "))

    if opcion == 1:
        I_Suma.sumar()
    elif opcion == 2:
        II_Producto.producto()
    elif opcion == 3:
        III_division.division_dos_numeros()
    elif opcion == 4:
        iv_factorial.factorial()
    elif opcion == 5:
        V_Tablas_multiplicar.tablas_de_multiplicar()
    elif opcion == 6:
        VI_cubo_y_cuadrado.calcular_cuadrado_y_cubo()
    elif opcion == 7:
        VII_Promedio.calcular_promedio()
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 7.")

except ValueError:
    print("Por favor, ingresa un número entero para la opción.")
