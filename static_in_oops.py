class student:
    clg_name="siet"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def change_clg_name(cls,name):
        cls.clg_name=name

    def display(self):
        print(self.clg_name,self.name)

    @staticmethod
    def check_age(age):
        if age>=18:
            print("Eligible")
        else:
            print("Not Eligible")

s1=student("Arun",19)
s1.display()
s1.check_age(19)
student.change_clg_name("Sri Shakthi Inititue Of Engineering And Technology")
s2=student("priya",20)
s2.display()

