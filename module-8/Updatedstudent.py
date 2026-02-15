import json

def print_students(students):
    """
    Prints each student record in the format:
    Last, First : ID = id , Email = email
    """
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

def main():
    # a. Load the JSON file into a Python list
    try:
        with open('student.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        print("Error: student.json not found. Make sure the file is in the same folder.")
        return
    except json.JSONDecodeError:
        print("Error: student.json does not contain valid JSON. Ensure it is a JSON array.")
        return

    # c. Output notification that this is the original list
    print("Original Student List:")
    # d. Call the print function
    print_students(students)
    print()  # blank line for readability

    # e. Add your own information using append()
    # Replace these values with your own details
    new_student = {
        "F_Name": "Amanda",   
        "L_Name": "Tirey",    
        "Student_ID": 21462045,         
        "Email": "atirey@my365.bellevue.edu"
    }
    students.append(new_student)

    # f. Output notification that this is the updated list
    print("Updated Student List:")
    # g. Call the print function again
    print_students(students)
    print()

    # h. Use json.dump() to write the updated list back to the file
    with open('student.json', 'w') as file:
        json.dump(students, file, indent=4)

    # i. Output notification that the file was updated
    print("student.json has been updated successfully.")

if __name__ == "__main__":
    main()