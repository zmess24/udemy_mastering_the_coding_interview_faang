# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def jumpingOnClouds(c):
    index, jumps = 0, 0
    
    while index < len(c) -1:
        if index + 2 < len(c):
            if c[index + 2] == 0:
                index = index + 2
            else:
                index = index + 1
        else:
            index = index + 1
        
        jumps = jumps + 1
    
    return jumps