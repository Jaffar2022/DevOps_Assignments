students = {}

while True:
    choice = input("\n1.Add  2.Update  3.Print  4.Exit : ")

    if choice == "1":
        name = input("Student name: ")
        grade = input("Grade: ")
        students[name] = grade

    elif choice == "2":
        name = input("Student name to update: ")
        if name in students:
            students[name] = input("New grade: ")
        else:
            print("Student not found")

    elif choice == "3":
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        break

    else:
        print("Invalid choice")