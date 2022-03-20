from nodos.nodo import *
from arboles.arbol import *

T = arbol()

T.ingresar(nodo(5))
T.ingresar(nodo(2))
T.ingresar(nodo(4))
T.ingresar(nodo(7))
T.ingresar(nodo(1))
T.ingresar(nodo(11))
T.ingresar(nodo(8))
# T.ingresar(nodo(9))
# T.ingresar(nodo(12))
# T.ingresar(nodo(13))


'''

    5
   / \
  2	7
 / \   \
1   4   11
       /
      8

'''
# T.inOrder(T.getRaiz())
# T.preOrder(T.getRaiz())
# T.posOrder(T.getRaiz())

# print(T.getLista())

# print(T.returnAlturaDelElemento(T.getRaiz(), 4, 0))

# print(T.sumarNodos(T.getRaiz()))

# print(T.encontrarMenor(T.getRaiz()))

# print(T.encontrarMayor(T.getRaiz()))

# print(T.mostrarHojas(T.getRaiz()))

# print(T.recorrerPrimos(T.getRaiz()))

# T.listaHojas(T.getRaiz())
# print("Lista de hojas del arbol: ", T.getLista())

# print(T.cantNodos(T.getRaiz(), 0))

# T.almacenarParesyPrimos(T.getRaiz())
# print(T.getLista())

# print(T.validarPares(T.getRaiz()))
