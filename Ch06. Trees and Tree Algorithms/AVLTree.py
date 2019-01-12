# NOT FINISHED
# update balance rotateRight
# delete method
# height property


class AVLTree:
    def __init__(self,key = None, payload = None, parent = None, 
            leftChild = None, rightChild = None, height = 0, balance = 0):
        self.key = key
        self.payload = payload
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.height = height
        self.balance = balance

    def isLeftChild(self):
        return self.parent.leftChild == self

    def isRightChild(self):
        return self.parent.rightChild == self

    def put(self, key, payload):
        if self.key == None:
            self.payload = payload
        elif self.key == key:
            self.payload = payload
        elif self.key > key:
            if self.leftChild != None:
                self.leftChild.put(key, payload)
            else:
                self.leftChild = AVLTree(key, payload, self)
                self.leftChild.height = self.leftChild.updateHeight()
                self.updateBalance(self.leftChild)
        elif self.key < key:
            if self.rightChild != None:
                self.rightChild.put(key, payload)
            else:
                self.rightChild = AVLTree(key, payload, self)
                self.rightChild.height = self.rightChild.updateHeight()
                self.updateBalance(self.rightChild)

    def updateHeigth(self):
        if self.parent == None:
            return 0
        else:
            return 1 + self.parent.updateHeigth()

    def updateBalance(self, node):
        if node.isLeftChild():
            self.balance += 1
        elif node.isRightChild():
            self.balance -= 1

        if self.balance < -1 or self.balance > 1:
            self.rebalance()
            return

        if self.balance != 0 and self.parent != None:
                self.parent.updateBalance(self)

    def rebalance(self):
        if self.balance < 0:
            if self.rightChild.balance > 0:
                self.rightChild.rotateRight()
                self.rotateLeft()
            else:
                self.rotateLeft()
        elif self.balance > 0:
            if self.leftChild.balance < 0:
                self.leftChild().rotateLeft()
                self.rotateRight()
            else:
                self.rotateRight()
        

    def rotateLeft(self):
        oldRoot = self
        newRoot = self.rightChild
        # child
        oldRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = oldRoot 
        # oldRoot parent
        newRoot.parent = oldRoot.parent
        if oldRoot.parent != None:
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            elif oldRoot.isRightChild():
                oldRoot.parent.rightChild = newRoot
        # set parent child relation
        newRoot.leftChild = oldRoot
        oldRoot.parent = newRoot

        oldRoot.balance = oldRoot.balance + 1 - min(newRoot.balance, 0)
        newRoot.balance = newRoot.balance + 1 + max(oldRoot.balance, 0) 

    def rotateRight(self):
        oldRoot = self
        newRoot = oldRoot.leftChild
        # child
        oldRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = oldRoot
        # oldRoot parent
        newRoot.parent = oldRoot.parent
        if oldRoot.parent != None:
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            elif oldRoot.isRightChild():
                oldRoot.parent.rightChild = newRoot
        # set parent child relation
        newRoot.rightChild = oldRoot
        oldRoot.parent = newRoot



