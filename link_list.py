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
        

        





if __name__ == "__main__":
    main()

