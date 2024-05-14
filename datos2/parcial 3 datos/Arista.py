class Arista():

    def __init__(self, integrantes):

        self.integrantesComa=integrantes

        self.num=self.cantidad()

    def cantidad(self):

        num = len(self.integrantesComa.split(','))
        return num
    
    def getList(self):

        return self.integrantesComa
    
    def getpeso(self):

        return self.num
    
