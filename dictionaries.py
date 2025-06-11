# Dictionaries 

dog = {"name":"Roger",  
       "color":"black",
        "age": 8} 

print(dog["name"])

dog["name"] = "Sydney"
print(dog) 

print(dog.get("color" , "brown")) 

# print(dog.popitem()) 

print("color" in dog) 

print(dog.keys()) 
print(list(dog.values()))
print(dog.items()) 

dog["favFood"] = "Meat"
print(dog) 
 
del dog["color"]

print(dog) 

dogCopy = dog.copy() 
dogCopy["color"] = "black"
print(dogCopy)