def selectionsort(inp: list):
    for i in range(len(inp)):
        
        lowestLoc = i;
        for i2 in range(i + 1, len(inp)):
            if inp[i2] < inp[lowestLoc]:
                lowestLoc = i2;
        inp[i], inp[lowestLoc] = inp[lowestLoc], inp[i]
        print(inp)

    return inp;
pass;
print(selectionsort([8,2,3,7, 11, 89, 389, 263]));