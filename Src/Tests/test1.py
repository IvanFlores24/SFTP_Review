#refereshing csv file handling
#today im working on filtering / object handling 
import csv

def filter_by_grade(rows):
    grade = int(input("Enter the minmum grade youd like to 'retrieve' 0-12: "))
    for row in rows:
        if(int(row['GradeId']) == grade):
            print(row['LastName'], row['FirstName'])

def filter_by_gender(rows):
    gender = input("Enter the gender youd like to 'retrieve' F or M: ")
    for row in rows:
        if(row['GenderId'] == gender):
            print(row['FirstName'])

def report_by_ethnicity(rows):
    for row in rows:
        if(row['HispanicLatino'] == 'Y'):
            print(row)

with open('Students.csv', newline='') as students:
    reader = csv.DictReader(students)
    rows = list(reader)


    filter_by_grade(rows)
    print('By Gender:\n')
    filter_by_gender(rows)
    print('Hispanic/Latino:\n')
    report_by_ethnicity(rows)
    students.close