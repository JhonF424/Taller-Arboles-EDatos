class nodo():
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None
        
    def getDato(self):
        return self.dato
    
    def getIzq(self):
        return self.izq
    
    def getDer(self):
        return self.der
    
    def setDato(self, dato):
        self.dato = dato
        
    def setIzq(self, izq):
        self.izq = izq
        
    def setDer(self, der):
        self.der = der
        