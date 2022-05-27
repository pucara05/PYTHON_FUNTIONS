#hacer unprograma que determine is un numero es positivo o negativo
#y si es par o impar

#funciones
def parImpar(numero):
    if numero>0:
     if numero % 2==0:
       print("el numero es positivo y es par")
    else:
        print("el numero es positivo e impar")
else:
    if numero % 2==0:
         print("el numero es negativo y es par")
     else:
        print("el numero es negativo e impar")




#cuerpo del programa
numero=int(input("digite un numero: "))
parImpar(numero)
