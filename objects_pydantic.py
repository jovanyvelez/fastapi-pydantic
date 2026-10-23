"""
PYDANTIC V2: GUÍA PRÁCTICA
==========================

Este archivo explica cómo definir modelos de datos con validación
automática usando Pydantic v2.

Requisito:
    pip install pydantic>=2.0

Cómo usarlo:
1. Guarda este archivo como guia_pydantic.py.
2. Ejecútalo con:
       python guia_pydantic.py

Idea principal:
- Un modelo Pydantic hereda de BaseModel.
- Los campos se declaran con anotaciones de tipo.
- Pydantic valida, convierte y serializa datos automáticamente.
"""

from typing import Self

from pydantic import BaseModel, Field, field_validator, model_validator

# ============================================================
# 1. MODELO MÍNIMO
# ============================================================


class Articulo(BaseModel):
    titulo: str
    cuerpo: str
    vistas: int = 0


articulo = Articulo(titulo="Hola", cuerpo="mundo", vistas=3)

print("\n1. Modelo mínimo")
print(articulo)
print(type(articulo.vistas))  # <class 'int'>

# Pydantic convierte tipos compatibles automáticamente.
# "3" → 3 es aceptado por defecto; "tres" → int lanza ValidationError.


# ============================================================
# 2. VALIDACIÓN DESDE DICCIONARIO O JSON
# ============================================================

datos = {"titulo": "Pydantic", "cuerpo": "validación", "vistas": "42"}

art2 = Articulo.model_validate(datos)
print("\n2. model_validate")
print(art2)
print("Vistas convertidas a int:", art2.vistas, type(art2.vistas))

json_str = '{"titulo": "JSON", "cuerpo": "string", "vistas": 10}'
art3 = Articulo.model_validate_json(json_str)
print("Desde JSON:", art3)

# Si un campo falta o tiene un tipo incompatible, Pydantic lanza
# ValidationError con la lista completa de errores.

# Descomenta para ver el error:
# Articulo(titulo="Sin cuerpo")   # falta cuerpo


# ============================================================
# 3. VALORES POR DEFECTO Y OPCIONALES
# ============================================================


class Usuario(BaseModel):
    nombre: str
    edad: int | None = None  # Opcional, por defecto None
    activo: bool = True  # Valor por defecto


u1 = Usuario(nombre="Laura")
u2 = Usuario(nombre="Andrés", edad=30, activo=False)

print("\n3. Campos opcionales y defaults")
print(u1)
print(u2)


# ============================================================
# 4. RESTRICCIONES CON Field()
# ============================================================


class Producto(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)
    precio: float = Field(gt=0, description="Precio en pesos")
    cantidad: int = Field(default=0, ge=0, description="Stock no negativo")
    codigo: str = Field(pattern=r"^[A-Z]{2}-\d{3}$")


prod = Producto(nombre="Teclado", precio=85000, cantidad=10, codigo="TE-123")

print("\n4. Field() con restricciones")
print(prod)

# Descomenta para ver errores de validación:
# Producto(nombre="", precio=-1, cantidad=-5, codigo="abc")


# ============================================================
# 5. VALIDADORES DE CAMPO: field_validator
# ============================================================


class Correo(BaseModel):
    direccion: str

    @field_validator("direccion")
    @classmethod
    def validar_arroba(cls, valor: str) -> str:
        if "@" not in valor:
            raise ValueError("El correo debe contener @")
        return valor.strip().lower()


c = Correo(direccion="  LAURA@EJEMPLO.COM  ")
print("\n5. field_validator")
print(c.direccion)  # laura@ejemplo.com

# field_validator se ejecuta después de la validación de tipo.
# Para ejecutarlo antes, usa mode="before".


# ============================================================
# 6. VALIDADORES DE MODELO: model_validator
# ============================================================


class RangoFechas(BaseModel):
    inicio: int
    fin: int

    @model_validator(mode="after")
    def validar_rango(self) -> Self:
        if self.fin <= self.inicio:
            raise ValueError("fin debe ser mayor que inicio")
        return self


rango = RangoFechas(inicio=1, fin=10)
print("\n6. model_validator")
print(rango)

# Descomenta para ver el error:
# RangoFechas(inicio=10, fin=5)


# ============================================================
# 7. SERIALIZACIÓN CON model_dump()
# ============================================================


class Direccion(BaseModel):
    ciudad: str
    pais: str = "Colombia"


class Persona(BaseModel):
    nombre: str
    direccion: Direccion


persona = Persona(nombre="Laura", direccion=Direccion(ciudad="Medellín"))

print("\n7. Serialización")
print(persona.model_dump())
# {'nombre': 'Laura', 'direccion': {'ciudad': 'Medellín', 'pais': 'Colombia'}}

print(persona.model_dump_json())
# {"nombre":"Laura","direccion":{"ciudad":"Medellín","pais":"Colombia"}}

# model_dump() produce un diccionario.
# model_dump_json() produce una cadena JSON.


# ============================================================
# 8. MODELOS ANIDADOS
# ============================================================


class Motor(BaseModel):
    cilindrada: int


class Moto(BaseModel):
    marca: str
    motor: Motor


moto = Moto(marca="Honda", motor={"cilindrada": 150})
print("\n8. Modelo anidado")
print(moto)
print("Cilindrada:", moto.motor.cilindrada)


# ============================================================
# 9. CONFIGURACIÓN DEL MODELO (model_config)
# ============================================================

from pydantic import ConfigDict


class UsuarioEstricto(BaseModel):
    model_config = ConfigDict(strict=True)

    nombre: str
    edad: int


# Con strict=True, "30" no se convierte a 30.
# Descomenta para ver el error:
# UsuarioEstricto(nombre="Laura", edad="30")


class UsuarioDesdeORM(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str
    edad: int


# from_attributes=True permite crear el modelo desde objetos
# que tienen atributos (por ejemplo, resultados de un ORM).


# ============================================================
# 10. RETOS PARA PRACTICAR
# ============================================================

# 1. Crea un modelo llamado Tarea con titulo, completada (bool)
#    y prioridad (int entre 1 y 5 usando Field).
# 2. Agrega un field_validator que rechace títulos vacíos.
# 3. Crea un modelo Cuenta con titular y saldo, y un
#    model_validator que impida saldo negativo.
# 4. Serializa un modelo anidado con model_dump().
# 5. Usa model_validate_json() para crear un modelo desde
#    una cadena JSON.
#
# Preguntas para comprobar tu comprensión:
# - ¿Qué diferencia hay entre field_validator y model_validator?
# - ¿Para qué sirve Field()?
# - ¿Qué hace model_validate() frente a model_dump()?
# - ¿Cuándo usarías strict=True?
# - ¿Qué ventaja ofrece from_attributes=True?

print("\n¡Fin de la guía de Pydantic v2!")
