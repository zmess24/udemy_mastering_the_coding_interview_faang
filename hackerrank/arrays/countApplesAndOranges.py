# https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count, orange_count = 0, 0
    for apple_distance in apples:
        apple_location = a + apple_distance
        if s <= apple_location and apple_location <= t:
            apple_count += 1
        
    print(apple_count)
    
    for orange_distance in oranges:
        orange_location = b + orange_distance
        if s <= orange_location and orange_location <= t:
            orange_count += 1
    
    print(orange_count)