def addition (num1 , num2): 
    number1 = num1 
    number2 = num2 
    return number1 + number2 

print(addition(2,1)) 

def subtraction (num1 , num2 ): 
    number1 = num1 
    number2 = num2 
    return number1 - number2 

print(subtraction(9, 3)) 

def hello(name="any name"): 
    return "Hello " + name 

print(hello("Sam")) 

def phrase (phrase): 
        def say(word): 
            print (word)
        
        words = phrase.split(" ")
        for word in words: 
             say(word) 
 
phrase("I am going to buy milk") 

def counter(): 
     count = 0 
     def increment(): 
          nonlocal count 
          count +=  1 
          return count 
     return increment 

increment = counter()
print(increment())
print(increment())
print(increment())