# Sets  
set1 = {"Roger","Sydney"}
set2 = {"Roger"}
set3 = {"Navine"}

intersect = set1 & set2 
print(intersect) 

union = set1 | set2 | set3
print(union) 

difference = set1 - set2
print(difference) 

subset = set1 > set2 
print(subset) 

print(len(set1)) 
print(list(set1))