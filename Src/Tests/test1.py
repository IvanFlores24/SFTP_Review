#refereshing csv file handling
#today im working on filtering / object handling 
import csv

#retrieves students whos grade is equal to or above desired grade 
def filter_by_grade(rows):
    grade = int(input("Enter the minmum grade youd like to 'retrieve' 0-12: "))
    for row in rows:
        if(int(row['GradeId']) == grade):
            print(row['LastName'], row['FirstName'])
    print()
    print(row)

#retrieves all students who match desired gender 
def filter_by_gender(rows):
    gender = input("Enter the gender youd like to 'retrieve' F or M: ")
    for row in rows:
        if(row['GenderId'] == gender):
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
    reader = csv.DictReader(students)
    rows = list(reader)


    filter_by_grade(rows)
#   print('By Gender:\n')
#    filter_by_gender(rows)
#    print('\nHispanic/Latino:')
#    report_by_ethnicity(rows) 
    students.close