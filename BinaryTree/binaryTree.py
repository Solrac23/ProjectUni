class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def _getData(self):
        return self.data

    def _setData(self, data):
        self.data = data

    def _getLeft(self):
        return self.left

    def _setLeft(self, left):
        self.left = left

    def _getRight(self):
        return self.right

    def _setRight(self, right):
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def _getRoot(self):
        return self.root

    def insert(self, data):
        # cria um novo nó
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
                    break

    def isEmpty(self):
        if self.root == None:
            return True
        return False
    # mostra em pré-ordem (raiz-esq-dir)
    def show(self, curr_node):
        if curr_node != None:
            print('%d' % curr_node._getData(), end=' ')
            self.show(curr_node._getLeft())
            self.show(curr_node._getRight())

    # mostra em em-Ordem (esq-raiz-dir)
    def showInOrder(self, curr_node):
        if curr_node != None:
            self.showInOrder(curr_node._getLeft())
            print('%d' % curr_node._getData(), end=' ')
            self.showInOrder(curr_node._getRight())

    # mostra Pós-ordem (esq-dir-raiz)
    def showPostOrder(self, curr_node):
        if curr_node != None:
            self.showPostOrder(curr_node._getLeft())
            self.showPostOrder(curr_node._getRight())
            print('%d' % curr_node._getData(), end=' ')
          

tree = BinaryTree()

tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(8)
tree.insert(6)
tree.show(tree._getRoot())
print('')
tree.showInOrder(tree._getRoot())
print('')
tree.showPostOrder(tree._getRoot())

# tree.insert(15)
# tree.insert(10)
# tree.insert(20)
# tree.insert(5)
# tree.insert(13)
# tree.insert(18)
