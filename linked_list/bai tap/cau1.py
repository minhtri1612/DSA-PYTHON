#    viết giải thuật thực hiện các thao tác trên danh sách liên kết đơn
#    a. in danh sách
#    b. tính số lượng các nút danh sách
#    c. kiểm tra danh sách có nút nào chứa gtri x không
#    d. bổ sung giá trị x vào danh sách nếu không tìm thấy x trong danh sách
#    e. xóa nút có giá trị x khỏi danh sách nếu danh sách có chứa giá trị x


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def createList(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
        print()
    def insertHead(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    
    def so_luong(self):
        current=self.head
        so_luong=0
        while current is not None:
            so_luong+=1
            current=current.next
        return so_luong
        
    def search(self,target):
        current=self.head
        while current is not None and current.data !=target:
            current=current.next
        return current is not None
     
    def remove(self, target):
        current = self.head
        previous = None
        while current is not None:
            if current.data == target:
                if previous is None:  # Node to be removed is the head
                    self.head = current.next 
                else:
                    previous.next = current.next
                print(f"Removed {target} from the list.")
                return
            previous = current
            current = current.next
        
    def add_if_not_found(self, target):
        if not self.search(target):
            self.insertHead(target)
            print(f"Added {target} to the list.")
        else:
            print(f"{target} already exists in the list.")
    
    def remove_if_found(self,data):
        if self.search(target):
            self.remove(target)
            
    
ll=LinkedList()
ll.insertHead(3)
ll.insertHead(4)
ll.insertHead(1)
ll.insertHead(2)
ll.createList()
print("\n")
print(f"Linked list co {ll.so_luong()} phan tu")
target=int(input("nhap gia tri can tim:"))
gia_tri=ll.search(target)
print(f"co gia tri:{target} khong?:",gia_tri)
if gia_tri:
    ll.remove_if_found(target)
else:
    ll.add_if_not_found(target)
ll.createList()

