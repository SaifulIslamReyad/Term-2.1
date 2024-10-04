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


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_count = 0

    def size(self):
        return self.size_count
    
    def isEmpty(self):
        return self.head is None
    
    def first(self):
        if self.isEmpty():
            return None
        return self.head.get_data()
    
    def last(self):
        if self.isEmpty():
            return None
        return self.tail.get_data()
    
    def addFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.size_count += 1

    def addLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.size_count += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        removed_data = self.head.get_data()
        self.head = self.head.get_next()
        if self.head is None:
            self.tail = None
        self.size_count -= 1
        return removed_data

    def showList(self):
        current = self.head
        while current:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print("None")


if __name__ == "__main__":
    l1 = SinglyLinkedList()
    l1.addLast(10)
    l1.addLast(20)
    l1.addLast(30)
    l1.addLast(40)
    l1.addLast(50)
    l1.showList()

    l2 = SinglyLinkedList()
    l2.addLast(1)
    l2.addLast(2)
    l2.addLast(3)
    l2.addLast(4)
    l2.addLast(5)
    l2.showList()

    print(f"First element in l1: {l1.first()}")
    print(f"Last element in l1: {l1.last()}")
    print(f"Size of l1: {l1.size()}")
    print(f"Is l1 empty? {l1.isEmpty()}")

    l1.addFirst(0)
    l1.showList()

    removed_element = l1.removeFirst()
    print(f"Removed first element: {removed_element}")
    l1.showList()

# • size(): Returns the number of elements in the list.
# • isEmpty(): Returns true if the list is empty, and false otherwise.
# • first(): Returns (but does not remove) the first element in the list.
# • last(): Returns (but does not remove) the last element in the list.
# • addFirst(e): Adds a new element to the front of the list.
# • addLast(e): Adds a new element to the end of the list.
# • removeFirst(): Removes and returns the first element of the list.