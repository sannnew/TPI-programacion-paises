# TPI - Gestión de Datos de Países
# Programación 1 - UTN
import os

# HELPERS

def separador(signo, longitud):
    return signo * longitud


def normalizar(texto):
    """
    Elimina espacios iniciales/finales y convierte a minúsculas.
    Se usa para comparar nombres ignorando mayúsculas y espacios.
    """
    return texto.strip().lower()


def buscar_pais_por_nombre(paises, nombre):
    """
    Busca un país por nombre exacto en la lista.
    Retorna el diccionario si lo encuentra, o None si no existe.
    """
    for pais in paises:
        if normalizar(pais["nombre"]) == normalizar(nombre):
            return pais
    return None


def validar_nombre(paises, nombre):
    """
    Valida que un nombre no esté vacío ni duplicado.
    Lanza ValueError con mensaje descriptivo si alguna condición falla.
    """
    if nombre.strip() == "":
        raise ValueError(ERR_NOMBRE_VACIO)
    if buscar_pais_por_nombre(paises, nombre) is not None:
        raise ValueError(ERR_PAIS_DUPLICADO.format(nombre.strip()))


def validar_numero_positivo(valor_string):
    """
    Convierte un string a entero y valida que sea mayor que cero.
    Lanza ValueError si no es un número entero o si es menor o igual a cero.
    """
    try:
        valor = int(valor_string)
    except ValueError:
        raise ValueError(ERR_DEBE_SER_ENTERO)
    if valor <= 0:
        raise ValueError(ERR_MAYOR_QUE_CERO)
    return valor


def mostrar_lista(lista):
    """
    Muestra por pantalla una lista de países con formato de tabla.
    Recibe cualquier lista de diccionarios, no solo la lista global.
    """
    if len(lista) == 0:
        print(MSG_SIN_PAISES)
        return
    print(f"""
{SEP_TABLA}
  {'Nombre':<25} {'Población':>15} {'Superficie':>15} {'Continente':<15}
{SEP_TABLA}""")
    for pais in lista:
        print(
            f"  {pais['nombre']:<25} {pais['poblacion']:>15,} {pais['superficie']:>15,} {pais['continente']:<15}"
        )
    print(SEP_TABLA)


def lista_vacia(paises):
    """
    Verifica si la lista de países está vacía e informa al usuario.
    Retorna True si está vacía, False si tiene países.
    """
    if len(paises) == 0:
        print(ERR_LISTA_VACIA)
        return True
    return False



# CONSTANTES


NOMBRE_ARCHIVO = "datos/paises.csv"

OPCION_AGREGAR = 1
OPCION_ACTUALIZAR = 2
OPCION_BUSCAR = 3
OPCION_FILTRAR = 4
OPCION_ORDENAR = 5
OPCION_ESTADISTICAS = 6
OPCION_MOSTRAR_TODOS = 7
OPCION_SALIR = 8

PAISES_INICIALES = [
    "Argentina,45376763,2780400,América",
    "Japón,125800000,377975,Asia",
    "Brasil,213993437,8515767,América",
    "Alemania,83149300,357022,Europa",
]

ERR = "Error"

ERR_OPCION_INVALIDA = f"{ERR}: Opción no válida. Ingrese un número entre 1 y 8."
ERR_DEBE_SER_ENTERO = f"{ERR}: Debe ingresar un número entero."
ERR_MAYOR_QUE_CERO = f"{ERR}: El valor debe ser un número entero mayor que cero."
ERR_NOMBRE_VACIO = f"{ERR}: El nombre no puede estar vacío."
ERR_CONTINENTE_VACIO = f"{ERR}: El continente no puede estar vacío."
ERR_LISTA_VACIA = f"{ERR}: No hay países cargados."
ERR_PAIS_NO_EXISTE = f"{ERR}: El país '{{}}' no existe en el sistema."
ERR_PAIS_DUPLICADO = f"{ERR}: El país '{{}}' ya existe en el sistema."
ERR_RANGO_INVALIDO = f"{ERR}: El mínimo no puede ser mayor que el máximo."
ERR_DIRECCION = f"{ERR}: Ingrese A para ascendente o D para descendente."
ERR_CSV_FORMATO = f"{ERR}: Línea con formato incorrecto ignorada."
ERR_CSV_GUARDADO = f"{ERR}: No se pudo guardar el archivo."
ERR_TERMINO_VACIO = f"{ERR}: El término de búsqueda no puede estar vacío."

