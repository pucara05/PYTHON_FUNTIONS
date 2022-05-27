#hacer un programa que pida dos numeros y le calcule las 2 operaciones basicas
#por medio de una funcion o funciones.

def operaciones(num1,num2):
    
    suma=num1+num2
    resta=num1-num2
    multiplicar=num1*num2
    dividir=num1/num2
    print("los numeros son ", num1, " y ", num2)
    print(" la suma de los dos numeros es: ", suma)
    print(" la suma de los dos numeros es: ", resta)
    print(" la suma de los dos numeros es: ", multiplicar)
    print(" la suma de los dos numeros es: ", dividir)
num1=float(input("digite su numero 1: "))
num2=float(input("digite su numero 2: "))
operaciones(num1,num2)



