# Funciones_TorresOlvera

Torres Olvera Gael

En esta practica, hacemos uso de las funciones en python

Ademas, en esta practica las lecciones son un resumen de los ejemplos y puestos en practica de lo que habia en classroom

# Funciones 1

print (" ")
print ("Torres Olvera Gael")
print (" ")

import math

def calcular_area_circulo(radio):

    """Calcula el área de un círculo dado su radio."""
    
    return math.pi * (radio ** 2)

def calcular_area_cuadrado(lado):

    """Calcula el área de un cuadrado dado su lado."""
    
    return lado ** 2

def main():

    print("Calculadora de áreas")
    
    print("1. Área de un círculo")
    
    print("2. Área de un cuadrado")
    
    opcion = input("Elige una opción (1 o 2): ")

    if opcion == '1':
    
        radio = float(input("Introduce el radio del círculo: "))
        
        area = calcular_area_circulo(radio)
        
        print(f"El área del círculo es: {area:.2f}")
        
    elif opcion == '2':
    
        lado = float(input("Introduce el lado del cuadrado: "))
        
        area = calcular_area_cuadrado(lado)
        
        print(f"El área del cuadrado es: {area:.2f}")
        
    else:
    
        print("Opción no válida. Por favor elige 1 o 2.")

if __name__ == "__main__":

    main()

![image](https://github.com/user-attachments/assets/eb34fc42-b242-4342-b979-d8ebd2188dbf)
![image](https://github.com/user-attachments/assets/0a781691-3372-4216-a14d-843bae8ab0bd)

# Funciones 2

print(" ")
print("Torres Olvera Gael")
print(" ")

def tri_recursion(k):

#Verificamos la condición base para detener la recursión

    if k > 0:

#Llamada recursiva: sumamos k con el resultado de la función llamada con k-1

        result = k + tri_recursion(k - 1)

        #Imprimimos el resultado acumulado en cada 

        #nivel de la recursión

        print(f"Suma hasta {k}: {result}")

    else:

        # Cuando k es 0, devolvemos 0 como base de la recursión

        result = 0

    #Devolvemos el resultado acumulado

    return result

def main():

    print ("Resultados")

#Llamamos a la función con un valor inicial de 6

total = tri_recursion(6)

print(f"Suma total: {total}")

#Ejecutamos la función principal

if __name__ == "__main__":

    main()
    
![image](https://github.com/user-attachments/assets/6c9202bd-ed41-40f3-b2c0-7da8ddd18543)
![image](https://github.com/user-attachments/assets/5d42784f-3b1a-4cb2-acff-7dd264a07a6b)


