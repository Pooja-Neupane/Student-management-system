# Student Record Management System using Dictionary

# Dictionary to store student records
students = {}

# Function to add a student
def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student with this roll number already exists.")
        return
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.\n")

# Function to search for a student
def search_student():
    roll = input("Enter Roll Number to Search: ")
    if roll in students:
        print(f"\nStudent Found:\nRoll: {roll}")
        print(f"Name: {students[roll]['name']}")
        print(f"Marks: {students[roll]['marks']}\n")
    else:
        print("Student not found.\n")

# Function to delete a student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    if roll in students:
        del students[roll]
        print("Student record deleted successfully.\n")
    else:
        print("Student not found.\n")

# Function to display all students
def display_all():
    if not students:
        print("No student records found.\n")
        return
    print("\nAll Student Records:")
    for roll, info in students.items():
        print(f"Roll: {roll} | Name: {info['name']} | Marks: {info['marks']}")
    print()

# Menu-driven program
def menu():
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            display_all()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
menu()

