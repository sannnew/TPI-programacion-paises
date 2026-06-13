
# TPI - Gestión de Datos de Países
# Programación 1 - UTN


from constantes import *

from archivos import leer_csv

from consultas import (
    agregar_pais,
    actualizar_pais,
    buscar_pais,
    filtrar_paises,
    ordenar_paises
)

from estadistica import mostrar_estadisticas

from validaciones import mostrar_lista


paises = []

leer_csv(paises, NOMBRE_ARCHIVO)

opcion = 0

while opcion != OPCION_SALIR:

    try:

        opcion = int(input(MENU))

        if opcion not in range(1, OPCION_SALIR + 1):
            raise ValueError()

        if opcion == OPCION_AGREGAR:
            agregar_pais(paises)

        elif opcion == OPCION_ACTUALIZAR:
            actualizar_pais(paises)

        elif opcion == OPCION_BUSCAR:
            buscar_pais(paises)

        elif opcion == OPCION_FILTRAR:
            filtrar_paises(paises)

        elif opcion == OPCION_ORDENAR:
            ordenar_paises(paises)

        elif opcion == OPCION_ESTADISTICAS:
            mostrar_estadisticas(paises)

        elif opcion == OPCION_MOSTRAR_TODOS:
            print(TITULO_OP_7)
            mostrar_lista(paises)

    except ValueError:
        print(ERR_OPCION_INVALIDA)
        opcion = 0

print(TITULO_OP_8)
print("Gracias por usar el sistema de gestión de países. ¡Hasta luego!")
