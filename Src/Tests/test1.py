# Refreshing CSV file handling
# Today I'm working on filtering / object handling 
import csv

# Filters students by grade
# Retrieves students whose grade is equal to the desired grade
def filter_by_grade(rows):
    grade = int(input("Enter the minimum grade you'd like to 'retrieve' 0-12: "))
    for row in rows:
        if int(row['GradeId']) == grade:
            print(row['LastName'], row['FirstName'])
    print()

# Filters students by gender
# Retrieves all students who match the desired gender
def filter_by_gender(rows):
    gender = input("Enter the gender you'd like to 'retrieve' F or M: ")
    for row in rows:
        if row['GenderId'] == gender:
            print(row['FirstName'], row['LastName'])
    print()

# Reports all Hispanic/Latino students
def report_by_ethnicity(rows):
    for row in rows:
        if row['HispanicLatino'] == 'Y':
            print(row)

# Reports all students who have a disability
def has_disability(rows):
    for row in rows:
        if row['DisabilityCategories'] != "":
            print(row['FirstName'], row['LastName'])
    print()

# Retrieves and reports all students with an IEP
def report_all_iep(rows):
    for row in rows:
        if row['IEP'] == 'Y':
            print(row['FirstName'], row['LastName'], row['IEP'])
    print()

# Open CSV file and retrieve its content
with open('Students.csv', newline='', encoding='utf-8') as students:
    reader = csv.DictReader(students)
    rows = list(reader)

    # Example usage:
    filter_by_grade(rows)
    # print('By Gender:\n')
    # filter_by_gender(rows)
    # print('Hispanic/Latino:\n')
    # report_by_ethnicity(rows)
    has_disability(rows)

    students.close()
