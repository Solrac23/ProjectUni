class Queue:
    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def insert(self, i):
        self.queue.append(i)
        self.len_queue += 1

    def pop(self):
        if self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def length(self):
        return self.len_queue

    def front(self):
        if not self.empty():
            return self.queue[0]
        return None

    def show(self):
        if self.empty():
            return self.queue[0]
        else:
            return print(self.queue)


q = Queue()
q.insert(10)
q.insert(4)
q.insert(6)
q.insert(8)
q.insert(3)
q.pop()
print(q.front())
q.show()

