import os

from constantes import *


def crear_csv_inicial(nombre_archivo):
    """
    Crea el archivo CSV con los 4 países de ejemplo del enunciado.
    Se llama automáticamente si el archivo no existe.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")

        for pais in PAISES_INICIALES:
            archivo.write(f"{pais}\n")

    print(f"Archivo '{nombre_archivo}' creado con los datos iniciales.")


def leer_csv(paises, nombre_archivo):
    """
    Lee el archivo CSV y carga los datos en la lista paises.
    Si el archivo no existe, lo crea con los 4 países de ejemplo.
    Valida el formato de cada línea antes de cargarla.
    """

    if not os.path.exists(nombre_archivo):
        crear_csv_inicial(nombre_archivo)

    try:

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            primera_linea = True

            for linea in archivo:

                if primera_linea:
                    primera_linea = False
                    continue

                linea = linea.strip()

                if linea == "":
                    continue

                partes = linea.split(",")

                if len(partes) != 4:
                    print(f"{ERR_CSV_FORMATO} -> {linea}")
                    continue

                try:

                    pais = {
                        "nombre": partes[0].strip(),
                        "poblacion": int(partes[1].strip()),
                        "superficie": int(partes[2].strip()),
                        "continente": partes[3].strip(),
                    }

                    paises.append(pais)

                except ValueError:
                    print(f"{ERR_CSV_FORMATO} -> {linea}")

        print(f"{len(paises)} países cargados correctamente.")

    except FileNotFoundError:
        print(f"{ERR}: No se encontró el archivo '{nombre_archivo}'.")


def guardar_csv(paises, nombre_archivo):
    """
    Sobrescribe el archivo CSV con el contenido actual de la lista paises.
    Se llama cada vez que se modifica la lista (agregar o actualizar).
    """

    try:

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:

            archivo.write("nombre,poblacion,superficie,continente\n")

            for pais in paises:

                archivo.write(
                    f"{pais['nombre']},{pais['poblacion']},"
                    f"{pais['superficie']},{pais['continente']}\n"
                )

    except IOError:
        print(f"{ERR_CSV_GUARDADO}\n{VOLVER}")