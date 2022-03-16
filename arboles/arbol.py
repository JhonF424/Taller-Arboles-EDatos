from nodos.nodo import *

class arbol():
    def __init__(self):
        self.raiz = None
        self.lista = []
        
    def getRaiz(self):
        return self.raiz
    
    def getLista(self):
        return self.lista
    
    def ingresar(self, nodo):
        if self.raiz == None:
            self.raiz = nodo
        else:
            self.ingresarR(self.raiz, nodo)
            
    def ingresarR(self, padre, nodo):
        # Si no hay un nodo padre establecido, retorna un true porque ...
        if padre == None:
            return True
        
        # Si el nodo hijo es menor que el nodo padre, se establece en la rama izquierda
        if nodo.getDato() < padre.getDato():
            if self.ingresarR(padre.getIzq(), nodo):
                padre.setIzq(nodo)
                return False

        # Si el nodo hijo es mayor que el nodo padre, se establece en la rama derecha
        if nodo.getDato() > padre.getDato():
            if self.ingresarR(padre.getDer(), nodo):
                padre.setDer(nodo)
                return False
        
        return False
    
    
    def inOrder(self, padre):
        if padre == None:
            return

        self.inOrder(padre.getIzq())
        self.lista.append(padre.getDato())
        self.inOrder(padre.getDer())


    def preOrder(self, padre):
        if padre == None:
            return

        self.lista.append(padre.getDato())
        self.preOrder(padre.getIzq())
        self.preOrder(padre.getDer())

    def posOrder(self, padre):
        if padre == None:
            return

        self.posOrder(padre.getIzq())
        self.posOrder(padre.getDer())
        self.lista.append(padre.getDato())

    def returnAltura(self, padre):
        if padre == None:
            return 0

        altura = 1 + max(self.returnAltura(padre.getIzq()), self.returnAltura(padre.getDer()))
        return altura

    def returnAlturaDelElemento(self, padre, n, alt):
        if not padre:
            return 0

        if padre.getDato() == n:
            return alt + 1
        
        if n < padre.getDato():
            return self.returnAlturaDelElemento(padre.getIzq(), n, alt + 1) 
        
        if n > padre.getDato():
            return self.returnAlturaDelElemento(padre.getDer(), n, alt + 1) 
         
    def sumarNodos(self, padre):
        if padre == None:
            return 0

        suma = 0

        sumaI = self.sumarNodos(padre.getIzq())
        sumaD = self.sumarNodos(padre.getDer())
        suma = sumaI + sumaD + padre.getDato()

        return suma

    # def encontrarPrimos(self, padre):
    #     self.encontrarPrimos(padre.getIzq())
    #     if padre.getDato():
    #         self.lista.append(padre.getDato())
    #         self.encontrarPrimos(padre.getDer())