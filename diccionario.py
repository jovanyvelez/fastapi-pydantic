"""
DICCIONARIOS EN PYTHON: GUÍA PRÁCTICA
====================================

Este archivo reúne ejemplos de creación, consulta, recorrido, modificación,
eliminación y otras operaciones con diccionarios.

Cómo usarlo:
1. Guarda este archivo como diccionarios_python.py.
2. Ejecútalo con Python:
       python diccionarios_python.py
3. Lee los comentarios y ejecuta los ejemplos por secciones.

Nota:
- Las líneas que empiezan con # son comentarios: explican el código.
- Las cadenas entre triple comilla, como esta, son docstrings.
"""

# ============================================================
# 1. CREAR UN DICCIONARIO
# ============================================================

# Un diccionario guarda parejas de clave y valor.
# Se escribe entre llaves {}, separando las parejas con comas.
producto = {
    "nombre": "Teclado",
    "precio": 85000,
    "cantidad": 12
}

print("\n1. Diccionario inicial")
print(producto)


# ============================================================
# 2. CONSULTAR VALORES
# ============================================================

# Para consultar un valor, escribe la clave entre corchetes.
print("\n2. Consultar valores")
print(producto["nombre"])  # Teclado
print(producto["precio"])  # 85000

# Si la clave no existe, los corchetes generan un KeyError.
# print(producto["marca"])  # Descomenta para probar el error.

# get() permite consultar sin generar un error si la clave no existe.
print(producto.get("marca"))  # None

# También podemos indicar un valor predeterminado.
print(producto.get("marca", "Sin marca"))  # Sin marca


# ============================================================
# 3. RECORRER UN DICCIONARIO CON FOR
# ============================================================

# Recorrer las claves. Escribir "for clave in producto" también
# recorre las claves; keys() lo hace explícito.
print("\n3A. Claves")
for clave in producto.keys():
    print(clave)

# Recorrer solamente los valores.
print("\n3B. Valores")
for valor in producto.values():
    print(valor)

# items() permite obtener la clave y el valor en cada vuelta.
print("\n3C. Claves y valores")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")


# ============================================================
# 4. AGREGAR ELEMENTOS
# ============================================================

# Si asignamos un valor a una clave que no existe, la agregamos.
producto["marca"] = "Logitech"
producto["disponible"] = True

print("\n4. Después de agregar claves")
print(producto)

# update() agrega o modifica varias parejas en una sola operación.
producto.update({
    "color": "negro",
    "garantia_meses": 12
})

print(producto)


# ============================================================
# 5. MODIFICAR VALORES EXISTENTES
# ============================================================

# La misma asignación sirve para agregar y para modificar.
# Si la clave ya existe, se reemplaza su valor.
producto["precio"] = 95000
producto["cantidad"] = 20

# También podemos calcular un nuevo valor a partir del anterior.
producto["cantidad"] += 5  # Suma 5 a la cantidad actual.

print("\n5. Después de modificar")
print(producto)  # La cantidad queda en 25.


# ============================================================
# 6. ELIMINAR ELEMENTOS
# ============================================================

# del elimina una pareja mediante su clave.
# Genera KeyError si la clave no existe.
del producto["color"]

# pop() elimina una pareja y devuelve el valor que tenía.
precio_eliminado = producto.pop("precio")
print("\n6. Precio eliminado:", precio_eliminado)

# Si la clave podría no existir, podemos indicar un valor predeterminado.
descuento_eliminado = producto.pop("descuento", None)
print("Descuento eliminado:", descuento_eliminado)

# clear() elimina todas las parejas y deja el diccionario vacío.
# No lo ejecutamos sobre producto porque seguiremos usándolo.
ejemplo_vacio = {"a": 1, "b": 2}
ejemplo_vacio.clear()
print("Diccionario después de clear():", ejemplo_vacio)  # {}


# ============================================================
# 7. CAMBIAR EL NOMBRE DE UNA CLAVE
# ============================================================

# No hay una operación directa para renombrar una clave.
# Podemos extraer el valor con pop() y asignarlo a la nueva clave.
# Atención: si la nueva clave ya existe, su valor será reemplazado.
producto["nombre_producto"] = producto.pop("nombre")

print("\n7. Después de cambiar el nombre de la clave")
print(producto)


# ============================================================
# 8. COMPROBAR SI UNA CLAVE EXISTE
# ============================================================

