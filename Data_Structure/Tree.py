class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.v = val

class Tree:
    def __init__(self):
         self.root = None

    def gerRoot(self):
        return  self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
    def _add(self,val, node):
        if val < node.v:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val,self.root)
    def _find(self,val,node):
        if val == node.v:
           print('----------------------------')
           print('------Found the value-------')
           print('----------------------------')

        elif val < node.v and node.left is not None:
            self._find(val, node.left)

        elif val > node.v and node.right is not None:
            self._find(val, node.right)

        else:
            print('----------------------------')
            print('------Value Not Found-------')
            print('----------------------------')


    def deleteTree(self):
        self.root = None
        print('----------------------------')
        print('-------- Tree Deleted-------')
        print('----------------------------')

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.v))
            self._printTree(node.right)

tree = Tree()
while True:
    print("1. Add Element 2. Search for element 3.Print Tree 4. Delete Tree and Exit")
    choice = int(input("enter you choice"))
    if choice == 1:
        val = int(input("Enter Element are: "))
        tree.add(val)

    elif choice == 2:
        val = int(input("Enter the value to be search"))
        tree.find(val)

    elif choice == 3:
        tree.printTree()
    elif choice == 4:
        tree.deleteTree()
        break
    else:
        print("the choice is wrong")



