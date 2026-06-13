from constantes import *

from validaciones import (
    validar_nombre,
    validar_numero_positivo,
    buscar_pais_por_nombre,
    normalizar,
    mostrar_lista,
    lista_vacia,
)

from archivos import guardar_csv


def agregar_pais(paises):

    print(TITULO_OP_1)

    try:

        nombre = input("Nombre del país: ")
        validar_nombre(paises, nombre)

        poblacion = validar_numero_positivo(input("Población: "))
        superficie = validar_numero_positivo(input("Superficie (km²): "))

        continente = input("Continente: ").strip()

        if continente == "":
            raise ValueError(ERR_CONTINENTE_VACIO)

        paises.append(
            {
                "nombre": nombre.strip(),
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente,
            }
        )

        guardar_csv(paises, NOMBRE_ARCHIVO)

        print(f"País '{nombre.strip()}' agregado correctamente.")

    except ValueError as e:
        print(f"{e}\n{VOLVER}")


def actualizar_pais(paises):

    print(TITULO_OP_2)

    nombre = input("Nombre del país a actualizar: ")

    pais = buscar_pais_por_nombre(paises, nombre)

    if pais is None:
        print(ERR_PAIS_NO_EXISTE.format(nombre.strip()))
        return

    print(f"\nDatos actuales de {pais['nombre']}:")
    print(f"  Población  : {pais['poblacion']:,}")
    print(f"  Superficie : {pais['superficie']:,} km²")

    try:

        pais["poblacion"] = validar_numero_positivo(
            input("Nueva población: ")
        )

        pais["superficie"] = validar_numero_positivo(
            input("Nueva superficie (km²): ")
        )

        guardar_csv(paises, NOMBRE_ARCHIVO)

        print(f"País '{pais['nombre']}' actualizado correctamente.")

    except ValueError as e:
        print(f"{e}\n{VOLVER}")


def buscar_pais(paises):

    print(TITULO_OP_3)

    if lista_vacia(paises):
        return

    try:

        termino = input(
            "Ingrese el nombre o parte del nombre a buscar: "
        ).strip()

        if termino == "":
            raise ValueError(ERR_TERMINO_VACIO)

        resultados = []

        for pais in paises:

            if normalizar(termino) in normalizar(pais["nombre"]):
                resultados.append(pais)

        if len(resultados) == 0:
            print(MSG_SIN_RESULTADOS)

        else:
            print(f"\n{len(resultados)} resultado(s) encontrado(s):")
            mostrar_lista(resultados)

    except ValueError as e:
        print(f"{e}\n{VOLVER}")


def filtrar_paises(paises):

    print(TITULO_OP_4)

    if lista_vacia(paises):
        return

    try:

        opcion = int(input(MENU_FILTROS))

        if opcion not in range(1, 4):
            raise ValueError(ERR_OPCION_INVALIDA)

        resultados = []

        if opcion == 1:

            continente = input("Ingrese el continente: ").strip()

            if continente == "":
                raise ValueError(ERR_CONTINENTE_VACIO)

            for pais in paises:

                if normalizar(pais["continente"]) == normalizar(continente):
                    resultados.append(pais)

            print(f"\nPaíses en {continente}:")

        elif opcion == 2:

            minimo = validar_numero_positivo(input("Mínimo: "))
            maximo = validar_numero_positivo(input("Máximo: "))

            if minimo > maximo:
                raise ValueError(ERR_RANGO_INVALIDO)

            for pais in paises:

                if minimo <= pais["poblacion"] <= maximo:
                    resultados.append(pais)

        elif opcion == 3:

            minimo = validar_numero_positivo(input("Mínimo: "))
            maximo = validar_numero_positivo(input("Máximo: "))

            if minimo > maximo:
                raise ValueError(ERR_RANGO_INVALIDO)

            for pais in paises:

                if minimo <= pais["superficie"] <= maximo:
                    resultados.append(pais)

        if len(resultados) == 0:
            print(MSG_SIN_RESULTADOS)

        else:
            mostrar_lista(resultados)

    except ValueError as e:
        print(f"{e}\n{VOLVER}")


def ordenar_paises(paises):

    print(TITULO_OP_5)

    if lista_vacia(paises):
        return

    try:

        criterio = int(input(MENU_ORDEN))

        if criterio not in range(1, 4):
            raise ValueError(ERR_OPCION_INVALIDA)

        direccion = input(
            "¿Orden ascendente (A) o descendente (D)? "
        ).upper()

        if direccion not in ["A", "D"]:
            raise ValueError(ERR_DIRECCION)

        ascendente = direccion == "A"

        lista_ordenada = [pais.copy() for pais in paises]

        n = len(lista_ordenada)

        for i in range(n - 1):

            for j in range(n - 1 - i):

                if criterio == 1:

                    actual = normalizar(
                        lista_ordenada[j]["nombre"]
                    )

                    siguiente = normalizar(
                        lista_ordenada[j + 1]["nombre"]
                    )

                elif criterio == 2:

                    actual = lista_ordenada[j]["poblacion"]
                    siguiente = lista_ordenada[j + 1]["poblacion"]

                else:

                    actual = lista_ordenada[j]["superficie"]
                    siguiente = lista_ordenada[j + 1]["superficie"]

                if ascendente and actual > siguiente:

                    lista_ordenada[j], lista_ordenada[j + 1] = (
                        lista_ordenada[j + 1],
                        lista_ordenada[j],
                    )

                elif not ascendente and actual < siguiente:

                    lista_ordenada[j], lista_ordenada[j + 1] = (
                        lista_ordenada[j + 1],
                        lista_ordenada[j],
                    )

        mostrar_lista(lista_ordenada)

    except ValueError as e:
        print(f"{e}\n{VOLVER}")