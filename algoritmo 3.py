cont=1
i=int(input("ingrese un numero: "))
if i >0:
    while cont <= 12:
         tabla=cont*i
         print(cont,"x",i,"=",tabla)
         cont +=1
else:
    print("NUMERO INCORRECTO")
