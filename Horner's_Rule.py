o=int(input("the order of equation:"))
x=int(input("the value of x:"))

equation=[]

for i in range(o+1):
    equation.append(int(input(f"The coefficient of x^{o-i}:")))

p=equation[0]
for i in range(1,o + 1):
    p=p*x+equation[i]

print(f"f(x)={p}")
