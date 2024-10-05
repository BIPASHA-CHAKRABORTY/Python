#1
x=int(input("Enter the value:"))
y=int(input("Enter the value:"))
c=int(input("Enter the value:"))
d=int(input("Enter the value:"))
z=int(input("Enter the value:"))

m=(2*x*y)/(c+10) -x/4*(z+d)
print(m)
#2
area=0
length = 0
breadth = 0
length=eval(input("Enter the Length of Rectange:"))
breadth=eval(input("Enter the Breadth of Rectangle:"))
area= length * breadth                  
print(f"Area of Rectangle = {area}")

3
e=int(input("Enter the 100 rs note:"))
d=int(input("Enter the 500:"))
z=int(input("Enter the 1000:"))
y=100*e
print(f"Total amount of 100s:{y}")
x=500*d
print(f"Total amount of 100s:{x}")
h=1000*z
print(f"Total amount of 100s:{h}")
Total=x+h+y
print(f"Total amount :{Total}")
 
#4
n=4
for i in range(1,n+1):
   print(*range(1,i+1))
for i in range(n-1,0,-1):
   print(*range(1,i+1))

#5
n=4
for i in range(1,n+1):
   print("*"*i)
for i in range(n-1,0,-1):
   print("*"*i)

#6
def charles_babbage():
   for i in range(0,6):
      T=i**2 + i+ 41
      print("i=",i,"T=",T)
charles_babbage()

#7
count = 35
for x in range(0,10):
   count = count - 1
   if x == 2:
    break
print(count)

#8
My_str = "I LOVE PHYTHON"
count = 0
for char in My_str:
   if char == "O":
     continue
   else:
     count = count + 1
print(count)

#9
i=0
total=0
while(i<=500):
  total+=i
  i+=5
print(f"Sum of every fifth number from 0 to 500 : {total}")


#10
for attempt in range(3):
  password=input("Enter the system password:")
  if(password=="Welcome to Python Programming"):
    print("Hurray , welcome backk")
    break
  print("Wrong password ....Try again !!! ")
else:
    print("Attempts run out")

#11
def dec_bin(num):
    return bin(num)[2:]
num=int(input("Enter a number:"))
print(f"Binary number of {num}: {dec_bin(num)}")


#12
def reverse_number(a):
    return int(str(a)[::-1])
 
a= input("Enter a number:")
print(f"The actual number you entreed: {a}")
print(f"Reverse the the entered number : {reverse_number(a)}")
