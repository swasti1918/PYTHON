class Employee:
    language = "Python"    ## This is a class attribute
    salary  = 1200000
    
swasti  = Employee()    
swasti.language= "JavaScript"   ## This is an instance attribute
print(swasti.salary,swasti.language)

