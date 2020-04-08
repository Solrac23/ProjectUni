class Node:
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


class Queue:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next:

                last = last.next
            # append the new node
            last.next = node
        self.length += 1

