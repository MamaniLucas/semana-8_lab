div=0
cont=0
n=int(input("ingrese un numero: "))
while div <= n:
    div +=1
    if n%div==0:
       cont +=1
if cont ==2:
    print("es un numero primo")
else:
    print("es un numero no primo")