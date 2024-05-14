def construir_grafo_diferencia_un_elemento(conjunto):
    grafo = {}

    # Iterar sobre cada par de subconjuntos
    for i in range(len(conjunto)):
        for j in range(i + 1, len(conjunto)):
            subset1 = conjunto[i]
            subset2 = conjunto[j]

            if len(subset1) != len(subset2):
                continue  # Ignorar si los subconjuntos no tienen la misma longitud

            # Encontrar la diferencia entre los dos subconjuntos
            diferencia_indices = []
            for k in range(len(subset1)):
                if subset1[k] != subset2[k]:
                    diferencia_indices.append(k)

            # Deben diferir exactamente en un elemento
            if len(diferencia_indices) == 1:
                origen = tuple(subset1)
                destino = tuple(subset2)

                if origen not in grafo:
                    grafo[origen] = set()

                grafo[origen].add(destino)

    return grafo



def imprimir_grafo_txt(grafo, archivo):
  """
  Función que imprime un grafo dirigido en un archivo .txt.

  Args:
    grafo: Un diccionario que representa el grafo dirigido.
    archivo: La ruta del archivo .txt donde se guardará el grafo.
  """
  with open(archivo, "w") as f:
    for nodo, adyacentes in grafo.items():
      f.write(f"{nodo}:\n")
      for adyacente in adyacentes:
        f.write(f"  -> {adyacente}\n")
        
        
grafo = construir_grafo_diferencia_un_elemento(subconjuntos)
        