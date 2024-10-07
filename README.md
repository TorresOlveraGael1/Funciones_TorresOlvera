# Funciones_TorresOlvera

Torres Olvera Gael

En esta practica, hacemos uso de las funciones en python

#Practica de funciones

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
