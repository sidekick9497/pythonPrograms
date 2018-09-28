class BinaryTree:
    class Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
        def getVal(self):
            return self.val
        def setVal(self,val):
            self.val = val
        def getLeft(self):
            return self.left
        def setLeft(self,val):
            self.left = val
        def getRight(self):
            return self.right
        def setRight(self,val):
            self.right = val
    def __init__(self,listItems):
        self.listItems = listItems
        self.tree = []
    def createBinaryTree(self):
        listItemsLength = len(self.listItems)
        listNodes = []
        i = 0
        while True:
            if(i > listItemsLength):
                break
            # formula for binary tree node childs node = i*2+1 for left and i*2 + 2
            if i == 0:
                tempNode = self.node(self.listItems[i])
                if (i*2)+1 < listItemsLength:
                    tempNode.setLeft = self.node(self.listItems[(i*2)+1])
                if (i*2)+2 <listItemsLength:
                    tempNode.setRight = self.node(self.listItems[(i*2)+2])
                listNodes.push(tempNode)    
            else:
                 tempNode = self.Node(self.listItems[i])
                 

