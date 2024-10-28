class Emp: # creating a class
    
    def put(self): #indentation is imp inside class
        self.id=int(input("Enter Employee Id:"))
        self.name=input("Enter Employee Name:") 
        
    def display(self):
        print("Employee id:.", self.id)
        print("Employee name:",self.name)
        
a=Emp() # calling an object 
a.put()
a.display()
