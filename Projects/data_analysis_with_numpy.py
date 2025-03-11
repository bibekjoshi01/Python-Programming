import numpy as np


# function to initialize and store data
def initialize_data():
    # create array of subjects
    subject = np.array(["English", "Maths", "Science", "Social", "History"])

    # create a student array
    students = np.array(["Sakshi", "Bibek", "Deepak", "Manish"])

    # assign random marks for each student and subject
    marks = np.array(
        [
            [81, 78, 80, 60, 63],
            [50, 60, 65, 48, 55],
            [30, 83, 97, 79, 75],
            [99, 55, 60, 48, 30],
        ]
    )

    return subject, students, marks


# function that takes user input for new record
def add_record(studentArray, subjectArray, marksArray):
    studentName = input("Student's Name: ")
    marks = np.empty(len(subjectArray), dtype=int)

    for i in range(len(subjectArray)):
        marks[i] = int(input(f"Enter marks for {subjectArray[i]}: "))

    studentArray = np.append(studentArray, studentName)
    marksArray = np.vstack((marksArray, marks))

    return studentArray, marksArray


# display the records
def display_record(studentArray, subjectArray, marksArray):

    # Calculation
    totalArray = np.sum(marksArray, axis=1)
    avgArray = np.mean(marksArray, axis=1)
    resultArray = np.where(np.all(marksArray >= 40, axis=1), "PASS", "FAIL")

    headerArray = np.hstack(
        ("Student/Subject", subjectArray, np.array(["Total", "Average", "Result"]))
    )

    # create a lengthArray for formatting purpose
    lengthArray = np.array([len(element) for element in headerArray])

    # print the separator line
    separator = "+".join(["-" * length for length in lengthArray])
    header = "|".join(headerArray)

    print(separator)
    print(header)
    print(separator)

    # print the marks for each student
    for i, student in enumerate(studentArray):
        row = f"{student :<{16}}"
        row += "".join(
            f"|{mark:<{len(subjectArray[col])}}"
            for col, mark in enumerate(marksArray[i])
        )
        # add Total, Average and Pass result for each student
        row += "|" + f"{totalArray[i]:<{lengthArray[6]}}"
        row += "|" + f"{avgArray[i]:<{lengthArray[7]}}"
        row += "|" + f"{resultArray[i]:<{lengthArray[8]}}"

        print(row)
    print(separator)


def main():
    subject, students, marks = initialize_data()
    # students, marks = add_record(students, subject, marks)
    display_record(students, subject, marks)


main()
