def is_armstrong_number(number):
    k = number
    j = 0
    while k > 0:
       k=k//10
       j += 1
    
    k = number
    sum = 0
    while k>0:
        sum = (k%10) ** j + sum
        k=k//10
    
    if sum == number:
        return True
    else:
        return False
    
