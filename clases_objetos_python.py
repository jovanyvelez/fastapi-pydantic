"""
CLASES Y OBJETOS EN PYTHON: GUÍA PRÁCTICA
=========================================

Este archivo explica el concepto de clases y objetos con ejemplos sencillos.
Incluye atributos, métodos, __init__, self, crear objetos, modificar datos,
métodos con parámetros, valores de retorno, varios objetos, composición,
__str__ y una pequeña práctica final.

Cómo usarlo:
1. Guarda este archivo como clases_objetos_python.py.
2. Ejecútalo con:
       python clases_objetos_python.py
3. Lee los comentarios y prueba cambiar los ejemplos.

Idea principal:
- Una CLASE es como un plano o molde que define datos y comportamientos.
- Un OBJETO es una instancia concreta creada a partir de una clase.
- Los ATRIBUTOS guardan datos del objeto.
- Los MÉTODOS son funciones definidas dentro de una clase que describen
  comportamientos de sus objetos.
"""

# ============================================================
# 1. UNA PRIMERA CLASE
# ============================================================

# Creamos una clase llamada Perro.
# Por convención, los nombres de las clases comienzan con mayúscula.
class Perro:
    pass  # pass significa "no hacer nada"; sirve como cuerpo temporal.


# Crear un objeto (también llamado instancia) de la clase Perro.
mi_perro = Perro()

print("\n1. Primer objeto")
print(mi_perro)

# Python mostrará una representación técnica del objeto.
# Todavía no tiene datos ni comportamientos propios.


# ============================================================
# 2. ATRIBUTOS: DATOS DE UN OBJETO
# ============================================================

class PerroConNombre:
    pass


# Podemos agregar atributos después de crear el objeto.
mi_perro = PerroConNombre()
mi_perro.nombre = "Luna"
mi_perro.edad = 4

print("\n2. Atributos")
print(mi_perro.nombre)
print(mi_perro.edad)

# Aunque esto es posible, normalmente definimos los atributos dentro
# de __init__, para que cada objeto nazca con los datos que necesita.


# ============================================================
# 3. __init__ Y SELF
# ============================================================

class Perro:
    # __init__ se ejecuta al crear una nueva instancia.
    # self representa el objeto concreto que se está inicializando.
    # nombre y edad son datos que recibimos al crear el objeto.
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Al llamar Perro(...), Python crea el objeto y ejecuta __init__.
# No escribimos self en la llamada: Python lo pasa automáticamente.
perro1 = Perro("Luna", 4)
perro2 = Perro("Max", 7)

print("\n3. Objetos con sus propios atributos")
print(perro1.nombre, perro1.edad)
print(perro2.nombre, perro2.edad)

# perro1 y perro2 pertenecen a la misma clase, pero son objetos distintos.
# Cada uno tiene sus propios valores para nombre y edad.


# ============================================================
# 4. MÉTODOS: COMPORTAMIENTOS DE LOS OBJETOS
# ============================================================

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Un método es una función definida dentro de la clase.
    # self permite acceder a los atributos del objeto.
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")


perro1 = Perro("Luna", 4)
perro2 = Perro("Max", 7)

print("\n4. Métodos")
perro1.ladrar()
perro2.ladrar()

# Observa que llamamos perro1.ladrar(), no Perro.ladrar(perro1).
# Python pasa automáticamente el objeto como primer argumento (self).


# ============================================================
# 5. MÉTODOS QUE RECIBEN PARÁMETROS
# ============================================================

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self, cantidad=1):
        # Modificamos el atributo edad del objeto.
        self.edad += cantidad
        print(f"{self.nombre} ahora tiene {self.edad} años.")


perro = Perro("Luna", 4)

print("\n5. Método con parámetro")
perro.cumplir_anios()     # Suma un año porque cantidad vale 1 por defecto.
perro.cumplir_anios(2)    # Suma dos años más.


# ============================================================
# 6. MÉTODOS QUE DEVUELVEN UN VALOR CON RETURN
# ============================================================

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_inventario(self):
        # return entrega un resultado para que el código que llama
        # al método pueda guardarlo, imprimirlo o usarlo en un cálculo.
        return self.precio * self.cantidad


teclado = Producto("Teclado", 85000, 12)

print("\n6. Método con return")
valor = teclado.calcular_valor_inventario()
print(f"Valor del inventario de {teclado.nombre}: ${valor}")

# Diferencia:
# print(...) muestra algo en pantalla.
# return devuelve un valor al código que llamó al método.


# ============================================================
# 7. MODIFICAR ATRIBUTOS Y CONSULTAR SU ESTADO
# ============================================================

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def agregar_stock(self, unidades):
        self.cantidad += unidades

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad: {self.cantidad}")


producto = Producto("Ratón", 45000, 10)

print("\n7. Cambiar atributos mediante métodos")
producto.cambiar_precio(50000)
producto.agregar_stock(5)
producto.mostrar_informacion()

# También es posible escribir producto.precio = 50000 directamente.
# Los métodos permiten reunir reglas y operaciones relacionadas con el dato.
# Por ejemplo, más adelante cambiar_precio podría validar que el precio
# no sea negativo antes de guardar el nuevo valor.


