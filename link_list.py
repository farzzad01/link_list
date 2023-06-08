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

        current = self.head
        prev = None
        while current and current.student_number != student_number:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    def display_students(self):
        current = self.head
        while current:
            print(f"Name: {current.name}, Lastname: {current.lastname}, Student Number: {current.student_number}")
            current = current.next


def main():
    num_students = int(input("Enter the number of students: "))
    student_list = LinkedList()

    for _ in range(num_students):
        name = input("Enter name: ")
        lastname = input("Enter lastname: ")
        student_number = input("Enter student number: ")
        student_list.add_student(name, lastname, student_number)
        print('----------------------------------------')

    print("\nStudent list:")
    print('----------------------------------------')
    student_list.display_students()

    while True:
        delete_student_number = input("\nEnter student number to delete (or press to quit): ")
        if delete_student_number == '':
            break
        else:
            student_list.delete_student(delete_student_number)
            print("\nUpdated student list:")
            print('--------------------------------')
            student_list.display_students()

    print("Exiting the program.")


if __name__ == "__main__":
    main()

