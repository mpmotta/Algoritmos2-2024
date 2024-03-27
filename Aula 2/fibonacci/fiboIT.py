#fibonacci Iterativo

def fiboIT(n):
    F = 0
    ant = 0

    for i in range(1, n + 1):
        if i == 1:
            F = 1
            ant = 0
        else:
            F += ant
            ant = F - ant
    return F

def show(n):
    print("Fibonacci Iterativo:")
    lista = [str(fiboIT(i)) for i in range(n)] 
    print(" - " . join(lista)) 

termos = 18
show(termos)              