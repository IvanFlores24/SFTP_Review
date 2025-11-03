#refereshing csv file handling 
import csv

def filter_by_grade(reader):
    for row in reader:
        if(int(row['GradeId']) >= 10):
            print(row['LastName'], row['FirstName'])

def filter_by_gender(reader):
    gender = input("Enter the gender youd like to 'retrieve' F or M: ")
    for row in reader:
        if(row['GenderId'] == gender):
            print(row['FirstName'])

with open('Students.csv', newline='') as students:
    reader = csv.DictReader(students)
    filter_by_grade(reader)
    print('\n')
    students.seek(0)
    filter_by_gender(reader)