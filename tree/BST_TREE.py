class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)   
    
    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
     
    def in_order(self):
        elements = []
        if self.left:
            elements += self.left.in_order()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order()
            
        return elements

    def pre_order(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order()
        if self.right:
            elements += self.right.pre_order()
        return elements

    def post_order(self):
        elements = []
        if self.left:
            elements += self.left.post_order()
        if self.right:
            elements += self.right.post_order()
        elements.append(self.data)
        return elements

    def bfs(self):
        elements = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            elements.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return elements


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


    def delete(self,data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
                
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
        
            # min_val=self.right.find_min()
            # self.data=min_val
            # self.right=self.right.delete(min_val)
            
            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.delete(max_val)
        return self
def build_tree(elements):
    root = BSTNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root

numbers = [4, 3, 2,6,8,1, 19,14,18, 22]
numbers_tree = build_tree(numbers)
print("In-order traversal:", numbers_tree.in_order())
print("pre-order traversal:", numbers_tree.pre_order())
print("post-order traversal:", numbers_tree.post_order())
print("BFS:",numbers_tree.bfs())
print("Search for 3:", numbers_tree.search(3))
print("Search for 5:", numbers_tree.search(5))
print("maximum data:",numbers_tree.find_max())
print("minimum data:",numbers_tree.find_min())
numbers_tree.delete(3)
print("In-order traversal after delete 3:", numbers_tree.in_order())
