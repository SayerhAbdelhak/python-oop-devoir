### act19 ex7: suite Fibonacci

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
print(Fibonacci(int(input('saisir l\'ordre de la suite Fibonacci a calculer :'))))