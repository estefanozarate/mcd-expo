def euclides(a, b):
    """
    Calcula el máximo común divisor (MCD) de a y b usando
    el algoritmo de Euclides y el principio del buen orden.
    """
    # Aseguramos que a y b son positivos (principio del buen orden)
    a, b = abs(a), abs(b) #elimina el signo de los numeros
    
    if b == 0:
        # Caso base: si b es 0, el MCD es a
        # Esto es el mínimo elemento en el conjunto de divisores comunes
        return a
    # Paso recursivo: el MCD de (a, b) es el mismo que el de (b, a mod b)
    # Esto se basa en que cualquier divisor común de a y s
    return euclides(b, a % b)

# Ejemplo de uso
_a = int(input("valor a: "))
_b = int(input("valor b:  "))

resultado = euclides(_a, _b)
print(f"El MCD de {_a} y {_b} es {resultado}")



"""
Cada llamada recursiva reduce el segundo parámetro (b) a a % b, que es siempre menor que b.
Por el principio del buen orden, no existe una sucesión infinita descendente de enteros positivos, así que la recursión debe terminar.
Cuando b llega a 0, a es el mínimo positivo restante que divide ambos números, es decir, el MCD
"""
