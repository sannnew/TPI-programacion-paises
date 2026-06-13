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

def separador(signo, longitud):
    return signo * longitud

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


