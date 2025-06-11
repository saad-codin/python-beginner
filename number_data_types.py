# num = 3+2j 
num = complex(3,2)
print(num)

print(abs(2.2))

print(round(5.49))

from enum import Enum 

class State(Enum): 
    ACTIVE =  1 
    INACTIVE = 0 

print(State.INACTIVE.value)
print(list(State))