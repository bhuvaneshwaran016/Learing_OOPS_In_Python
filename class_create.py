""" Now I learning OOPS so this file is how to create class and object for student in Python"""

class Students:
    def __init__(self,s_name,s_age,s_status):
        self.name=s_name
        self.age=s_age
        self.status=s_status

    def display(self):
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)
        print("Student Role: ",self.status)


s1=Students("Arun",19,"Enginnering")
s2=Students("aakash",20,"Doctor")

s1.display()
print("______________")
s2.display()