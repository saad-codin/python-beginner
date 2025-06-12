# Exceptions 
try: 
    result = 2 / 0 
except ZeroDivisionError: 
    print("Cannot be divided by zero!")

finally: 
    result = 1 

print(result) 

# filename = "game" 

# with open(filename , "game") as file: 
#     content = file.read()
#     print(content)