VOLVER = "Volviendo al menú principal."

SEP_TITULO = separador("-", 50)
SEP_MENU = separador("=", 50)
SEP_TABLA = separador("-", 72)
SEP_STATS = separador("-", 44)

TITULO_OP_1 = f"\n{SEP_TITULO}\n{'Opción 1 - Agregar país':^50}\n{SEP_TITULO}"
TITULO_OP_2 = f"\n{SEP_TITULO}\n{'Opción 2 - Actualizar país':^50}\n{SEP_TITULO}"
TITULO_OP_3 = f"\n{SEP_TITULO}\n{'Opción 3 - Buscar país':^50}\n{SEP_TITULO}"
TITULO_OP_4 = f"\n{SEP_TITULO}\n{'Opción 4 - Filtrar países':^50}\n{SEP_TITULO}"
TITULO_OP_5 = f"\n{SEP_TITULO}\n{'Opción 5 - Ordenar países':^50}\n{SEP_TITULO}"
TITULO_OP_6 = f"\n{SEP_TITULO}\n{'Opción 6 - Estadísticas':^50}\n{SEP_TITULO}"
TITULO_OP_7 = f"\n{SEP_TITULO}\n{'Opción 7 - Todos los países':^50}\n{SEP_TITULO}"
TITULO_OP_8 = f"\n{SEP_MENU}\n{'Opción 8 - Salir':^50}\n{SEP_MENU}"

MSG_SIN_PAISES = "No hay países para mostrar."
MSG_SIN_RESULTADOS = "No se encontraron países con ese criterio."

MENU = f"""
{SEP_MENU}
{'Gestión de Datos de Países':^50}
{SEP_MENU}
  1. Agregar país
  2. Actualizar país
  3. Buscar país
  4. Filtrar países
  5. Ordenar países
  6. Mostrar estadísticas
  7. Mostrar todos los países
  8. Salir
{SEP_MENU}
Seleccione una opción: """

MENU_FILTROS = f"""
{SEP_TITULO}
{'Filtrar por':^50}
{SEP_TITULO}
  1. Por continente
  2. Por rango de población
  3. Por rango de superficie
Seleccione una opción: """

MENU_ORDEN = f"""
{SEP_TITULO}
{'Ordenar por':^50}
{SEP_TITULO}
  1. Por nombre
  2. Por población
  3. Por superficie
Seleccione una opción: """


# FUNCIONES DE ARCHIVO



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



# FUNCIONES DE MENÚ



def agregar_pais(paises):
    """
    Solicita los datos de un nuevo país y lo agrega a la lista.
    Valida que ningún campo esté vacío y que el nombre no esté duplicado.
    Usa raise para lanzar errores de validación.
    """
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
    """
    Busca un país por nombre exacto y actualiza su población y superficie.
    No modifica el nombre ni el continente.
    """
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
        pais["poblacion"] = validar_numero_positivo(input("Nueva población: "))
        pais["superficie"] = validar_numero_positivo(input("Nueva superficie (km²): "))
        guardar_csv(paises, NOMBRE_ARCHIVO)
        print(f"País '{pais['nombre']}' actualizado correctamente.")

    except ValueError as e:
        print(f"{e}\n{VOLVER}")


