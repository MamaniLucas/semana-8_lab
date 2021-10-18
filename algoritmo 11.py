contador=1
factorial=1
i=int(input("Ingresa un numero: "))
while contador <= i:
    factorial = factorial * contador
    contador += 1
print (factorial)