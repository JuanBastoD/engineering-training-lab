"""
función que devuelva el N-ésimo número de Fibonacci (sin recursión).
"""
def fibonacci(x):
    if x==0:return 0
    elif x==1: return 1
    ant=0
    sig=1
    while x>1:
        fib=ant+sig
        ant=sig
        sig=fib
        x=x-1
    return fib
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))
        