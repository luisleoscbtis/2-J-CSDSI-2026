def height(n, m):
    if n == 0 or m == 0:
        return 0
    
    floors = 0
    binom = 1
    for i in range(1, min(n, m) + 1):
        binom = binom * (m - i + 1) // i
        floors += binom
    
    return floors