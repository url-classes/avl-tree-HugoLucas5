from node import Node


class AVLTree:

    def __init__(self) -> None:
        self.__root = None

    def __height(self, node):
        if node is None:
            return 0
        else:
            return node.high

    def __balancefactor(self, node):
        if node is None:
            return 0
        else:
            return self.__height(node.left) - self.__height(node.right)

    def __rotate_right(self, node):
        tempa = node.left
        tempb = tempa.right
        tempa.right = node
        node.left = tempb
        node.high = 1 + max(self.__height(node.left), self.__height(node.right))
        tempa.high = 1 + max(self.__height(tempa.left), self.__height(tempa.right))
        if node is self.__root:
            self.__root = tempa
        return tempa

    def __rotate_left(self, node):
        tempa = node.right
        tempb = tempa.left
        tempa.left = node
        node.right = tempb
        node.high = 1 + max(self.__height(node.left), self.__height(node.right))
        tempa.high = 1 + max(self.__height(tempa.left), self.__height(tempa.right))
        if node is self.__root:
            self.__root = tempa
        return tempa

    def insert(self, val):
        if self.__root is None:
            self.__root = Node(val)
            self.__root.high = 1 + max(self.__height(self.__root.left), self.__height(self.__root.right))
        else:
            temp = self.__root
            while temp is not None:
                if val <= temp.dato:
                    if temp.left is None:
                        self.insert_left(val, temp.dato)
                        break
                    else:
                        temp = temp.left
                elif val > temp.dato:
                    if temp.right is None:
                        self.insert_right(val, temp.dato)
                        break
                    else:
                        temp = temp.right
            temp.high = 1 + max(self.__height(temp.left), self.__height(temp.right))
            self.check_balance(val, self.__root)

    def check_balance(self, val, node):
        if node is not None:
            balance = self.__balancefactor(node)
            if balance > 1:
                if node.left is not None and node.left.dato > val:
                    org = node.dato
                    node = self.__rotate_right(node)
                    self.guardarcambios(node, org)
                if node.left is not None and val > node.left.dato:
                    org = node.dato
                    node.left = self.__rotate_left(node.left)
                    node = self.__rotate_right(node)
                    self.guardarcambios(node, org)
            if balance < -1:
                if node.right is not None and val > node.right.dato:
                    org = node.dato
                    node = self.__rotate_left(node)
                    self.guardarcambios(node, org)
                if node.right is not None and val < node.right.dato:
                    org = node.dato
                    node.right = self.__rotate_right(node.right)
                    node = self.__rotate_left(node)
                    self.guardarcambios(node, org)
            self.check_balance(val, node.left)
            self.check_balance(val, node.right)

    def guardarcambios(self, node, valoriginal):
        if node is not None:
            if node is not self.__root:
                temp = self.__root
                while temp is not None:
                    if temp.right.dato == valoriginal:
                        temp.right = node
                        break
                    elif temp.left.dato == valoriginal:
                        temp.left = node
                        break
                    elif valoriginal > temp.dato:
                        temp = temp.right
                    elif valoriginal <= temp.dato:
                        temp = temp.left

    def insert_left(self, data, ref):
        node = self.__search(ref)
        if node is not None:
            new_node = Node(data)
            if node.left is None:
                node.left = new_node
            else:
                raise Exception("The left side isn't empty")
        else:
            raise Exception("The reference doesn't exist")

    def insert_right(self, data, ref):
        node = self.__search(ref)
        if node is not None:
            new_node = Node(data)
            if node.right is None:
                node.right = new_node
            else:
                raise Exception("The right side isn't empty")
        else:
            raise Exception("The reference doesn't exist")

    def __search(self, ref, *args):
        node = self.__root if len(args) == 0 else args[0]
        if node is not None:
            if node.dato == ref:
                return node
            else:
                result = self.__search(ref, node.left)
                if result is None:
                    result = self.__search(ref, node.right)
                    return result
                else:
                    return result
        else:
            return None

    def preorder(self, *args):
        node = self.__root if len(args) == 0 else args[0]
        if node is not None:
            if node.isleaf():
                return str(node.dato)
            else:
                result = str(node.dato) + ' ('
                result += self.preorder(node.left) + ', '
                result += self.preorder(node.right) + ')'
                return result
        else:
            return ''
