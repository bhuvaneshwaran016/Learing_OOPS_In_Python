""" Now I learning OOPS so this file is how to create class and object for student in Python  for class attribute"""

class student:
    College_Name="ABC_College"
    def __init__(self,name,age,area):
        self.name=name
        self.age=age
        self.area=area
    def display(self):
        print("Student Details\n")
        print(self.name,self.age,self.College_Name,self.area)

s1=student("Arun",19,"Tir")
s2=student("Bala",20,"Cbe")

s1.display()
s2.display()