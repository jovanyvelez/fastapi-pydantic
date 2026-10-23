"""
LISTAS EN PYTHON: GUÍA PRÁCTICA
===============================

Este archivo reúne ejemplos de creación, acceso, modificación,
ordenamiento y otras operaciones con listas.

Cómo usarlo:
1. Guarda este archivo como guia_listas.py.
2. Ejecútalo con:
       python guia_listas.py

Idea principal:
- Una lista es una colección ordenada y mutable de elementos.
- Se escribe entre corchetes [] y admite elementos de cualquier tipo.
- Los índices comienzan en 0; los índices negativos cuentan desde el final.
"""

# ============================================================
# 1. CREAR UNA LISTA
# ============================================================

vacia = []
frutas = ["manzana", "banana", "pera"]
mezclada = [1, "dos", 3.0, True]

print("\n1. Creación")
print(frutas)
print(mezclada)

# También se puede usar list() para crear una lista a partir
# de cualquier iterable.
numeros = list(range(5))
print(numeros)  # [0, 1, 2, 3, 4]


# ============================================================
# 2. ACCESO POR ÍNDICE Y SLICING
# ============================================================

print("\n2. Índices y slicing")
print(frutas[0])  # manzana
print(frutas[-1])  # pera

# Slicing: lista[inicio:fin:paso] (fin excluido)
print(frutas[1:])  # ['banana', 'pera']
print(frutas[:2])  # ['manzana', 'banana']
print(frutas[::2])  # ['manzana', 'pera']
print(frutas[::-1])  # ['pera', 'banana', 'manzana']  ← invertida

# Un índice fuera de rango lanza IndexError.
# print(frutas[10])


# ============================================================
# 3. AGREGAR ELEMENTOS
# ============================================================

print("\n3. Agregar elementos")

# append(): añade UN elemento al final.
frutas.append("naranja")
print("append:", frutas)

# extend(): añade todos los elementos de un iterable al final.
frutas.extend(["uva", "mango"])
print("extend:", frutas)

# insert(): inserta en una posición específica.
frutas.insert(1, "kiwi")
print("insert:", frutas)


# ============================================================
# 4. ELIMINAR ELEMENTOS
# ============================================================

print("\n4. Eliminar elementos")

# remove(): elimina la PRIMERA aparición del valor indicado.
frutas.remove("banana")
print("remove:", frutas)

# pop(): elimina y DEVUELVE el elemento en la posición indicada.
# Sin argumento, elimina el último.
ultima = frutas.pop()
print("pop() devolvió:", ultima)
print("Después de pop:", frutas)

# del: elimina por índice.
del frutas[0]
print("Después de del:", frutas)

# clear(): vacía la lista.
copia = frutas.copy()
copia.clear()
print("clear():", copia)


# ============================================================
# 5. BUSCAR Y CONTAR
# ============================================================

print("\n5. Búsqueda y conteo")

colores = ["rojo", "verde", "azul", "rojo", "amarillo"]

print("index('rojo'):", colores.index("rojo"))  # 0
print("count('rojo'):", colores.count("rojo"))  # 2

# El operador in comprueba si un valor existe.
print("'azul' in colores:", "azul" in colores)  # True

# index() lanza ValueError si el valor no existe.
# print(colores.index("morado"))


# ============================================================
# 6. ORDENAR Y REVERTIR
# ============================================================

print("\n6. Ordenamiento")

numeros = [5, 2, 8, 1, 9]

# sort(): ordena la lista EN SITIO (modifica la original) y devuelve None.
numeros.sort()
print("sort() ascendente:", numeros)

numeros.sort(reverse=True)
print("sort() descendente:", numeros)

# reverse(): invierte el orden actual en sitio.
numeros.reverse()
print("reverse():", numeros)

# sorted(): devuelve una NUEVA lista ordenada sin modificar la original.
otra = [3, 1, 4, 1, 5]
ordenada = sorted(otra)
print("Original:", otra)
print("sorted():", ordenada)


# ============================================================
# 7. COMPRENSIÓN DE LISTAS
# ============================================================

print("\n7. Comprensión de listas")

# Sintaxis: [expresion for elemento in iterable if condicion]
cuadrados = [n**2 for n in range(6)]
print("Cuadrados:", cuadrados)

pares = [n for n in range(10) if n % 2 == 0]
print("Pares:", pares)

# Equivalente con bucle:
pares_bucle = []
for n in range(10):
    if n % 2 == 0:
        pares_bucle.append(n)
print("Pares con bucle:", pares_bucle)


# ============================================================
# 8. COPIAR LISTAS: REFERENCIA VS. COPIA
# ============================================================

print("\n8. Copias")

original = [1, 2, 3]

# Asignación: NO crea copia, ambas variables apuntan a la misma lista.
referencia = original
referencia.append(4)
print("Original tras modificar referencia:", original)  # [1, 2, 3, 4]

# copy() o slicing crean una copia superficial.
original = [1, 2, 3]
copia = original.copy()
copia.append(4)
print("Original:", original)  # [1, 2, 3]
print("Copia:", copia)  # [1, 2, 3, 4]


# ============================================================
# 9. LISTAS ANIDADAS
# ============================================================

print("\n9. Listas anidadas")

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz[0][0])  # 1
print(matriz[1][2])  # 6

# Recorrer una matriz con bucles anidados.
for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print()


# ============================================================
# 10. RETOS PARA PRACTICAR
# ============================================================

# 1. Crea una lista con tus 5 películas favoritas.
# 2. Agrega una película al final con append().
# 3. Inserta una película al inicio con insert(0, ...).
# 4. Elimina una película por su valor con remove().
# 5. Ordena la lista alfabéticamente con sort().
# 6. Crea una nueva lista solo con las películas que empiecen
#    con la letra "A" usando comprensión de listas.
# 7. Crea una copia de la lista y modifícala sin afectar la original.
#
# Preguntas para comprobar tu comprensión:
# - ¿Qué diferencia hay entre append() y extend()?
# - ¿Qué devuelve pop()?
# - ¿Qué diferencia hay entre sort() y sorted()?
# - ¿Por qué una asignación simple no crea una copia?
# - ¿Cómo se accede al elemento en la fila 2, columna 3 de una matriz?

print("\n¡Fin de la guía de listas!")
