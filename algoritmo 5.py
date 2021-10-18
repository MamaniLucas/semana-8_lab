cont=1
n=int(input("Ingrese un numero: "))
if n>0:
    while cont <= 12:
        x=cont *n
        print(cont, "*",n,"=",x)
        cont +=1
else:
    print("numero incorrecto")
    