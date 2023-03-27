from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k))) 


m=combinations(13, 4)
print(f'm = {m}')

n=combinations(52, 4)
print(f'n = {n}')

P=m/n
print(f'P(4 крести) = {round(P,4)}')


n=combinations(52, 4)
print(f'n = {n}')
m=sum([combinations(4,1)*combinations(48,3),combinations(4,2)*combinations(48,2),combinations(4,3)*combinations(48,1),1])
print(f'm = {m}')
P=m/n
print(f'P(хотя бы 1 туз) = {round(P,4)}')