# El operador in comprueba si una clave existe.
if "marca" in producto:
    print("\n8. El producto tiene una marca registrada")

# not in comprueba que una clave no exista.
if "descuento" not in producto:
    producto["descuento"] = 0

print("Descuento:", producto["descuento"])

# in sobre el diccionario busca claves, no valores.
print("¿Existe la clave 'marca'?", "marca" in producto)
print("¿Existe el valor 85000?", 85000 in producto.values())


# ============================================================
# 9. COPIAR UN DICCIONARIO
# ============================================================

original = {"nombre": "Teclado"}

# Esta asignación NO crea una copia: ambas variables apuntan al mismo
# diccionario. Cambiar una afecta lo que vemos desde la otra.
referencia = original
referencia["nombre"] = "Ratón"
print("\n9A. Original tras modificar la referencia:", original)
# Resultado: {'nombre': 'Ratón'}

# copy() crea una copia superficial independiente en este ejemplo.
original = {"nombre": "Teclado"}
copia = original.copy()
copia["nombre"] = "Ratón"

print("9B. Original:", original)  # {'nombre': 'Teclado'}
print("9B. Copia:", copia)       # {'nombre': 'Ratón'}

# Importante: copy() es una copia superficial. Si el diccionario contiene
# listas u otros diccionarios, esos objetos internos pueden seguir compartidos.


# ============================================================
# 10. DICCIONARIOS CON LISTAS Y OTROS DICCIONARIOS
# ============================================================

estudiante = {
    "nombre": "Laura",
    "edad": 16,
    "notas": [4.2, 3.8, 4.5],
    "direccion": {
        "ciudad": "Medellín",
        "barrio": "Buenos Aires"
    }
}

# Para acceder a una lista dentro del diccionario, usamos su clave
# y luego el índice de la lista. Los índices empiezan en cero.
print("\n10. Primera nota:", estudiante["notas"][0])  # 4.2

# Podemos modificar un elemento de esa lista.
estudiante["notas"][1] = 4.0

# Para acceder a un diccionario dentro de otro, encadenamos las claves.
print("Ciudad:", estudiante["direccion"]["ciudad"])

# También podemos modificar el dato anidado.
estudiante["direccion"]["ciudad"] = "Bello"
print("Nueva ciudad:", estudiante["direccion"]["ciudad"])


# ============================================================
# 11. EJEMPLO INTEGRADOR: CRUD DE PRODUCTOS
# ============================================================

# CRUD significa:
# Create: crear un registro.
# Read: consultar registros.
# Update: modificar un registro.
# Delete: eliminar un registro.
#
# Aquí cada clave es un código de producto y cada valor es otro
# diccionario con los datos del producto.

productos = {
    101: {"nombre": "Teclado", "precio": 85000},
    102: {"nombre": "Ratón", "precio": 45000},
    103: {"nombre": "Monitor", "precio": 650000}
}

# READ: consultar todos los productos.
print("\n11A. Lista de productos")
for codigo, datos in productos.items():
    print(f"{codigo}: {datos['nombre']} - ${datos['precio']}")

# CREATE: agregar un producto nuevo.
# Antes de usar esta asignación, asegúrate de que el código no exista,
# porque si existe, se reemplazará el registro anterior.
if 104 not in productos:
    productos[104] = {"nombre": "Audífonos", "precio": 70000}

# UPDATE: modificar el precio del producto con código 102.
if 102 in productos:
    productos[102]["precio"] = 50000

# DELETE: eliminar el producto con código 103.
# pop(103, None) no genera error si ese código no existe.
productos.pop(103, None)

print("\n11B. Productos después de las operaciones")
for codigo, datos in productos.items():
    print(f"{codigo}: {datos['nombre']} - ${datos['precio']}")


# ============================================================
# 12. RETOS PARA PRACTICAR
# ============================================================

# Intenta resolver estos retos antes de consultar una solución:
#
# 1. Crea un diccionario con tu nombre, edad y ciudad.
# 2. Imprime todas sus claves usando un for.
# 3. Imprime cada clave y valor usando items().
# 4. Agrega una clave llamada "profesion".
# 5. Modifica la ciudad y elimina la clave "edad".
# 6. Cambia el nombre de una clave sin perder su valor.
#
# Consejo: puedes copiar una sección, modificarla y ejecutarla
# por separado para experimentar sin alterar los otros ejemplos.

print("\n¡Fin de la guía de diccionarios!")
