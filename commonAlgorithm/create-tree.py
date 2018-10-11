class Tree: 	
    def __init__(self, cargo, left = None, right = None):		
        self.cargo = cargo		
        self.left = left		
        self.right = right		
    
    def __str__(self):		
        return str(self.cargo) 

tree = Tree(1, Tree(2), Tree(3))

def total(atree):
    if atree == None:
        return 0
    else:
        return total(atree.left) + total(atree.right) + atree.cargo

print(total(tree))


def printTree(atree):
	if atree == None:
		return 
	print (atree.cargo)
	printTree(atree.left)
	printTree(atree.right)
print ("Preorder:")
printTree(tree)

def printTreePostOrder(atree):
    if atree == None:
        return
    printTreePostOrder(atree.left)
    printTreePostOrder(atree.right)
    print(atree.cargo)

print("PostOrder:")
printTreePostOrder(tree)

def printTreeInorder(atree):
    if atree == None:
        return 
    printTreeInorder(atree.left)
    print(atree.cargo)
    printTreeInorder(atree.right)

print("Inorder: ")
printTreeInorder(tree)

