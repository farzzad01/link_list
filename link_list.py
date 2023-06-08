class Node:
    def __init__(self, name, lastname, student_number):
        self.name = name
        self.lastname = lastname
        self.student_number = student_number
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, name, lastname, student_number):
        new_node = Node(name, lastname, student_number)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_student(self, student_number):
        if self.head is None:
            return

        if self.head.student_number == student_number:
            self.head = self.head.next
            return

        





if __name__ == "__main__":
    main()

