#refereshing csv file handling 
import csv

#Filters students by grade
def filter_by_grade(rows):
    for row in rows:
        if(int(row['GradeId']) >= 10):
            print(row['LastName'], row['FirstName'])
#filters students by gender
def filter_by_gender(rows):
    gender = input("Enter the gender youd like to 'retrieve' F or M: ")
    for row in rows:
        if(row['GenderId'] == gender):
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
    reader = csv.DictReader(students)
    rows = list(reader)


#   filter_by_grade(rows)
#   print('By Gender:\n')
#   filter_by_gender(rows)
#   print('Hispanic/Latino:\n')
#   report_by_ethnicity(rows)
    has_disability(rows)
    students.close