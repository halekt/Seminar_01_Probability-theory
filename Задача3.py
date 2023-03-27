from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 

P=combinations(9,3)/combinations(15,3)
print(f'P(3 из 3-х окрашены) = {round(P,4)}')

