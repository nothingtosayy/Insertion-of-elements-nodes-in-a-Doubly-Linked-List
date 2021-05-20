class Node:
    def __init__(self,data,link1=None,link2=None):
        self.data =data
        self.link1= link1
        self.link2 = link2
class DoublyLL:
    def __init__(self,head = None):
        self.head = None
    def traverse(self):
        if self.head is None:
            print("Doubly LL is empty")
        else:
            while self.head is not None:
                print(self.head.data,end="--->")
                self.head = self.head.link2
    
    def insert_empty(self,data):
        new_node = Node(data)
        self.head = new_node
    
    def add_begin(self,data):
        new_node = Node(data)
        self.head.link1 = new_node
        new_node.link2 = self.head
        self.head = new_node
        
    def add_end(self,data):
        new_node = Node(data)
        n = self.head
        while n.link2 is not None:
            n = n.link2
        n.link2 = new_node
        new_node.link1 = n
    
    def add_between(self,data,x):
        new_node = Node(data)
        n = self.head
        while n.data != x:
            n = n.link2
        new_node.link1 = n.link2.link1
        new_node.link2 = n.link2
        n = new_node
        n.link1.link2 = n
        n.link2.link1 = n
        # n.link2 = new_node
        # new_node.link1 = n
d1 = DoublyLL()
d1.insert_empty(30)
d1.add_begin(20)
d1.add_begin(10)
d1.add_end(40)
d1.add_between(50,20)
d1.add_between(60,30)

d1.traverse()
        
