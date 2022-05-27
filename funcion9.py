#hacer un programa con 4 funciones para calcular la definitiva  de un estudiante,
#la cual  se debe calcular asi:
#4 notas de quices(una funcion)
#3 notas de trabajos (una funcion)
#2 notas de parciales (una funcion)
#calcular la definitiva por medio de una funcion


#funciones
def quices():
    quiz_1=float(input("digite la nota del quiz #1: \n-->"))
    quiz_2=float(input("digite la nota del quiz #2: \n-->"))
    quiz_3=float(input("digite la nota del quiz #3: \n-->"))
    quiz_4=float(input("digite la nota del quiz #4: \n-->"))
    definitivaQ=(quiz_1+quiz_2+quiz_3+quiz_4)/4
    return definitivaQ

def trabajos():
    trabajo_1=float(input("digite la nota del trabajo #1: \n-->))
    trabajo_2=float(input("digite la nota del trabajo #2: \n-->))
    trabajo_3=float(input("digite la nota del trabajo #3: \n-->))
    definitivaT=(trabajo_1+trabajo_2+trabajo_3)/3
     return definitivaT                     
def parciales():
    parcial_1=float(input("digite la nota del parcial #1: \n-->))
    parcial_2=float(input("digite la nota del parcial #2: \n-->))
    definitivaP=(parcial_1+parcial_2)/2
    return definitivaP                      
#cuerpo del programa
Q=quices()
T=trabajos()
P=parciales()                          
definitivaTotal=(Q+P+T)/3
print("la definitiva del estudiantes es: ", definitivaTotal)