def buscar_pais(paises):
    """
    Busca países por coincidencia parcial o exacta en el nombre.
    Muestra todos los países cuyo nombre contenga el texto ingresado.
    """
    print(TITULO_OP_3)

    if lista_vacia(paises):
        return

    try:
        termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip()
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
    """
    Filtra la lista según el criterio elegido:
    por continente, rango de población o rango de superficie.
    """
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
            print("Rango de población:")
            minimo = validar_numero_positivo(input("  Mínimo: "))
            maximo = validar_numero_positivo(input("  Máximo: "))
            if minimo > maximo:
                raise ValueError(ERR_RANGO_INVALIDO)
            for pais in paises:
                if minimo <= pais["poblacion"] <= maximo:
                    resultados.append(pais)
            print(f"\nPaíses con población entre {minimo:,} y {maximo:,}:")

        elif opcion == 3:
            print("Rango de superficie (km²):")
            minimo = validar_numero_positivo(input("  Mínimo: "))
            maximo = validar_numero_positivo(input("  Máximo: "))
            if minimo > maximo:
                raise ValueError(ERR_RANGO_INVALIDO)
            for pais in paises:
                if minimo <= pais["superficie"] <= maximo:
                    resultados.append(pais)
            print(f"\nPaíses con superficie entre {minimo:,} y {maximo:,} km²:")

        if len(resultados) == 0:
            print(MSG_SIN_RESULTADOS)
        else:
            mostrar_lista(resultados)

    except ValueError as e:
        print(f"{e}\n{VOLVER}")


def ordenar_paises(paises):
    """
    Ordena una copia de la lista según el criterio y dirección elegidos.
    Usa bubble sort manual. No modifica la lista original.
    """
    print(TITULO_OP_5)

    if lista_vacia(paises):
        return

    try:
        criterio = int(input(MENU_ORDEN))
        if criterio not in range(1, 4):
            raise ValueError(ERR_OPCION_INVALIDA)

        direccion = input("¿Orden ascendente (A) o descendente (D)? ").strip().upper()
        if direccion not in ["A", "D"]:
            raise ValueError(ERR_DIRECCION)
        ascendente = direccion == "A"

        lista_ordenada = []
        for pais in paises:
            lista_ordenada.append(pais.copy())

        n = len(lista_ordenada)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if criterio == 1:
                    val_actual = normalizar(lista_ordenada[j]["nombre"])
                    val_siguiente = normalizar(lista_ordenada[j + 1]["nombre"])
                elif criterio == 2:
                    val_actual = lista_ordenada[j]["poblacion"]
                    val_siguiente = lista_ordenada[j + 1]["poblacion"]
                else:
                    val_actual = lista_ordenada[j]["superficie"]
                    val_siguiente = lista_ordenada[j + 1]["superficie"]

                if ascendente and val_actual > val_siguiente:
                    lista_ordenada[j], lista_ordenada[j + 1] = (
                        lista_ordenada[j + 1],
                        lista_ordenada[j],
                    )
                elif not ascendente and val_actual < val_siguiente:
                    lista_ordenada[j], lista_ordenada[j + 1] = (
                        lista_ordenada[j + 1],
                        lista_ordenada[j],
                    )

        criterios = {1: "nombre", 2: "población", 3: "superficie"}
        direccion_label = "ascendente" if ascendente else "descendente"
        print(f"\nPaíses ordenados por {criterios[criterio]} ({direccion_label}):")
        mostrar_lista(lista_ordenada)

    except ValueError as e:
        print(f"{e}\n{VOLVER}")


def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadísticas generales:
    mayor/menor población, promedios y cantidad por continente.
    """
    print(TITULO_OP_6)

    if lista_vacia(paises):
        return

    mayor_pob = paises[0]
    menor_pob = paises[0]
    total_poblacion = 0
    total_superficie = 0
    continentes = {}

    for pais in paises:
        if pais["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = pais
        if pais["poblacion"] < menor_pob["poblacion"]:
            menor_pob = pais
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        if pais["continente"] in continentes:
            continentes[pais["continente"]] += 1
        else:
            continentes[pais["continente"]] = 1

    promedio_poblacion = total_poblacion // len(paises)
    promedio_superficie = total_superficie // len(paises)

    print(f"""
{SEP_STATS}
  Total de países      : {len(paises)}
{SEP_STATS}
  Mayor población      : {mayor_pob['nombre']} ({mayor_pob['poblacion']:,} hab.)
  Menor población      : {menor_pob['nombre']} ({menor_pob['poblacion']:,} hab.)
{SEP_STATS}
  Promedio población   : {promedio_poblacion:,} hab.
  Promedio superficie  : {promedio_superficie:,} km²
{SEP_STATS}
  Países por continente:""")
    for continente in continentes:
        print(f"    {continente:<20}: {continentes[continente]}")
    print(SEP_STATS)


# BLOQUE PRINCIPAL


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
