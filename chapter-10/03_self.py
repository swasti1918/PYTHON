class Employee:
    language = "Python"    ## This is a class attribute
    salary  = 1200000
    
    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
        
    @staticmethod    ### this shows without add self fxn this greet statement
    def greet():
        print("Good morning!")
    
swasti  = Employee()    
swasti.language= "JavaScript"   ## This is an instance attribute
swasti.greet()
swasti.getInfo()
# Employee.getInfo(swasti)

