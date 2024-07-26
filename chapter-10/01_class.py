# class Employee:
#     name = "Swasti"
#     language = "Py"
#     salary  = 1200000
    
# swasti  = Employee()        ## Swasti is a object
# print(swasti.name,swasti.language)

class Employee:
    language = "Py"    ## This is an class attribute
    salary  = 1200000
    
swasti  = Employee()    ## Swasti is a instance attribute
swasti.name = "Swasti"
print(swasti.name,swasti.language)

sam = Employee()
sam.name = "Sam"
print(sam.salary,sam.language)

## Here name is instance attribute and salary and lang. are 
# class attributes as they directly belong to the class