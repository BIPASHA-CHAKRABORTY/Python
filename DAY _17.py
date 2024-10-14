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
You added 0 num:  2


''''


