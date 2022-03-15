from nodos.nodo import *
from arboles.arbol import *

T = arbol()

T.ingresar(nodo(5))
T.ingresar(nodo(2))
T.ingresar(nodo(4))
T.ingresar(nodo(7))
T.ingresar(nodo(1))

'''

	5
   / \
  2	  7
 / \
1   4

'''
T.inOrder(T.getRaiz())
T.preOrder(T.getRaiz())
T.posOrder(T.getRaiz())

#print(T.getLista())

#print(T.returnAlturaDelElemento(T.getRaiz(), 2))

print(T.sumarNodos(T.getRaiz()))