"""
DATACLASSES EN PYTHON: GUÍA PRÁCTICA
====================================

Este archivo explica cómo usar el decorador @dataclass para crear clases
de datos con menos código repetitivo.

Cómo usarlo:
1. Guarda este archivo como guia_dataclasses.py.
2. Ejecútalo con:
       python guia_dataclasses.py
3. Lee los comentarios y prueba cambiar los ejemplos.

Idea principal:
- Una dataclass genera automáticamente __init__, __repr__ y __eq__
  a partir de los campos anotados con tipos.
- Es ideal para clases que principalmente almacenan datos.
"""

from dataclasses import dataclass, field

# ============================================================
# 1. DATACLASS MÍNIMA
# ============================================================


@dataclass
class Punto:
    x: int
    y: int


p1 = Punto(3, 4)
p2 = Punto(3, 4)

print("\n1. Dataclass mínima")
print(p1)  # Punto(x=3, y=4)  ← __repr__ generado
print(p1 == p2)  # True              ← __eq__ generado
print(p1.x, p1.y)  # 3 4               ← __init__ generado

# Las anotaciones de tipo son obligatorias para que @dataclass reconozca
# los campos, aunque Python no las valida en tiempo de ejecución.
# Punto("hola", "mundo") también se construye sin error.


# ============================================================
# 2. VALORES POR DEFECTO Y field()
# ============================================================


@dataclass
class Estudiante:
    nombre: str
    nota: float = 0.0
    # Los valores mutables (listas, diccionarios) DEBEN usar
    # field(default_factory=...). Un [] directo genera ValueError.
    materias: list[str] = field(default_factory=list)


e1 = Estudiante("Laura", 4.5, ["Matemáticas", "Física"])
e2 = Estudiante("Andrés")

print("\n2. Valores por defecto")
print(e1)
print(e2)

# Cada instancia recibe su PROPIA lista vacía, no una lista compartida.
e2.materias.append("Química")
print("Materias de Andrés:", e2.materias)  # ['Química']
print("Materias de Laura:", e1.materias)  # ['Matemáticas', 'Física']


# ============================================================
# 3. __post_init__: CÁLCULOS DESPUÉS DE INICIALIZAR
# ============================================================


@dataclass
class Rectangulo:
    ancho: float
    alto: float
    area: float = field(init=False)  # No se pasa como argumento

    def __post_init__(self):
        # Se ejecuta automáticamente al final de __init__.
        # Ideal para calcular campos derivados o validar datos.
        self.area = self.ancho * self.alto


r = Rectangulo(5, 3)
print("\n3. __post_init__")
print(r)
print("Área:", r.area)  # 15


# ============================================================
# 4. INMUTABILIDAD CON frozen=True
# ============================================================


@dataclass(frozen=True)
class Configuracion:
    host: str
    puerto: int
    debug: bool = False


cfg = Configuracion("localhost", 8080)

print("\n4. Dataclass inmutable")
print(cfg)

# Descomenta la siguiente línea para ver el error:
# cfg.puerto = 9090
# → dataclasses.FrozenInstanceError

# frozen=True también hace que la instancia sea hashable y pueda
# usarse como clave de diccionario o elemento de un set.
configuraciones = {cfg: "desarrollo"}
print("Hashable:", cfg in configuraciones)  # True

# Si necesitas modificar un campo dentro de __post_init__ en una
# dataclass frozen, usa object.__setattr__(self, "campo", valor).


# ============================================================
# 5. ORDENAMIENTO CON order=True
# ============================================================


@dataclass(order=True)
class Version:
    mayor: int
    menor: int
    parche: int = 0


versiones = [
    Version(2, 1, 0),
    Version(1, 9, 5),
    Version(2, 0, 3),
]

print("\n5. Ordenamiento automático")
for v in sorted(versiones):
    print(v)

# order=True genera __lt__, __le__, __gt__ y __ge__ comparando
# los campos en el orden en que fueron declarados.


# ============================================================
# 6. MÉTODOS PROPIOS EN UNA DATACLASS
# ============================================================


@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int = 0

    def valor_inventario(self):
        return self.precio * self.cantidad

    def vender(self, unidades: int):
        if unidades <= self.cantidad:
            self.cantidad -= unidades
            print(f"Venta: {unidades} unidad(es) de {self.nombre}")
        else:
            print("Stock insuficiente.")


prod = Producto("Teclado", 85000, 10)
print("\n6. Métodos propios")
print("Valor inventario:", prod.valor_inventario())
prod.vender(3)
print(prod)


# ============================================================
# 7. slots=True (PYTHON 3.10+)
# ============================================================


@dataclass(slots=True)
class PuntoLigero:
    x: float
    y: float


pl = PuntoLigero(1.0, 2.0)
print("\n7. slots=True")
print(pl)

# slots=True reduce el uso de memoria por instancia y acelera el
# acceso a atributos, pero impide agregar atributos nuevos fuera
# de los declarados.

# Descomenta para ver el error:
# pl.z = 3.0   # AttributeError


# ============================================================
# 8. RETOS PARA PRACTICAR
# ============================================================

# 1. Crea una dataclass llamada Libro con titulo, autor y anio.
# 2. Agrega un campo paginas con valor por defecto 0.
# 3. Usa field(default_factory=list) para un campo etiquetas.
# 4. Agrega un método __post_init__ que calcule una propiedad
#    "es_largo" (True si paginas > 300).
# 5. Crea una dataclass frozen llamada Coordenada.
# 6. Ordena una lista de dataclasses Version con order=True.
#
# Preguntas para comprobar tu comprensión:
# - ¿Qué métodos genera automáticamente @dataclass?
# - ¿Por qué los valores mutables requieren default_factory?
# - ¿Para qué sirve __post_init__?
# - ¿Qué efecto tiene frozen=True?
# - ¿Cuándo usarías slots=True?

print("\n¡Fin de la guía de dataclasses!")
