class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def __init__(self) -> None:
        self.root = None
    
    def height(self, root):
        if root == None:
            return 0
        
        return root.height

    def get_balance_factor(self, root):
        if root == None:
            return 0

        return self.height(root.left) - self.height(root.right)
    
    def left_rotate(self, n):
        right_node = n.right
        left_node = right_node.left

        right_node.left = n
        n.right = left_node
        
        n.height = 1 + max(self.height(n.left), self.height(n.right))
        right_node.height = 1 + max(self.height(right_node.left), self.height(right_node.right))

        return right_node
    
    def right_rotate(self, n):
        left_node = n.left
        right_node = left_node.right

        left_node.right = n
        n.left = right_node

        n.height = 1 + max(self.height(n.left), self.height(n.right))
        left_node.height = 1 + max(self.height(left_node.left), self.height(left_node.right))

        return left_node
    
    def insert(self, root, val):
        if not root:
            return Node(val)
        
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance_factor = self.get_balance_factor(root)

        if balance_factor > 1 and val < root.left.val:
            return self.right_rotate(root)
        
        if balance_factor < -1 and val > root.right.val:
            return self.left_rotate(root)
        
        if balance_factor > 1 and val > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if balance_factor < -1 and val < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def insertVal(self,val):
        self.root = self.insert(self.root, val)

    def printLevels(self):
        root = self.root
        q = [root]

        while q:
            qLen = len(q)
            level = []
            for idx in range(qLen):
                node = q.pop(0)

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            print(level)
            print('\n')


if __name__ == '__main__':
    avl = AVLTree()
    avl.insertVal(1)
    avl.insertVal(2)
    avl.insertVal(3)
    avl.insertVal(4)
    avl.insertVal(5)
    avl.insertVal(6)
    avl.printLevels()