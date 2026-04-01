students = []

def add_student():
    try:
        quantity_students = int(input("How many students do you want to add?: "))
        student_id = len(students) + 1

        for idx in range(quantity_students):
            name = input(f"Enter the name of student {idx+1}: ")
            course = input(f"Enter the course of student {idx+1}: ")

            new_student = {
                "id_student": student_id,
                "name": name,
                "course": course,
            }

            students.append(new_student)
            print(f"Student {name} has been added successfully")
            student_id += 1

    except:
        print("Error: invalid input")


def show_students():
    if not students:
        print("There are no students")
    else:
        for student in students:
            print(f"ID: {student['id_student']} | Name: {student['name']} | Course: {student['course']}")


def search_student():
    search_id = int(input("Enter the student ID you want to search: "))
    found = False

    for student in students:
        if search_id == student['id_student']:
            print(f"ID: {student['id_student']} | Name: {student['name']} | Course: {student['course']}")
            found = True
            break

    if not found:
        print("Student not found")


def delete_student():
    delete_id = int(input("Enter the student ID to delete: "))
    found = False

    for student in students:
        if student['id_student'] == delete_id:
            students.remove(student)
            print("Student has been deleted")
            found = True
            break

    if not found:
        print("Student not found")


while True:
    option = input("""
================================
    What do you want to do?

    
1.Add new students
2.Show students
3.Search student
4.Delete a student
5.Exit program
================================

Choose an option: """)

    if option == "1":
        add_student()
    elif option == "2":
        show_students()
    elif option == "3":
        search_student()
    elif option == "4":
        delete_student()
    elif option == "5":
        print("Exiting the program. Thanks for using it <3")
        break
    else:
        print("Invalid option, please try again")
