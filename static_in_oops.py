class student:
    clg_name="siet"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def clg_name(cls,name):
        cls.clg_name=name

    def display(self):
        print(cls.clg_name,self.name)


s1=student("Arun",19)
s1.display()