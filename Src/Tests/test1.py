#refereshing csv file handling
#today im working on filtering / object handling 
import csv

<<<<<<< HEAD
#Filters students by grade
=======
#retrieves students whos grade is equal to or above desired grade 
>>>>>>> main
def filter_by_grade(rows):
    grade = int(input("Enter the minmum grade youd like to 'retrieve' 0-12: "))
    for row in rows:
        if(int(row['GradeId']) == grade):
            print(row['LastName'], row['FirstName'])
<<<<<<< HEAD
#filters students by gender
=======
    print()
    print(row)

#retrieves all students who match desired gender 
>>>>>>> main
def filter_by_gender(rows):
    gender = input("Enter the gender youd like to 'retrieve' F or M: ")
    for row in rows:
        if(row['GenderId'] == gender):
<<<<<<< HEAD
            print(row['FirstName'])
#reports all hispanic/latino students
def report_by_ethnicity(rows):
    for row in rows:
        if(row['HispanicLatino'] == 'Y'):
            print(row)
#reports all students who have a disability
def has_disability(rows):
    for row in rows:
        if(row['DisabilityCategories'] != ""):
            print(row['FirstName'])
#Open's csv file and retreives it's content 
with open('Students.csv', newline='') as students:
=======
            print(row['FirstName'], row['LastName'])
#retrieves all students who are hispanic/latino
def report_by_ethnicity(rows):
    for row in rows:
        if(row['HispanicLatino'] == 'Y'):
            print(row['FirstName'], row['LastName'])

#retreieve and report all students with an IEP
def report_all_iep(rows):
    for row in rows:
        if(row['IEP'] == 'Y'):
            print(row['FirstName'], row['LastName'], row['IEP'])

#note to self refactor and remove the repetative for row in rows
with open('Students.csv', newline='', encoding='utf-8') as students:
>>>>>>> main
    reader = csv.DictReader(students)
    rows = list(reader)


<<<<<<< HEAD
#   filter_by_grade(rows)
#   print('By Gender:\n')
#   filter_by_gender(rows)
#   print('Hispanic/Latino:\n')
#   report_by_ethnicity(rows)
    has_disability(rows)
=======
    filter_by_grade(rows)
#   print('By Gender:\n')
#    filter_by_gender(rows)
#    print('\nHispanic/Latino:')
#    report_by_ethnicity(rows) 
>>>>>>> main
    students.close