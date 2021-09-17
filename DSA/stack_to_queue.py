def stack_to_queue(stack) :

    min1 = stack[0] 
    min2 = stack[0]
    min_idx1 = 0
    min_idx2 = 0
    
    for i, num in enumerate(stack) :
        if num < min1 :
            min2 = min1
            min_idx2 = min_idx1
            min1 = num
            min_idx1 = i 
        elif num < min2 :
            min2 = num
            min_idx2 = i 

    multiples1 = []
    multiples2 = []
    
    for num in stack :
        if (num > min1) and (num % min1 == 0) :
            multiples1.append(num)

        if (num > min2) and (num % min2 == 0) :
            multiples2.append(num) 

    if min_idx1 < min_idx2 :
       multiples1.extend(multiples2)
       return multiples1 
    else :
        multiples2.extend(multiples1)
        return multiples2
    
    
if __name__ == "__main__" :
    print(stack_to_queue([6, 12, 2, 15, 17, 3, 9]))
                