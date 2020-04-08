class No:
    def __init__(self, label):
        self.label = label
        self.next = None

    def __str__(self):
        return str(self.label)

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    # Função para inserir
    def push(self, label, index):
        if index >= 0:
            # cria um novo nó
            node = No(label)

            # Verifica se a lista está vazia
            if self.empty():
                self.first = node
                self.last = node
            else:
                if index == 0:
                    # inserção no início
                    node.setNext(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # inserção no final
                    self.last.setNext(node)
                    self.last = node
                else:
                    # inserção no meio
                    bef_node = self.first
                    curr_node = self.first.getNext()
                    curr_index = 1

                    while curr_node != None:
                        if curr_index >= index:
                            # seta o curr_node como o próximo do nó
                            node.setNext(curr_node)
                            # seta o node como o próximo do bef_node
                            bef_node.setNext(node)

            # Atualiza o tamanho da lista
            self.len_list += 1

    # Função para remover
    def remove(self, index):
        if not self.empty() and index >= 0 and index < self.len_list:
            flag_remove = False

            if self.first.getNext() == None:
                # possui apenas 1 elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # remove do início, mas possui mais de 1 elemento
                self.first = self.first.getNext()
                flag_remove = True
            else:
                bef_node = self.first
                curr_node = self.first.getNext()
                curr_index = 1

                while curr_node != None:
                    if index == curr_index:
                        # o próximo do anterior aponta para o próximo do nó corrente
                        bef_node.setNext(curr_node.getNext())
                        curr_node.setNext(None)
                        flag_remove = True
                        break

                    bef_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index += 1

            if flag_remove:
                # atualiza o tamanho da lista
                self.len_list += 1

    # Função para verificar o tamanho da lista
    def length(self):
        return self.len_list

    # Fução para verificar se a lista está vazia
    def empty(self):
        if self.first == None:
            return True
        return False

    # Função para mostrar a lista
    def show(self):
        curr_node = self.first
        while curr_node != None:
            print(curr_node.getLabel(), end=" ")
            curr_node = curr_node.getNext()
        print('')


lista = LinkedList()

lista.push('Carlos', 0)
lista.show()
lista.push('Keully', 1)
lista.show()
print("Tamanho da lista: %d\n" % lista.length())

lista.remove(0)
lista.show()
