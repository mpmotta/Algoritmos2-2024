#fibonacci Iterativo

def fiboREC(n):
    if n <= 1:
        return n
    else:
        return fiboREC(n-1) + fiboREC(n-2)

def show(n):
    print("Fibonacci Recursivo:")
    lista = [str(fiboREC(i)) for i in range(n)] 
    print(" - " . join(lista)) 

termos = 8
show(termos)              