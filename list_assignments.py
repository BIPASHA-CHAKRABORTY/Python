#QUESTION_1
L1=[1,"x",4,5.6,"z", 9, "a", 0, 4]
integers_only = []
for item in L1:
    if type(item) == int:
        integers_only.append(item)

print(integers_only)
#QUESTION_2
celsius_values = [0, 20, 37, 100, -10]
fahrenheit_values = []
for c in celsius_values:
    f = (c * 9/5) + 32
    fahrenheit_values.append(f)
print(fahrenheit_values)
