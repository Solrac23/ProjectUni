class Node(object):

	def __init__(self, d, n = None, p = None):
		self.data = d
		self.next = n
		self.prev = p

	def get_next(self):
		return self.next

	def set_next(self, n):
		self.next = n
		
	def get_prev(self):
		return self.prev

	def set_prev(self, p):
		self.prev = p
		
	def get_data(self):
		return self.data

	def set_data(self, d):
		self.data = d
		
	def to_string(self):
		return "Node value: " + str(self.data)
		
	def has_next(self):
		if self.get_next() is None:
			return False
		return True

class DoublyLinkedList(object):
  def __init__(self, r = None):
    self.root = r
    self.last = r
    self.size = 0
  
  def getSize(self):
    # if self.size == " ":
    #   return str(self.size)
    # else:
      return self.size

  def add (self, d):
    if self.size == 0:
      self.root = Node(d)
      self.last = self.root
    else:
      new_node = Node(d, self.root)
      self.root.set_prev(new_node)
      self.root = new_node
    self.size += 1
	
  def printList(self):
    print("Print List..........")
    if self.root is None:
      return
    this_node = self.root
    print(this_node.to_string())
    while this_node.has_next():
      this_node = this_node.get_next()
      print(this_node.to_string())

def main():
  myList = DoublyLinkedList()
  myList.add("Carlos Eduardo")
  myList.add("João")
  myList.add("Pedro")
  myList.add("Matheus")
  myList.add("Lucas")
  print("size="+ str(myList.getSize()))
  myList.printList()

main()