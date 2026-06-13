from constantes import *


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
            f"  {pais['nombre']:<25} "
            f"{pais['poblacion']:>15,} "
            f"{pais['superficie']:>15,} "
            f"{pais['continente']:<15}"
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