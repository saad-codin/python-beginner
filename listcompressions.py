# List compressions 
numbers = [1, 2,  3, 4, 5]

numbers_power_2 = list([n**2 for n in numbers])

(print(numbers_power_2)) 

numbers = [1,2,3,4,5,6,7]
numbers_power_2 = []
for n in numbers: 
    numbers_power_2.append(n**2)

print(numbers_power_2) 


numbers = [2,5,8] 

numbers_power_2 = list(map(lambda n: n**2 , numbers))

print((numbers_power_2))