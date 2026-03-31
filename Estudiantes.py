students = []

def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except:
            print("Error: you must enter a valid number")


def get_text(message):
    while True:
        text = input(message)
        if text.strip() == "":
            print("Error: this field cannot be empty")
        else:
            return text


def add_student():
    quantity = get_number("How many students do you want to add?: ")

    for i in range(quantity):
        print(f"\nStudent {i+1}")

        name = get_text("Name: ")
        age = get_number("Age: ")
        course = get_text("Course: ")

        student_id = len(students) + 1

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        print("Student added successfully")


def show_students():
    if len(students) == 0:
        print("There are no registered students")
    else:
        print("\nStudent list:")
        for student in students:
            print("----------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])


def search_student():
    if len(students) == 0:
        print("There are no students to search")
        return

    id_to_search = get_number("Enter the student ID: ")

    found = False

    for student in students:
        if student["id"] == id_to_search:
            print("\nStudent found:")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            found = True
            break

    if not found:
        print("Student not found")


def delete_student():
    if len(students) == 0:
        print("There are no students to delete")
        return

    id_to_delete = get_number("Enter the ID to delete: ")

    found = False

    for student in students:
        if student["id"] == id_to_delete:
            students.remove(student)
            print("Student deleted successfully")
            found = True
            break

    if not found:
        print("Student not found")


while True:
    print("""
======== MENU ========
Add student
Show students
Search student
Delete student
Exit
=====================
""")

    option = input("Choose an option: ")

    if option == "1":
        add_student()
    elif option == "2":
        show_students()
    elif option == "3":
        search_student()
    elif option == "4":
        delete_student()
    elif option == "5":
        print("Program finished")
        break
    else:
        print("Invalid option")
