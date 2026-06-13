# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**  
Tecnicatura Universitaria en Programación — Universidad Tecnológica Nacional

---

## Descripción

Sistema de gestión de información sobre países desarrollado en Python 3.
Permite cargar datos desde un archivo CSV y realizar consultas, filtros,
ordenamientos y estadísticas a través de un menú interactivo en consola.

---

## Integrantes

| Nombre    | Apellido  |
| --------- | --------- |
| Adalberto | Navas     |
|           |           |

---

## Estructura del proyecto

```
proyecto/
├── main.py              # Archivo principal con todas las funciones del sistema
├── constantes.py        # Constantes: menús, separadores, mensajes y datos iniciales
├── datos/
│   └── paises.csv       # Dataset de países (se crea automáticamente si no existe)
├── .gitignore           # Excluye __pycache__ y archivos .pyc del repositorio
└── README.md            # Este archivo
```

---

## Requisitos

- Python 3.x
- No requiere librerías externas

---

## Instrucciones de uso

**1. Clonar el repositorio:**

```bash
git clone [URL_DEL_REPOSITORIO]
cd [NOMBRE_DEL_PROYECTO]
```

**2. Ejecutar el programa:**

```bash
python main.py
```

El archivo `datos/paises.csv` se crea automáticamente con 4 países de ejemplo si no existe.

---

## Funcionalidades

| Opción | Descripción                                                           |
| ------ | --------------------------------------------------------------------- |
| 1      | Agregar un nuevo país                                                 |
| 2      | Actualizar población y superficie de un país existente                |
| 3      | Buscar país por nombre (coincidencia parcial o exacta)                |
| 4      | Filtrar por continente, rango de población o rango de superficie      |
| 5      | Ordenar por nombre, población o superficie (ascendente o descendente) |
| 6      | Mostrar estadísticas generales                                        |
| 7      | Mostrar todos los países                                              |
| 8      | Salir                                                                 |

---

## Ejemplos de uso

**Agregar un país:**

```
==================================================
         Opción 1 - Agregar país
==================================================
Nombre del país: España
Población: 47415750
Superficie (km²): 505990
Continente: Europa
País 'España' agregado correctamente.
```

**Buscar un país:**

```
==================================================
         Opción 3 - Buscar país
==================================================
Ingrese el nombre o parte del nombre a buscar: ar

2 resultado(s) encontrado(s):
------------------------------------------------------------------------
  Nombre                    Población      Superficie  Continente
------------------------------------------------------------------------
  Argentina                45,376,763       2,780,400  América
------------------------------------------------------------------------
```

**Filtrar por continente:**

```
==================================================
         Opción 4 - Filtrar países
==================================================
--------------------------------------------------
               Filtrar por
--------------------------------------------------
  1. Por continente
  2. Por rango de población
  3. Por rango de superficie
Seleccione una opción: 1
Ingrese el continente: América

Países en América:
------------------------------------------------------------------------
  Nombre                    Población      Superficie  Continente
------------------------------------------------------------------------
  Argentina                45,376,763       2,780,400  América
  Brasil                  213,993,437       8,515,767  América
------------------------------------------------------------------------
```

**Estadísticas:**

```
==================================================
         Opción 6 - Estadísticas
==================================================
--------------------------------------------
  Total de países      : 4
--------------------------------------------
  Mayor población      : Brasil (213,993,437 hab.)
  Menor población      : Alemania (83,149,300 hab.)
--------------------------------------------
  Promedio población   : 117,079,875 hab.
  Promedio superficie  : 3,007,791 km²
--------------------------------------------
  Países por continente:
    América             : 2
    Asia                : 1
    Europa              : 1
--------------------------------------------
```

---

## Formato del CSV

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

---

## Links


- **Video demostración:** [https://youtu.be/UMwC5_cdIC8]

