class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None            # Step 2: head and tail are None
        self.tail = None

    def add(self, data):
        new_node = Node(data)       # Step 3
        if self.head is None:       # Step 4: both head and tail
            self.head = self.tail = new_node
        else:                       # Step 5
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        parts, current = [], self.head
        while current:
            parts.append(current.data)
            current = current.next
        print("None <-> " + " <-> ".join(parts) + " <-> None")

    def remove_from_tail(self):
        while self.tail is not None:            # Step 6 & 8
            print("Remove", self.tail.data)     # Step 7: display tail data
            self.tail = self.tail.prev          # move tail to prev node
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
        print("List is now empty")


def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    dll = DoublyLinkedList()

    print("\nAdding the letters:")
    for ch in word:
        if ch.isalpha():
            dll.add(ch)
    dll.display()

    print("\nRemoving the letters starting from the tail:")
    dll.remove_from_tail()


if __name__ == "__main__":
    main()