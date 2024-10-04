class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class CircularlyLinkedList:
    def __init__(self):
        self.tail = None  
        self.size_count = 0

    def size(self):
        return self.size_count

    def isEmpty(self):
        return self.size_count == 0

    def first(self):
        if self.isEmpty():
            return None
        return self.tail.get_next().get_data() 

    def last(self):
        if self.isEmpty():
            return None
        return self.tail.get_data() 

    def addFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.tail = new_node
            self.tail.set_next(new_node)  
        else:
            new_node.set_next(self.tail.get_next()) 
            self.tail.set_next(new_node)  
        self.size_count += 1

    def addLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.tail = new_node
            self.tail.set_next(new_node)
        else:
            new_node.set_next(self.tail.get_next())
            self.tail.set_next(new_node)
            self.tail = new_node
        self.size_count += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        old_head = self.tail.get_next() 
        removed_data = old_head.get_data()
        if self.size_count == 1: 
            self.tail = None
        else:
            self.tail.set_next(old_head.get_next())  
        self.size_count -= 1
        return removed_data

    def rotate(self):
        if self.size_count > 0:
            self.tail = self.tail.get_next()

    def showList(self):
        if self.isEmpty():
            print("List is empty")
            return
        current = self.tail.get_next()  
        while True:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
            if current == self.tail.get_next(): 
                break
        print("... circular")

if __name__ == "__main__":
    clist = CircularlyLinkedList()

    clist.addLast(10)
    clist.addLast(20)
    clist.addLast(30)
    clist.addLast(40)
    clist.addLast(50)
    clist.showList()

    print(f"First element: {clist.first()}")
    print(f"Last element: {clist.last()}")
    print(f"Size: {clist.size()}")

    print("Rotating the list:")
    clist.rotate()  
    clist.showList()

    print("Adding element at the front:")
    clist.addFirst(5)
    clist.showList()

    print("Removing first element:")
    clist.removeFirst()
    clist.showList()
