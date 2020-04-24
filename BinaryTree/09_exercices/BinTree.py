class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def _getLeft(self):
        return self.left

    def _setLeft(self, left):
        self.left = left

    def _getRight(self):
        return self.right

    def _setRight(self, right):
        self.right = right

    def _getData(self):
        return self.data

    def _setData(self, right):
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def _getRoot(self):
        return self.root

    def isEmpty(self):
        if self.root == None:
            return True
        return False
    
    def insert(self, data):
        # criar um novo nó
        node = Node(data)

        # verifica se a árvore está vazia
        if self.isEmpty():
            self.root = node
        else:
            # árvore não vazia, insere recursivamente
            data_node = None
            curr_node = self.root

            while True:
                if curr_node != None:
                    data_node = curr_node

                    # verifica se vai para esquerda ou direita
                    if node._getData() < curr_node._getData():
                        curr_node = curr_node._getLeft()
                    else:
                        curr_node = curr_node._getRight()
                else:
                    # se curr_node é None, então encontrou onde inserir
                    if node._getData() < data_node._getData():
                        data_node._setLeft(node)
                    else:
                        data_node._setRight(node)
                    break # finaliza o loop
    
    # mostra árvore Pré-Ordem (raiz-esq-dir)
    def show(self, curr_node):
       if curr_node != None:
           print('%d' % curr_node._getData(), end=' ')
           self.show(curr_node._getLeft())
           self.show(curr_node._getRight())

tree = Tree()

tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(14)
tree.insert(13)
tree.show(tree._getRoot())
