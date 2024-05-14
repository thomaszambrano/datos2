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



equipo = ["Luz", "José", "Juan", "Eva", "Sara", "Luna", "Ana", "Leo", "Emma", "Iván"]

subconjuntos = generar_subconjuntos(equipo)

# Abrir el archivo de salida en modo de escritura
with open('combinaciones.txt', 'w') as file:
    for subconjunto in subconjuntos:
        # Escribir cada combinación en el archivo
        file.write(', '.join(subconjunto) + '\n')

print(subconjuntos)
