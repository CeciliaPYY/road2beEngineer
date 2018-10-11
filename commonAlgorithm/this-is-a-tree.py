class Tree:
    def __init__(self, cargo, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.cargo)

tree = Tree(1, Tree(3), Tree(5))

def total(atree):
    if atree == None:
        return 0
    else:
        return total(atree.left) + total(atree.right) + atree.cargo

print(total(tree))

def printTreePreOrder(atree):
    if atree == None:
        return 
    print(atree.cargo)
    printTreePreOrder(atree.left)
    printTreePreOrder(atree.right)

print("Pre-Order: ")
printTreePreOrder(tree)

def printTreeInOder(atree):
    if atree == None:
        return
    printTreeInOder(atree.left)
    print(atree.cargo)
    printTreeInOder(atree.right)

print("In-Order: ")
printTreeInOder(tree)

def printTreePostOrder(atree):
    if atree == None:
        return
    printTreePostOrder(atree.left)
    printTreePostOrder(atree.right)
    print(atree.cargo)

print("Post-Order: ")
printTreePostOrder(tree)


