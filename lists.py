list = ["Roger","Rob" ,20,"Neymar"]

list[2]="Gren"

print(list[2:4])
print(len(list))
print(list) 

list.append("Judaism")

print(list) 

list += ["Ronaldo", 20 ,"Popeyes"]

print(list)

list.remove("Ronaldo")
print(list)

print(list.pop()) 
list.insert(2, "Fandom")
print(list) 

list[3:3] = ["bitcoin","ethereum"]

print(list) 

list.remove(20)
# listcopy = list[:]
# list.sort(key=str.lower) 

# print(list)
# print(listcopy) 

print(sorted(list, key=str.lower))
print(list)
