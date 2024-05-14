

def generar_subconjuntos(conjunto):
  """
  Función que genera todos los subconjuntos propios de un conjunto dado.

  Args:
    conjunto: Un conjunto de elementos.

  Returns:
    Una lista de subconjuntos propios.
  """
  subconjuntos = []
  for i in range(1 << len(conjunto)):
    if i != 0 and i != (1 << (len(conjunto) - 1)):
      subconjunto = []
      for j in range(len(conjunto)):
        if (i & (1 << j)) > 0:
          subconjunto.append(conjunto[j])
      subconjuntos.append(subconjunto)
  return subconjuntos





def generar_grafo(equipo):
    """
    Función que genera un grafo dirigido a partir de las combinaciones del equipo.

    Args:
        equipo: Una lista que contiene los nombres de los miembros del equipo.

    Returns:
        Un objeto Grafo que representa el grafo generado.
    """
    grafo = grafo()

    # Generar subconjuntos del equipo
    subconjuntos = generar_subconjuntos(equipo)

    # Crear aristas en el grafo
    for i in range(len(subconjuntos) - 1):
        for j in range(i + 1, len(subconjuntos)):
            subconjunto_i = set(subconjuntos[i])
            subconjunto_j = set(subconjuntos[j])

            # Si el grupo B tiene un elemento menos que el grupo C
            if len(subconjunto_j) == len(subconjunto_i) + 1:
                diferencia = subconjunto_j - subconjunto_i
                elemento_diferente = list(diferencia)[0]

                # Agregar arista dirigida de grupo i a grupo j
                grafo.agregar_arista(frozenset(subconjunto_i), frozenset(subconjunto_j), peso=1)

                # Agregar arista dirigida de elemento diferente al grupo i
                grafo.agregar_arista(elemento_diferente, frozenset(subconjunto_i), peso=1)

    return grafo




equipo = ["Luz", "José", "Juan", "Eva", "Sara", "Luna", "Ana", "Leo", "Emma", "Iván"]

subconjuntos = generar_subconjuntos(equipo)



grafo = generar_grafo(equipo)

# Imprimir el grafo
print(grafo)


        











