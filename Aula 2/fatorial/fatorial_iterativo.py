#Fatorial Iterativo
def fatorialIT(x):
    fat = 1
    for i in range(1, x+1):
        fat = fat * i
    return fat

num = 19

res = fatorialIT(num)

print("Cálculo Fatorial Iterativo:")
fatores = list(range(1, num+1))

for i in range(num-1, -1, -1):
    print(" " + str(fatores[i]), end="")
    if i > 0:
        print(" *", end="")
        
print(" = " + str(res))        