class Node(object):
    def __init__(self, d, next=None, prev=None):
        self.data = d
        self.prev = prev
        self.next = next

    def _getData(self):
        return self.data

    def _setData(self, d):
        self.data = d

    def _getPrev(self):
        return self.prev

    def _setPrev(self, prev):
        self.prev = prev

    def _getNext(self):
        return self.next

    def _setNext(self, next):
        self.next = next


class DoublyLikendList(object):
    def __init__(self, i=None):
        self.init = i
        self.size = 0

    # Função para pegar o tamanho
    def _getSize(self):
        return self.size

    # Função para adicionar a lista
    def add(self, d):
        # Adicionando um novo nó
        new_node = Node(d, self.init)

        if self.init:
            self.init._setPrev(new_node)
        self.init = new_node
        self.size += 1

    # Função para remover da lista
    def remove(self, d):
        this_node = self.init

        while this_node:
            if this_node._getData() == d:
                next = this_node._getNext()
                prev = this_node._getPrev()

                if next:
                    next._setPrev(prev)
                if prev:
                    prev._setNext(next)
                else:
                    self.init = this_node
                self.size -= 1
                return True  # removendo data
            else:
                this_node = this_node._getNext()
        return False  # data não encontrada

    # Função para buscar os dados
    def find(self, d):
        this_node = self.init
        while this_node:
            if this_node._getData() == d:
                return print(d)
            else:
                this_node = this_node._getNext()
        return None


myList = DoublyLikendList()
myList.add(10)
myList.add(5)
myList.add(14)
print(myList.remove(14))
myList.find(10)
