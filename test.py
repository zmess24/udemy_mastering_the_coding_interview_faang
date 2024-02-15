def sum_of_divisors(num):
    """Calculate the sum of proper divisors of a number"""
    sum_divisors = 1  # Start with 1 because it is a proper divisor of every number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:  # Add the pair divisor if it's not the square root
                sum_divisors += num // i
    return sum_divisors

def amicable(n):
    """Return the smallest amicable number greater than n"""
    current = n + 1
    while True:
        sum_div_current = sum_of_divisors(current)
        # Check if the sum of divisors forms an amicable pair with current and it's not the same number
        if sum_of_divisors(sum_div_current) == current and sum_div_current != current:
            return current
        current += 1