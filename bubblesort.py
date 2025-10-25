sampl = []
import random
for i in range(500):
    sampl.append(random.randint(1, 100))
comparisons = 0
swaps = 0
for i2 in range(len(sampl) - 1):
    for i in range(len(sampl) - 1 - i2):
        item = sampl[i]
        comparisons += 1
        if item > sampl[i + 1]:
            swaps += 1
            sampl[i], sampl[i + 1] = sampl[i + 1], sampl[i]
        print(f"iteration {i2}")
       
   # print("")
       


print(comparisons,swaps, sampl)
