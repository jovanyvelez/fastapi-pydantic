# Guías de Python para trabajar con un ORM

> Ruta de aprendizaje: **Python básico → POO → Dataclasses → Pydantic v2 → FastAPI + ORM**

Este repositorio reúne **cinco guías prácticas y ejecutables** que construyen, paso a paso, las bases
necesarias para trabajar con comodidad con un **ORM** (SQLAlchemy, SQLModel, Tortoise ORM, Django ORM…)
y, en la capa de la API, con **FastAPI + Pydantic v2**.

Todos los ejemplos son autocontenidos, están comentados línea a línea y terminan con una sección de
**retos para practicar** y **preguntas de repaso**.

---

## Índice

1. [¿Por qué estas guías son necesarias para trabajar con un ORM?](#por-qué-estas-guías-son-necesarias-para-trabajar-con-un-orm)
2. [Contenido de las guías](#contenido-de-las-guías)
3. [Ruta de aprendizaje recomendada](#ruta-de-aprendizaje-recomendada)
4. [Requisitos e instalación](#requisitos-e-instalación)
5. [Cómo ejecutar las guías](#cómo-ejecutar-las-guías)
6. [Retos y ejercicios](#retos-y-ejercicios)
7. [Próximos pasos](#próximos-pasos)
8. [Convenciones de los archivos](#convenciones-de-los-archivos)

---

## ¿Por qué estas guías son necesarias para trabajar con un ORM?

Un ORM no devuelve filas crudas de SQL: **devuelve objetos**. Cada registro de la base de datos se
convierte en una instancia de una clase mapeada, y cada consulta devuelve colecciones de esas
instancias. Escribir la primera aplicación con un ORM sin estas bases produce errores
conceptuales, no solo errores de sintaxis.

Estas guías cubren exactamente esas bases:

| Guía | Qué aporta al trabajo con un ORM |
|---|---|
| [`lista.py`](lista.py) | Las consultas del ORM devuelven **colecciones** ordenadas. Necesitas saber iterar, filtrar, ordenar, paginar (`limit`/`offset` se expresan como *slicing*) y distinguir `sort()` (en sitio) de `sorted()` (copia). |
| [`diccionario.py`](diccionario.py) | Los filtros del ORM se expresan como pares **clave = valor** (`filter_by(nombre="Luna")`). Aquí se aprenden pares clave/valor, `get()` con valor por defecto, `items()`, `in` para comprobar existencia y estructuras anidadas. |
| [`clases_objetos_python.py`](clases_objetos_python.py) | Una **clase mapeada** es, en el fondo, una clase de Python: `__init__`, `self`, atributos de instancia vs. de clase, `__str__` y relaciones de composición ("tiene un" / "tiene muchos"). |
| [`objects_dataclass.py`](objects_dataclass.py) | Las **entidades y DTOs** del dominio son clases que sobre todo almacenan datos. `@dataclass` genera `__init__`, `__repr__` y `__eq__` automáticamente, con campos derivados, inmutabilidad y `slots`. |
| [`objects_pydantic.py`](objects_pydantic.py) | Los **schemas de la API** (lo que entra y lo que sale por HTTP) se modelan con Pydantic. Es la capa que conecta el ORM con FastAPI: validación, serialización y `from_attributes=True` para construir un schema desde una fila del ORM. |

### El puente ORM ↔ Pydantic

Este repositorio no es solo teoría: la sección 9 de
[`objects_pydantic.py`](objects_pydantic.py) introduce `ConfigDict(from_attributes=True)`, la pieza
exacta que permite algo como esto:

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel, ConfigDict


class Base(DeclarativeBase):
    pass


class Producto(Base):                      # Entidad mapeada (ORM)
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str]
    precio: Mapped[float]


class ProductoOut(BaseModel):              # Schema de respuesta (API)
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    precio: float


# La fila del ORM se convierte en schema sin dict() ni .copy():
# producto = session.get(Producto, 1)
# ProductoOut.model_validate(producto)
```

Ese `model_validate(objeto_orm)` **no es posible sin Pydantic**, y el objeto ORM **no existiría sin
las clases y objetos** que se estudian en `clases_objetos_python.py`.

---

## Contenido de las guías

### 1. `lista.py` — Listas en Python

Colecciones ordenadas y mutables: la base de toda lista que devuelve un `SELECT`.

1. Crear una lista (incluye `list(range(...))`)
2. Índices y slicing (`lista[inicio:fin:paso]`, índices negativos)
3. Agregar elementos: `append()`, `extend()`, `insert()`
4. Eliminar elementos: `remove()`, `pop()`, `del`, `clear()`
5. Buscar y contar: `index()`, `count()`, operador `in`
6. Ordenar y revertir: `sort()`, `reverse()`, `sorted()`
7. Comprensión de listas (`[expr for x in it if cond]`)
8. Copiar listas: referencia vs. copia superficial
9. Listas anidadas y recorrido con bucles anidados
10. **Retos para practicar** + preguntas de repaso

### 2. `diccionario.py` — Diccionarios en Python

Pares clave/valor: la estructura con la que el ORM expresa filtros y datos de una fila.

1. Crear un diccionario
2. Consultar valores: `dic[clave]`, `KeyError` vs. `get()` con valor por defecto
3. Recorrer con `for`: `keys()`, `values()`, `items()`
4. Agregar elementos (asignación y `update()`)
5. Modificar valores existentes (incluido cálculo a partir del valor anterior)
6. Eliminar elementos: `del`, `pop()`, `clear()`
7. Cambiar el nombre de una clave (`pop()` + asignación)
8. Comprobar si una clave existe: `in`, `not in`
9. Copiar un diccionario: asignación vs. `copy()` (copia superficial)
10. Diccionarios con listas y diccionarios anidados
11. **Ejemplo integrador: CRUD de productos** (Create, Read, Update, Delete)
12. **Retos para practicar** + preguntas de repaso

### 3. `clases_objetos_python.py` — Clases y objetos en Python

La base conceptual de una entidad mapeada: atributos, comportamiento y relaciones.

1. Una primera clase
2. Atributos: datos de un objeto
3. `__init__` y `self`
4. Métodos: comportamientos de los objetos
5. Métodos que reciben parámetros (valores por defecto)
6. Métodos que devuelven un valor con `return` (vs. `print`)
7. Modificar atributos y consultar su estado
8. Cada objeto mantiene sus propios datos
9. Una clase que trabaja con otros objetos — **composición / relación "tiene un"**
10. El método especial `__str__`
11. Atributos de instancia y atributos de clase
12. **Ejemplo integrador: productos** (con validaciones de stock)
13. **Retos para practicar** + preguntas de repaso

### 4. `objects_dataclass.py` — Dataclasses en Python

Clases de datos con menos código repetitivo: la base de entidades y DTOs del dominio.

1. Dataclass mínima (`__init__`, `__repr__` y `__eq__` generados)
2. Valores por defecto y `field(default_factory=...)`
3. `__post_init__`: cálculos y validaciones después de inicializar
4. Inmutabilidad con `frozen=True` (y `hashable`)
5. Ordenamiento automático con `order=True`
6. Métodos propios en una dataclass
7. `slots=True` (Python 3.10+): menos memoria, sin atributos dinámicos
8. **Retos para practicar** + preguntas de repaso

### 5. `objects_pydantic.py` — Pydantic v2

Modelos con validación automática: la capa que conecta el ORM con la API.

1. Modelo mínimo (`BaseModel` y anotaciones de tipo)
2. Validación desde diccionario o JSON (`model_validate`, `model_validate_json`)
3. Valores por defecto y opcionales (`int | None = None`)
4. Restricciones con `Field()` (`min_length`, `gt`, `ge`, `pattern`)
5. Validadores de campo: `@field_validator`
6. Validadores de modelo: `@model_validator`
7. Serialización con `model_dump()` y `model_dump_json()`
8. Modelos anidados
9. Configuración del modelo: `model_config` con `strict=True` y `from_attributes=True`
10. **Retos para practicar** + preguntas de repaso

---

## Ruta de aprendizaje recomendada

```
lista.py                    →  cómo se recorren y filtran colecciones
   ↓
diccionario.py               →  cómo se expresan los filtros y los datos de una fila
   ↓
clases_objetos_python.py     →  qué es una entidad, un atributo y una relación
   ↓
objects_dataclass.py        →  cómo escribir clases de datos con lo mínimo
   ↓
objects_pydantic.py          →  cómo validar y serializar hacia/desde la API
   ↓
FastAPI + ORM (Siguiente)    →  endpoints que leen y escriben en la base de datos
```

Se recomienda **no saltar pasos**: `objects_pydantic.py` da por sentado que se sabe lo que es una
clase y un objeto, y `objects_dataclass.py` da por sentado que se saben las colecciones básicas.

---

## Requisitos e instalación

| Requisito | Versión | Motivo |
|---|---|---|
| Python | **3.11+** | `from typing import Self` (usado en `objects_pydantic.py`) y `slots=True` en dataclasses (3.10+) |
| Pydantic | **v2** (`>=2.0`) | Requisito de `objects_pydantic.py` |

Las cuatro primeras guías usan **solo la biblioteca estándar**: se ejecutan sin instalar nada.

Instalación de Pydantic con `uv` (recomendado):

```bash
uv venv
uv pip install "pydantic>=2.0"
```

O con `pip`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install "pydantic>=2.0"
```

---

## Cómo ejecutar las guías

Cada archivo es un script autónomo que imprime los ejemplos por secciones.

```bash
# Guías sin dependencias externas
python lista.py
python diccionario.py
python clases_objetos_python.py
python objects_dataclass.py

# Guía con Pydantic v2 (requiere el venv activo)
python objects_pydantic.py
```

La salida de cada guía está numerada por secciones, de modo que se puede seguir el hilo de la
explicación en la terminal mientras se lee el código.

**Para practicar:** lo ideal es copiar una sección a un archivo aparte, modificarla y ejecutarla por
separado, sin tocar los ejemplos originales.

---

## Retos y ejercicios

Cada guía cierra con retos propuestos y preguntas de repaso. Resumen de los retos principales:

- **Listas:** construir una lista de películas, agregar e insertar, eliminar, ordenar y filtrar por
  letra inicial con comprensión de listas.
- **Diccionarios:** crear un diccionario personal, recorrerlo con `items()`, agregar y eliminar
  claves, renombrar una clave sin perder su valor.
- **Clases y objetos:** modelo `Persona` con `presentarse()` y `cumplir_anios()`, y clase
  `CuentaBancaria` con `depositar()` y `consultar_saldo()`.
- **Dataclasses:** `Libro` con campo `paginas` por defecto, `etiquetas` con `default_factory`, campo
  derivado `es_largo` en `__post_init__`, y dataclass `frozen` para `Coordenada`.
- **Pydantic:** modelo `Tarea` con `Field(ge=1, le=5)`, validador que rechaza títulos vacíos, y
  modelo `Cuenta` con `model_validator` que impide saldo negativo.

---

## Próximos pasos

Cuando las cinco guías estén dominadas, el siguiente paso natural es la **capa web**:

1. **FastAPI + Pydantic** — declarar `response_model` y usar los schemas de
   `objects_pydantic.py` como contrato de la API.
2. **SQLAlchemy 2.0 (ORM)** — `DeclarativeBase`, `Mapped[]`, `mapped_column()`, `Session` y
   consultas con `select()` / `filter_by()`, apoyándose en los conceptos de
   `clases_objetos_python.py`.
3. **Modelos anidados y relaciones** — `relationship()` para "tiene uno" y "tiene muchos",
   reutilizando la composición vista en la sección 9 de la guía de clases.
4. **Pydantic ↔ ORM** — `from_attributes=True` para serializar entidades del ORM
   directamente como respuestas de la API.
5. **CRUD completo** — llevar el CRUD de productos de `diccionario.py` a endpoints HTTP con
   persistencia real.

---

## Convenciones de los archivos

- Los archivos se numeran con `print("\nN. Título")` para que la salida en consola siga el mismo
  orden que el código.
- Cada archivo abre con una **docstring** que resume el objetivo y explica cómo usarlo.
- Los comentarios explican el *porqué*; el código muestra el *qué*.
- Las líneas que producen un error están comentadas con una nota (`# Descomenta para ver el error`),
  para que el lector pueda provocarlas a voluntad.
- Cada guía termina con **retos para practicar** y **preguntas de repaso**.

> **Nota:** las docstrings de los archivos mencionan nombres como `guia_listas.py` o
> `guia_dataclasses.py`, pero en el repositorio los archivos se llaman `lista.py`,
> `objects_dataclass.py`, etc. Se conserva el nombre real de cada archivo al ejecutarlos.
