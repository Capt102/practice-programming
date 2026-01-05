"""
complete the function print number take an integer input from user and print it on screen
"""
class Solution:
    def printnumber(self):
        number=int(input())
        print(number)

"""
Given marks of a student, print on the screen:

Grade A if marks >= 90
Grade B if marks >= 70
Grade C if marks >= 50
Grade D if marks >= 35
Fail, otherwise.
"""
class Solution:
    def studentGrade(self, marks):
        if marks>=90:
            print("grade A")
        elif marks>=70:
            print("grade B")
        elif marks>=50:
            print("grade C")
        elif marks>=35:
            print("grade D")
        else:
            print("fail")

instance1=Solution()
instance1.studentGrade(50)