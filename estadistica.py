from constantes import *
from validaciones import lista_vacia


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