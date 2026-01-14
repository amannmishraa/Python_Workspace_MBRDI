# from math_utils import square,cube,sums
# print(cube(3))
# print(sums(20,32))

def student_marks(name,marks):
    if marks >= 60:
        print(name, "got distinction")
    elif marks > 50 and marks < 59.9:
        print(name,'got 1st division')
    elif marks < 50 and marks > 40:
        print(name,'got 2nd division')
    else:
        print(name,"failed")
    
name = input("Enter your name :")
marks = int(input('Enter your marks :'))
student_marks(name,marks)
