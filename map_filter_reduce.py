# map filter and reduce 

numbers = [2 , 3 ,4 ,5 ,6, 7]

double = lambda a : a * 2 

result = map(double, numbers)

print(list(result)) 

numCheck = [2,5,6,7,8,9]

result = filter(lambda a : a % 2 == 0 , numCheck)

print(list(result))

from functools import reduce 

expenses = [ 
    ("Dinner", 299),
    ("Lunch", 200)
]

sum = reduce(lambda a,b : a[1] + b[1] , expenses) 

print(sum)