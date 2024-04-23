# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    hashTable = {}
    pairs = 0
    for sock in ar:
        if sock in hashTable:
            hashTable[sock] += 1
            if hashTable[sock] % 2 == 0: 
                pairs += 1
        else:
            hashTable[sock] = 1
    
    return pairs