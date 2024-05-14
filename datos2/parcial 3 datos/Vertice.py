from Arista import Arista

class Vertice:

    def __init__(self, num, origen, destino):

        self.num =num

        self.adyacencia=[]

        self.AgregarAdyacencia(origen,destino)

    def AgregarAdyacencia(self, origen, destino):

        self.adyacencia.append([origen])
        self.adyacencia.append([destino])

        #print(self.adyacencia)

    def getVertice(self):
            
            if len(self.adyacencia) >= 2:  # Verifica que haya al menos dos aristas almacenadas
                arista_origen = self.adyacencia[0]
                arista_destino = self.adyacencia[1]
                return f'Peso: {self.num}\n---\nArista Origen:\n{arista_origen}\n---\nArista Destino:\n{arista_destino}'
            
            else:
                 
                 return f'tu mamá'