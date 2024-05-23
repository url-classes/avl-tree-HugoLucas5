from avl_tree import AVLTree

arbol = AVLTree()
opcion = 1

while opcion > 0:
    print("Bienvenido, que quiere hacer?")
    print("1 - Insertar nodo al arbol    2 - Ver arbol   0 - Salir")
    opcion = int(input())

    if opcion == 1:
        print("Que numero quiere insertar?")
        num = int(input())
        arbol.insert(num)
    if opcion == 2:
        print("Arbol Actual")
        print(arbol.preorder())
