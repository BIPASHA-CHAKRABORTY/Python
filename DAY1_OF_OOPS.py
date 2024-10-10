# CREATING A CLASS AND A NORMAL BASIC FUNCTION

class A:
    name="Bipasha"
    sex="78"
    def disp(self):
         print(f"{self.name} is a women of age {self.sex}")

a=A()
a.disp()

# MOD 1 Q1

class Person:
    name="HII"
    sex="none"
    profession="Acc"
    def work(self,name,sex,profession):
        self.name = name
        self.sex = sex
        self.profession = profession
        print(f"{self.name} is a {self.sex} working as a {self.profession}")
 
a=Person()
b=Person()
a.work("JESSA","Female","Software engg")
b.work("John","male","doctor")
