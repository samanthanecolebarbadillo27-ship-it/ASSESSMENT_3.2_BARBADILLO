class Node:
    def __init__(self, data):
        self.data = data
        self.next = None            # only one direction


class SinglyLinkedList:
    def __init__(self):
        self.head = None            # Step 2: empty list, head is None

    def add(self, data):
        new_node = Node(data)       # Step 3: create new node
        if self.head is None:       # Step 4: empty -> new node is head
            self.head = new_node
        else:                       # else connect to last node using next
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        parts, current = [], self.head
        while current:
            parts.append(current.data)
            current = current.next
        print(" -> ".join(parts) + " -> None")

    def remove_all(self):
        while self.head is not None:        # Step 5 & 7
            print("Remove", self.head.data) # Step 6: display head data
            self.head = self.head.next      # move head to next node
        print("List is now empty")


def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    lst = SinglyLinkedList()

    print("\nAdding the letters:")
    for ch in word:
        if ch.isalpha():
            lst.add(ch)
    lst.display()

    print("\nRemoving the letters:")
    lst.remove_all()


if __name__ == "__main__":
    main()
