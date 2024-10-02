class Programmers:
    def data(Microsoft):
        Microsoft.name=input("Enter the name of the the Microsoft Employee:")
        Microsoft.id=int(input("Enter programmer's id:"))
        Microsoft.designation=input("Enter their designation:")
    def display(Microsoft):
        print("Programeer's name:", Microsoft.name)
        print("Programeer's id:", Microsoft.id)
        print("Programeer's designation:", Microsoft.designation)
a=Programmers()
b=Programmers()
a.data()
b.data()
a.display()
b.display()
