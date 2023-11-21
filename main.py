import I_Suma
import II_Producto
import III_division
import IV_Factorial
import V_Tablas_multiplicar
import VI_cubo_y_cuadrado
import VII_Promedio
import VIII_MaxMin

menu = """
-----------------------
 Bienvenido al menú
-----------------------

1. Suma de n números
2. Producto de números
3. División de números
4. Factorial de un número
5. Tablas de multiplicar
6. Cubo y cuadrado de un número
7. Cálculo de promedio
8. Maximo y minimo de conjunto de numeros
"""

print(menu)


try:
    opcion = int(input("Ingresa la opción que deseas realizar (1-8): "))

    if opcion == 1:
        I_Suma.sumar()
    elif opcion == 2:
        II_Producto.producto()
    elif opcion == 3:
        III_division.division_dos_numeros()
    elif opcion == 4:
        IV_Factorial.obt_factorial()
    elif opcion == 5:
        V_Tablas_multiplicar.tablas_de_multiplicar()
    elif opcion == 6:
        VI_cubo_y_cuadrado.calcular_cuadrado_y_cubo()
    elif opcion == 7:
        VII_Promedio.calcular_promedio()
    elif opcion == 8:
        VIII_MaxMin.maxymin()
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 8.")

except ValueError:
    print("Por favor, ingresa un número entero para la opción.")
