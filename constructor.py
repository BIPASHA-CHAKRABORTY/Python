class Person:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def show(self):
        print("Name:",self.name,"\nSex:",self.sex)
    

jess=Person('Jess','female')

jess.show()
