class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None
    
    def addLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
   

    def showList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def merging_node(self, x):
        current = self.head
        while current:
            if current.data == x:
                return current
            current = current.next
        return None 

    def merge(self, merging_node, list2):
        
        current = list2.head
        if current is None:
            list2.head = merging_node 
        else:
            while current.next:
                current = current.next 
            current.next = merging_node 
        list2.tail = self.tail 
    def tailll(self):
        return self.tail
    def merging_node2(self,node):
        return node.next.data
if __name__ == "__main__":
    l1 = SinglyLinkedList()
    l1.addLast(1)
    l1.addLast(2)
    l1.addLast(3)
    l1.addLast(4)
    l2 = SinglyLinkedList()
    l2.addLast(5)
    l2.addLast(6)
    l2.addLast(7)
    xx= l2.tailll()

    merging_node = l1.merging_node(2)
    l1.merge(merging_node, l2)
    print("First List : ",end="")
    l1.showList()  

    print("Second List : ",end="")
    l2.showList()
    print("Merging element : ",end="")
    print(l1.merging_node2(xx))

