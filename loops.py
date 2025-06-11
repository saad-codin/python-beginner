# Loops  
condition = True
while condition == True: 
    print("This condition is True")
    condition = False 

# items = [1 , 2 , 3 , 4]
# for index, items in  enumerate(items):  
#     print(index, items) 


# items = [1 , "baloney", "misa", 4]
# for index, items in  enumerate(items):  
#     print(index, items) 


# for item in range(14): 
#     print(item)  

items = [1 , 2, 3 ,4 ,5]
for item in items: 
    if item == 2:
        continue 
    print(item) 


items = [1 , 2, 3 ,4 ,5]
for item in items: 
    if item == 2:
        break 
    print(item) 