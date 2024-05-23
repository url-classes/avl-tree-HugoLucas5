class Node:
    def __init__(self, num):
        self.dato = num
        self.left = None
        self.right = None
        self.high = 1

    def isleaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False
