import json

# Dictionary to store all student records
students={} 

# Add a new student with grades
def add_students():
    print("\nPress 'q' to quit")
    name = input("Enter student name: ").strip()
    if name.lower() == 'q':
        print("Cancelled. Returning to menu.")
        return

    try:
        subject_count = int(input(f"How many subject does {name} have? "))
        if subject_count <= 0:
            print("Subject must be a number greater than 0")
            return
    except ValueError:
        print("Enter a valid number")
        return
    
    grades = []
    for i in range(1, subject_count + 1):
        while True:
            try:
                grade = float(input(f"What is {name}'s grade for subject #{i}: "))
                if 0 < grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Please anter a valid value for grades")
            except ValueError:
                print("Enter a valid number")
                return

    total = sum(grades)
    subs = len(grades)
    average = total / subs
    
    print(f"\n{name} has {subject_count} subjects.")
    print("--------------------------------------")
    print(f"{name}'s average is: {average:.2f}")

    if average >= 75:
            remark = "PASSED"
            print(f"{name} PASSED " ,end="")
            if average >= 98:
                remark = "Passed With Highest Honors"
                print("With Highest Honors")
            elif average >= 94.5:
                remark = "Passed With High Honors!"
                print("With High Honors")
            elif average >= 89.5:
                remark = "Passed With Honors"
                print("With Honors")
    else:
            remark = "FAILED"
            print(f"{name} failed")
    
    students[name] = {
        "Average": average,
        "Remarks": remark
    }

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print(f"{name}'s data is saved")
    
# Display all student records
def view_students():
    if not students:
        print("\nThere are no students to show")
    
    print("-" *40)
    print("Student list:")

    for name, data in students.items():
        print(f"Student name: {name}")
        print(f"Average: {data['Average']:.2f}")
        print(f"Remarks: {data['Remarks']}")
        print("-" *40)

# Search for a specific student
def search_students():
    while True:
        print("\nPress 'q' to quit")
        to_search = input("What is the name of the students you want to search? ")
        if to_search.lower() == "q":
            break
        elif to_search in students:
            print(f"Name    : {to_search}")
            print(f"Average : {students[to_search]['Average']:.2f}")
            print(f"Remarks : {students[to_search]['Remarks']}")
        else:
            print(f"No record found for{to_search}")

# Delete a student from records
def delete_students():
    print("\nStudents:")
    for name in students:
        print(f"- {name}")

    while True:
        print("\npress 'q' to quit")
        to_remove = input("Name of the student to be removed: ")
        if to_remove.lower() == "q":
            break
        elif to_remove in students:
            del students[to_remove]
            print(f"{to_remove} is removed")
        else:
            print(f"{to_remove} is not in the records")
    
    # Save updated dictionary to file
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
        print("\nRecord updated")   

# Main menu
def question():
    global students 

    # Load saved student data (if file exists)
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
        print("\n✅ Records loaded!")
    except FileNotFoundError:
        print("\n⚠️ No saved record found yet.")
    
    # Menu loop
    while True:
        print("\n1. Add Students")
        print("2. View Students")
        print("3. Search Students")
        print("4. Delete Students")
        print("5. Quit")
        try:
            ques = int(input("What do you want to do? select numbers 1-5: "))
        except ValueError:
            print("Enter a number between 1-5")
    
        if ques == 1:
            add_students()
        elif ques == 2:
            view_students()
        elif ques == 3:
            search_students()
        elif ques == 4:
            delete_students()
        elif ques == 5:
            print("Bye")
            break
        else:
            print("Invalid option")

question()
