'''Operator overloading in python is 1) + symbol is used to strings concatetion and arithmetic addition
2) * sysmbol is used to multiple a list,string or tuple'''

#USE OF +
print(10+20)
print("Python"+ " Programming")
print([1,2]+[3,4])

#USE OF *

print(" Python"*3)
print([1,2,3]*4)


''Len() func use'''
my_string="Bipasha Chakraborty"
my_list=[2,3,4,5,6,7,8,9]
my_dict={"name":"Namm","Age":3}
print(len(my_string))
print(len(my_list))
print(len(my_dict))

# Method Overloading
class Studennt:
    def sum(self,a=None,b=None,c=None):   
        if(a!=None and b!=None and c!=None):
            print("You added 3 num: ",-a+b+c)
        elif(a!=None and b!=None):     
           print("You added 2 num: ",a+b)
        else:
           print("You added 0 num: ", a)
a=Studennt()
a.sum(2,3,4)
a.sum(3,5)
a.sum(2)
''' OUTPUT:
You added 3 num:  5
You added 2 num:  8
You added 0 num:  2''''



#EXCEPTION HANDLING WITH THE TRY , EXPECT , ELSE, FINALLYY
#questions 1
a=int(input("enter:"))
b=int(input("enter:"))
 
try:
   c=a/b
   print(c)
except Exception as e:
    print("Handeled")
finally:
    print("DONEE")




#Expection questions 2 
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print(f"My name is {self.name} and my age is {self.age}")
class Emply(Person):
    def __init__(self, name, age,salary):
         super().__init__(name,age)
         self.salary=salary
    def disp(self):
        super().disp()
        print(f"Your slary will be: {self.salary}")

    def set_salary(self,salary):
        try:
            if (salary<0):
                print("Salary can`t be negative")
            else:
                self.salary=salary
        except:
            print("Handled")
person=Person("Alexa",56)
emply=Emply("Alice",83,3333)
emply.set_salary(-9)
person.disp()
emply.disp()
