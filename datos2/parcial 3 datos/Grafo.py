from Arista import Arista
from Vertice import Vertice

class Grafo():

    def __init__(self):

        self.ListArista=[]
        self.ListVertice=[]

    def crearGrafo(self):

        with open('combinaciones.txt','r') as file:

            grupos = file.read().strip().split('\n')

            self.AgregarAristas(grupos)

            self.AgregarVertices(grupos)

            #print(self.ListArista)

            #print(self.ListVertice)


    def AgregarAristas(self,gruposList):
        
        for grupo in gruposList:

            lineas = grupo.split('\n')

            #print(f'\n\n--{lineas}--\n\n')

            integrantes = ','.join(lineas)

            arista = Arista(integrantes)

            self.ListArista.append(arista)

    def AgregarVertices(self,gruposList):

        for i in range(len(gruposList)):

            for j in range(i+1, len(gruposList)):

                grupo_origen = gruposList[i].split('\n')
                grupo_destino = gruposList[j].split('\n')

                tam_origen = len(grupo_origen[0].split(','))
                tam_destino = len(grupo_destino[0].split(','))

                if tam_origen > tam_destino:

                    origen = grupo_origen[0]
                    destino = grupo_destino[0]
                    peso = tam_origen - tam_destino
                    self.crearVertice(origen, destino, peso)

    def crearVertice(self,origen,destino,peso):

        vertice = Vertice(peso,origen,destino)

        self.ListVertice.append(vertice)


    def imprimirGrafo(self):

        print("Aristas:\n\n")

        i=0

        with open('Grafo.txt', 'w') as file:

            for vertice in self.ListVertice:
                i=i+1
                texto=f'\n\n--->Vertice número: {i}'
                        
                        # Escribir cada combinación en el archivo
                file.write(f'{texto}\n{vertice.getVertice()}\n\n')


def dijkstra(self, inicio, llegada):
  distancia = {}
  padre = {}
  for v in Vertice:
    distancia[v] = float('inf')
    padre[v] = None
    distancia[inicio] = 0
    
    vertices_restantes = set(self.vertices.keys())
    
    while vertices_restantes:
      u = min(vertices_restantes, key=lambda v: distancia[v])
      vertices_restantes.remove(u)
      
      if u == llegada:
        break
      
      
    for v in self.Vertice:
       if(u,v) in self.Arista:
         alt = distancia[u] + 1
         if alt < distancia[v]:
            distanica[v] = alt
            padre[v] = u
           
           
  Trayectoria = []
  v = llegada
  while padre[v] is not None:
    Trayectoria.append(v)
    v = padre[v]
    Trayectoria.append(inicio)
    Trayectoria.reverse()
    
    
    return Trayectoria, distancia[llegada]
    
     
      



if __name__ == "__main__":

    grafo =Grafo()

    grafo.crearGrafo()

    grafo.imprimirGrafo()




