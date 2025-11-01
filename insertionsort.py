sampl = []
import random
for i in range(5):
    sampl.append(random.randint(1, 10))
sampl = [6, 5, 3, 9, 5]
print( sampl)

for i in range(1, len(sampl)):
    key = sampl[i]
 
    j = i - 1
    while  sampl[j] > key and j >= 0:
        
        sampl[j + 1] = sampl[j]
        j-=1
    sampl[j + 1] = key
    print(sampl)
    

print(sampl)