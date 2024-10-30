# Punto 2

print (" ")
print ("Torres Olvera Gael")
print (" ")

def tri_recursion(k):
    """
    Esta función suma todos los números enteros desde k hasta 1 utilizando recursión.
    
    Parámetros:
    k (int): El número hasta el cual se sumará.

    Retorna:
    int: La suma total desde k hasta 1.
    """
    # Verificamos la condición base para detener la recursión
    if k > 0:
        # Llamada recursiva: sumamos k con el resultado de la función llamada con k-1
        result = k + tri_recursion(k - 1)
        # Imprimimos el resultado acumulado en cada nivel de la recursión
        print(f"Suma hasta {k}: {result}")
    else:
        # Cuando k es 0, devolvemos 0 como base de la recursión
        result = 0

    # Devolvemos el resultado acumulado
    return result

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("Resultados del ejemplo de recursividad:")
    # Llamamos a la función con un valor inicial de 6
    total = tri_recursion
