class Person:
    def __init__(self,name,idname):
        self.name=name
        self.idname=idname

    def display(self):
        print(self.name)
        print(self.idname)

class cv(Person):
    def __init__(self,name,idname,salary,post):
        self.salary=salary
        self.post=post

        Person.__init__(self,name,idname)
    def display(self):
        print(self.post)
        print(self.salary)
        Person.display(self)

person1=cv("vishnu",43,43000,"manager")
person1.display()
        
