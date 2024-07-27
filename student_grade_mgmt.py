student_grades = {}
def add_student(name,grade):
    student_grades[name] = grade
    print(f"Added{name} with a {grade}Grade")
def update_student(name,grade):
    if name in student_grades:
        print("student name found in the database")
        student_grades[name] = grade
        print(f"student{name} grade {grade} has been updated")
    else:
        print(f"{name} not found in the database")
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name}has been succesfully deleted")
    else:
        print(f"{name} not found in the database")
def view_all():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} , {grade}")
    else:
        print("no student info is available yet!!")
def main():
    while True:
        print("THIS IS A STUDENT GRADE MANAGEMENT SYSTEM !!!!")
        operation = int(input(("1. for enter student info\n   2.for updating student grade\n  3.for deleting dtudent info\n 4.for viewing all the entered information of the students\n 5.for existing the application")))
        if operation == 1:
            name = input("enter student name:")
            grade = int(input("enter student grade:"))
            add_student(name,grade)
        elif operation == 2:
            name = input("enter student name:")
            grade = int(input("enter student grade:"))
            update_student(name,grade)
        elif operation == 3:
            name = input("enter student name:")
            delete_student(name)
        elif operation == 4:
            view_all()
        elif operation == 5:
            print("end of session")
            break
        else:
            print("invalid option")
main()
            
        
        