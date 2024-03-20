class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubel_linked_list:
    def __init__(self):
        self.head = None
        #self.last = None
    
    def display_forward(self):
        if self.head is None:
            print("Dll is empty.")
        else:
            current_node = self.head
            print("Dari pertama ke terakhir")
            while current_node is not None:
                print(current_node.data, end= "")
                current_node = current_node.next
    
    def display_backward(self):
        print()
        if self.head is None:
            print("Dll is empty.") 
        else:
            current_node = self.head
            print("Dari terakhir ke pertama")
            while current_node.next is not None:
                current_node = current_node.next
            while current_node is not None:
                print(current_node.data, end="")
                current_node = current_node.prev

    def insert_at_beginning(self,data):
        nb = node(data)
        current_node = self.head
        current_node.prev = nb
        nb.next = current_node
        self.head = nb
       
    def insert_at_end(self,data):
        ne = node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = ne
        ne.prev = current_node

    def insert_at_x(self,position,data):
        nx = node(data)
        current_node  = self.head
        for _ in range(1,position - 1):
            current_node = current_node.next
        nx.prev = current_node
        nx.next = current_node.next
        current_node.next.prev = nx
        current_node.next = nx
        
    def deletion_at_beginning(self):
        current_node = self.head
        self.head = current_node.next
        current_node.next = None
        self.head.prev= None

    def deletion_at_end(self):
        prev = self.head
        current_node = self.head.next
        while current_node.next is not None:
            current_node = current_node.next
            prev = prev.next

        prev.next = None
        current_node.prev = None
        

    def deletion_at_x(self,position):
        current_node = self.head.next
        b = self.head
        for _ in range(1, position - 1):
            current_node = current_node.next
            b = b.next
        b.next = current_node.next
        current_node.next.prev = b
        current_node.next = None
        current_node.prev = None
      

dll = doubel_linked_list()

    
# Insert nodes
node1 = node(1)
node2 = node(2)
node3 = node(3)

dll.head = node1
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
# dll.last = node3

dll.insert_at_beginning(0)
dll.insert_at_end(4)
dll.insert_at_x(3,9)
dll.deletion_at_beginning()
dll.deletion_at_end()
# dll.deletion_at_x(3)
# Display forward and backward
dll.display_forward()
dll.display_backward()
