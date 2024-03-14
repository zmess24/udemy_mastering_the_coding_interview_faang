# https://www.algoexpert.io/questions/nth-fibonacci

def getNthFib(n: int, seq = { 1: 0, 2: 1 }):
    if n in seq:
        return seq[n]
    else:
        seq[n] = getNthFib(n-1, seq) + getNthFib(n-2, seq)
        return seq[n]