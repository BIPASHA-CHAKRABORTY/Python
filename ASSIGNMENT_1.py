#Q1
area=0
length = 0
breadth = 0
length=eval(input("Enter the Length of Rectange:"))
breadth=eval(input("Enter the Breadth of Rectangle:"))
area= length * breadth
print(f"Area of rectangle:",{area})
#Q2
a=int(input("Enter eng marks:"))
b=int(input("Enter hindi marks:"))
c=int(input("Enter eng marks:"))
d=(a+b+c)/3
print(d)
#Q3 Calculate the sum of 4 input digit
a = input("Enter any 4 digit number:")  
c = 0 
for i in range(0, 4):
    b = a[i]  
    c = c + int(b)  
print(f"Sum:{c}")

#q4
distance=int(input("Enter the distance between two cities in kilometers:"))
meter=distance*1000
print(f"Distance in meter:{meter} m")
centimeter=distance*100000
print(f"Distance in centimeter:{centimeter} cm")
miles=distance*0.6213
print(f"Distance in miles:{miles} miles")

#q5
weight=int(input("Enter the weight in kg:"))
pound=weight*2.20
print(f"Weight in Pound: {pound}")
tonne=weight*0.001
print(f"Weight in toone: {tonne}")
#q6
distance=int(input("Enter distance in meter:"))
time=int(input("Enter time in seconds:"))
speed=distance/time
print(f"Speed:{speed}")
#q7
radius=int(input("Enter the radius:"))
volume=4/3*3.14*radius**3
print(f"Volume of the sphere:{volume}")
#q8
a=int(input("Enter the no. of 100 rs notes you want to withdraw:"))
b=int(input("Enter the no. of 500 rs notes you want to withdraw:"))
c=int(input("Enter the no. of 1000 rs notes you want to withdraw:")) 
d=a*100
e=b*500
f=c*1000
total=d+e+f
print(f"TOTAL AMOUNT:{total}")