# ============================================================
# 8. CADA OBJETO MANTIENE SUS PROPIOS DATOS
# ============================================================

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobar(self):
        return self.nota >= 3.0


estudiante1 = Estudiante("Laura", 4.5)
estudiante2 = Estudiante("Andrés", 2.8)

print("\n8. Objetos independientes")
print(estudiante1.nombre, estudiante1.nota, estudiante1.aprobar())
print(estudiante2.nombre, estudiante2.nota, estudiante2.aprobar())

# Cambiar estudiante1 no cambia los atributos de estudiante2.
estudiante1.nota = 4.8
print("Nueva nota de Laura:", estudiante1.nota)
print("Nota de Andrés:", estudiante2.nota)


# ============================================================
# 9. UNA CLASE QUE TRABAJA CON OTROS OBJETOS
# ============================================================

class Motor:
    def __init__(self, cilindrada):
        self.cilindrada = cilindrada

    def describir(self):
        return f"Motor de {self.cilindrada} cc"


class Motocicleta:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Este atributo guarda un objeto Motor.

    def mostrar_informacion(self):
        print(f"Motocicleta: {self.marca} {self.modelo}")
        print(self.motor.describir())


motor = Motor(150)
moto = Motocicleta("Honda", "CB150", motor)

print("\n9. Un objeto contiene otro objeto")
moto.mostrar_informacion()

# La motocicleta tiene un atributo motor que referencia un objeto Motor.
# Esta relación se conoce como composición o, de forma general, como
# una relación "tiene un" (una motocicleta tiene un motor).


# ============================================================
# 10. EL MÉTODO ESPECIAL __str__
# ============================================================

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        # __str__ define una representación legible del objeto.
        return f'"{self.titulo}", de {self.autor}'


libro = Libro("Cien años de soledad", "Gabriel García Márquez")

print("\n10. Representación legible")
print(libro)  # Python usa automáticamente __str__ al imprimir el objeto.


# ============================================================
# 11. ATRIBUTOS DE INSTANCIA Y ATRIBUTOS DE CLASE
# ============================================================

class Estudiante:
    # Este atributo pertenece a la clase y se comparte como valor común,
    # salvo que una instancia tenga un atributo del mismo nombre.
    institucion = "IE Ejemplo"

    def __init__(self, nombre):
        # Este atributo pertenece a cada instancia.
        self.nombre = nombre


alumna = Estudiante("Laura")
alumno = Estudiante("Andrés")

print("\n11. Atributos de clase e instancia")
print(alumna.nombre, alumna.institucion)
print(alumno.nombre, alumno.institucion)

# Cambiar el atributo en la clase afecta el valor común que consultan
# las instancias que no lo hayan sobrescrito.
Estudiante.institucion = "IE Nuevo Horizonte"
print(alumna.institucion)
print(alumno.institucion)

# Si escribimos alumna.institucion = "Otra institución", creamos/sobrescribimos
# un atributo en esa instancia, sin cambiar el atributo de la clase.


# ============================================================
# 12. EJEMPLO INTEGRADOR: PRODUCTOS
# ============================================================

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_inventario(self):
        return self.precio * self.cantidad

    def agregar_stock(self, unidades):
        if unidades > 0:
            self.cantidad += unidades
        else:
            print("Las unidades deben ser mayores que cero.")

    def vender(self, unidades):
        # Solo vendemos si la cantidad solicitada es positiva y hay stock.
        if unidades <= 0:
            print("La cantidad a vender debe ser mayor que cero.")
        elif unidades > self.cantidad:
            print("No hay suficiente inventario.")
        else:
            self.cantidad -= unidades
            print(f"Venta realizada: {unidades} unidad(es) de {self.nombre}.")

    def __str__(self):
        return (
            f"{self.codigo} - {self.nombre} | "
            f"Precio: ${self.precio} | Stock: {self.cantidad}"
        )


producto1 = Producto(101, "Teclado", 85000, 12)
producto2 = Producto(102, "Ratón", 45000, 20)

print("\n12. Ejemplo integrador")
print(producto1)
print(producto2)

producto1.agregar_stock(3)
producto2.vender(2)

print("\nInventario actualizado")
print(producto1)
print(producto2)
print(
    "Valor del inventario del teclado:",
    producto1.calcular_valor_inventario()
)


# ============================================================
# 13. RETOS PARA PRACTICAR
# ============================================================

# 1. Crea una clase llamada Persona con nombre y edad.
# 2. Crea dos objetos Persona con datos diferentes.
# 3. Agrega un método presentarse() que imprima un saludo con el nombre.
# 4. Agrega un método cumplir_anios() que aumente la edad en uno.
# 5. Crea una clase CuentaBancaria con titular y saldo.
# 6. Agrega un método depositar(cantidad) que aumente el saldo.
# 7. Agrega un método consultar_saldo() que devuelva el saldo con return.
#
# Preguntas para comprobar tu comprensión:
# - ¿Cuál es la diferencia entre una clase y un objeto?
# - ¿Qué representa self?
# - ¿Para qué sirve __init__?
# - ¿Qué diferencia hay entre print() y return?
# - ¿Por qué dos objetos de la misma clase pueden tener datos distintos?

print("\n¡Fin de la guía de clases y objetos!")
