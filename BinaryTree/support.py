from tree import BinaryTree, Node

  #     '+'
  #   /     \
  # 'a '     '*'
  #         /    \
  #       'b'     '-'
  #             /     \
  #           '/'        'e'
  #          /    \
  #        'c'     'd'

#(a + (b * ((c/d) - e)))

if __name__ == "__main__":
      tree = BinaryTree()
      n1 = Node('a')
      n2 = Node('+')
      n3 = Node('*')
      n4 = Node('b')
      n5 = Node('-')
      n6 = Node('/')
      n7 = Node('c')
      n8 = Node('d')
      n9 = Node('e')

      n6.left = n7
      n6.right = n8
      n5.left = n6
      n5.right = n9
      n3.left = n4
      n3.right = n5
      n2.left = n1
      n2.right = n3
      tree.root = n2
