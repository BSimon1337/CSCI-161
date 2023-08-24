'''
Beau Simon
CSCI L02
Assignment #10
Online Student - 0869416
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data=data)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def search(self, value):
        count = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count


def menu():
    linked_list = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Add to the list")
        print("2. Display the list")
        print("3. Search from the list")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            while True:
                value = input("Enter an integer value to add to the list (type 'done' when finished): ")
                if value == "done":
                    break
                linked_list.append(int(value))
        elif choice == 2:
            print("List:", linked_list.display())
        elif choice == 3:
            search_value = int(input("Enter the value you want to search for: "))
            count = linked_list.search(search_value)
            if count > 0:
                print(f"{search_value} found {count} time(s) in the list.")
            else:
                print("Item not found.")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
