class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_lv(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    
    def print_tree(self):
        spaces=' '*self.get_lv()*3
        
        print(spaces+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
            
def build_tree():
    root = TreeNode("electronic")
    
    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("Asus"))
    laptop.add_child(TreeNode("Lenovo"))
    
    root.add_child(laptop)
    
    dienthoai=TreeNode("cellphone")
    dienthoai.add_child(TreeNode("Iphone"))
    dienthoai.add_child(TreeNode("Samsung"))
    dienthoai.add_child(TreeNode("Nokia"))
    dienthoai.add_child(TreeNode("xiaomi"))
    root.add_child(dienthoai)
    print(dienthoai.get_lv())

    return root

root = build_tree()
print(root.get_lv())

root.print_tree()
