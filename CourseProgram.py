'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''



def main():

    name = 'MIS 4322 - Advanced Python'
    crn = '250309'
    seats = 4
    status = 'open'
    students = ['John','James','Jill','Jack','Joanne']

import CourseClass as CC

course = CC.course(name,crn,seats,status)

reg0 = CC.Register(students[0], crn)
reg1 = CC.Register(students[1], crn)
reg2 = CC.Register(students[2], crn)
reg3 = CC.Register(students[3], crn)
reg4 = CC.Register(students[4], crn)

StuRegistration = [reg0, reg1, reg2, reg3, reg4]

count =+ 0 

for i in StuRegistration:
        if course.get_seats() > 0:
            course.update_seat_count()
            print("Name: ", student.get_name())
            print("Course: ", course.get_name())
            print("CRN: ", course.get_crn())
            print("Seats Left: ", course.get_seats())
            print()
            print()
        else:
           print("Sorry Joanne, registration is closed for MIS 4322 - Advanced Python")
    
main()



        
    
    
