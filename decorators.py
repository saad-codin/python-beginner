# Decorators 
def logtime(func): 
    def wrapper():
        val = func()
        print("Before change" ,val) 
        val = 2 * val
        print("After change" , val) 
        return val 
    return wrapper 

@logtime 
def number():  
   return int(input("Enter any number"))
   
number()

        