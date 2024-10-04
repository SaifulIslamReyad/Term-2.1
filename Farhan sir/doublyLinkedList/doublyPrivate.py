class Node:
    def __init__(self, data):
        self.__data = data  # Private data attribute
        self.__next = None  # Private next pointer
        self.__prev = None  # Private prev pointer

    # Getter and setter for data
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    # Getter and setter for next pointer
    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node

    # Getter and setter for prev pointer
    def get_prev(self):
        return self.__prev

    def set_prev(self, prev_node):
        self.__prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.__head = None  # Private head pointer
        self.__tail = None  # Private tail pointer
        self.__size_count = 0  # Private size counter

    # Getter for size
    def size(self):
        return self.__size_count

    # Check if the list is empty
    def isEmpty(self):
        return self.__size_count == 0

    # Add a node to the front of the list
    def addFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.__head = self.__tail = new_node  # The list is empty, so new node is both head and tail
        else:
            new_node.set_next(self.__head)  # New node points to the current head
            self.__head.set_prev(new_node)  # Current head's previous pointer points to new node
            self.__head = new_node  # Update the head to the new node
        self.__size_count += 1

    # Add a node to the end of the list
    def addLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.__head = self.__tail = new_node  # The list is empty, so new node is both head and tail
        else:
            self.__tail.set_next(new_node)  # Current tail's next pointer points to new node
            new_node.set_prev(self.__tail)  # New node's previous pointer points to current tail
            self.__tail = new_node  # Update the tail to the new node
        self.__size_count += 1

    # Remove the first node of the list
    def removeFirst(self):
        if self.isEmpty():
            return None
        removed_data = self.__head.get_data()
        if self.__head == self.__tail:  # Only one element in the list
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.get_next()  # Move head to the next node
            self.__head.set_prev(None)  # Set the previous pointer of the new head to None
        self.__size_count -= 1
        return removed_data

    # Remove the last node of the list
    def removeLast(self):
        if self.isEmpty():
            return None
        removed_data = self.__tail.get_data()
        if self.__head == self.__tail:  # Only one element in the list
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.get_prev()  # Move tail to the previous node
            self.__tail.set_next(None)  # Set the next pointer of the new tail to None
        self.__size_count -= 1
        return removed_data

    # Display the list from head to tail
    def showListForward(self):
        current = self.__head
        while current:
            print(current.get_data(), end=" <-> ")
            current = current.get_next()
        print("None")

    # Display the list from tail to head
    def showListBackward(self):
        current = self.__tail
        while current:
            print(current.get_data(), end=" <-> ")
            current = current.get_prev()
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("Adding elements at the end:")
    dll.addLast(10)
    dll.addLast(20)
    dll.addLast(30)
    dll.addLast(40)
    dll.showListForward()  # Should display: 10 <-> 20 <-> 30 <-> 40 <-> None

    print("\nAdding elements at the front:")
    dll.addFirst(5)
    dll.addFirst(0)
    dll.showListForward()  # Should display: 0 <-> 5 <-> 10 <-> 20 <-> 30 <-> 40 <-> None

    print("\nDisplaying list backward:")
    dll.showListBackward()  # Should display: 40 <-> 30 <-> 20 <-> 10 <-> 5 <-> 0 <-> None

    print("\nRemoving first element:")
    dll.removeFirst()
    dll.showListForward()  # Should display: 5 <-> 10 <-> 20 <-> 30 <-> 40 <-> None

    print("\nRemoving last element:")
    dll.removeLast()
    dll.showListForward()  # Should display: 5 <-> 10 <-> 20 <-> 30 <-> None

    print(f"\nSize of the list: {dll.size()}")
