def sum_of_divisors(num): 
    divisors = [1] 

    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0: 
            divisors.append(i) 
            
            if i != num // i: 
                divisors.append(num // i) 
                return sum(divisors) 
    
def amicable(n): 
    while True: 
        n += 1
        sum1 = sum_of_divisors(n) 
        sum2 = sum_of_divisors(sum1) 
        if n != sum1 and n == sum2: return n 