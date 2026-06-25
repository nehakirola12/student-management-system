class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print("-" * 20)


students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, marks)
        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                student.display()

    elif choice == "3":
        search_id = input("Enter Student ID to search: ")
        found = False

        for student in students:
            if student.student_id == search_id:
                student.display()
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        delete_id = input("Enter Student ID to delete: ")
        found = False

        for student in students:
            if student.student_id == delete_id:
                students.remove(student)
                found = True
                print("Student deleted successfully!")
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")