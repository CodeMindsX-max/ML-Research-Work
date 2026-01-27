import numpy as np
"""
Problem no. 2.0
==Student Marks Management System==
Scenario: You’re building the backend logic for a school's internal grading tool.

>>Create a program that:

>have sample dic with hard coded data {'Ali':[78,85,90],'Sara':[88,92,79]}

>>Takes user input:

>name (must be in string add validation)
>marks (marks must be integer or float number add validation)
>store student in dictionary their names become 'key' and value will be list of number of diff subjects

>>Functions to create:

>add_student(student_dict)
*take user input
*Adds a new student with marks
*Prevent duplicate student names

>calculate_average(marks_list)
*return average (don't print it)

>get_topper(student_dict)
*return name + average of top student

>get_failed_student(student_dict)
*Return list of students whose average < 50

--Must use functions
--Use loops + conditions 
--use lambda function only where it makes sense
->now this is little advance python enjoy it
"""
def validate_number(value):
    return value.replace('.', '', 1).isdigit()

def add_student(students):
    name = input("Enter student name: ").strip()

    if not name.isalpha():
        print("Name must contain only alphabets")
        return students

    if name in students:
        choice = input("Student exists. Update marks? (y/n): ")
        if choice.lower() != 'y':
            return students

    marks = []
    for i in range(3):
        while True:
            m = input(f"Enter marks for subject {i+1}: ")
            if validate_number(m):
                marks.append(float(m))
                break
            print("Invalid marks")

    students[name] = marks
    return students

def calculate_average(marks):
    return sum(marks) / len(marks)
"""
Another way to calculate avg if you want to become data analyst and learning NumPy
 def calculate_averages(marks_list):
     arr=np.array(marks_list)
     average=np.mean(arr)
     return average
"""
"""
my logic
def get_topper(std_dic):
    avg=[]
    name=[]
    for k,v in std_dic.items():
        name.append(k)
        avg.append(calculate_average(v))

    max_avg=max(avg)
    max_avg_index=avg.index(max_avg)
    print(f"{name[max_avg_index]} is a topper with {max_avg} average marks")
"""
"""
Chatgpt style :) below and yes more advance style to write function not tradional
def get_topper(std_dic):
    topper = max(std_dic, key=lambda name: calculate_average(std_dic[name]))
    avg = calculate_average(std_dic[topper])
    print(f"{topper} is a topper with {avg} average marks")
"""

def get_topper(students):
    topper = max(students, key=lambda s: calculate_average(students[s]))
    return topper, calculate_average(students[topper])
"""
my logic
def get_failed(std_dic):
    avg=[]
    name=[]
    for k,v in std_dic.items():
        name.append(k)
        avg.append(calculate_average(v))
    for i in range(len(avg)):
        if avg[i]<50:
            return(f'{name[i]} failed with {avg[i]} average marks')
"""

def get_failed_students(students):
    return [
        name for name, marks in students.items()
        if calculate_average(marks) < 50
    ]
"""
my logic
def main():
    std_dic={'Ali':[78,85,90],'Sara':[88,92,79]}
    while True:
        while True:
            choce=input("Press 1 to add student\n" \
            "Press 2 to check topper student\n" \
            "Press 3 to check failed students\n" \
            "Press anything else to exit\n" \
            "Your choice: ")
            if validate_num(choce):
                choice=int(choce)
                break
            else:
                print('Wrong input, try again')

        if choice==1:
            std_dic=add_student(std_dic)
            continue
        elif choice==2:
            get_topper(std_dic)
            continue
        elif choice==3:
            print(get_failed(std_dic))
            continue
        else:
            break

"""            

def main():
    students = {
        "Ali": [78, 85, 90],
        "Sara": [88, 92, 79]
    }

    while True:
        choice = input(
            "\n1. Add Student"
            "\n2. Show Topper"
            "\n3. Show Failed Students"
            "\n4. Exit"
            "\nChoice: "
        )

        if choice == '1':
            students = add_student(students)

        elif choice == '2':
            name, avg = get_topper(students)
            print(f"Topper: {name} with average {avg:.2f}")

        elif choice == '3':
            failed = get_failed_students(students)
            if failed:
                print("Failed students:", ", ".join(failed))
            else:
                print("No failed students")

        else:
            break


main()