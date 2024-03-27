#Fatorial Recursivo
def fatorialREC(x):
    if x == 1:
        return 1
    return fatorialREC(x - 1) * x


num = 6

res = fatorialREC(num)

print("Cálculo Fatorial Recursivo:")
fatores = list(range(1, num+1))

for i in range(num-1, -1, -1):
    print(" " + str(fatores[i]), end="")
    if i > 0:
        print(" *", end="")
        
print(" = " + str(res))        