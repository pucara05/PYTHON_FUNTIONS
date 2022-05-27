#hacer un programa que muestre los 
def menu():
    print("\n")
    print("programa para registro de partidos uis")
    print("-------------------------------")
    prnt("\n seleciona una opcion")
    print("\n 1 - regristar partido")
    print("\n 2 - ver resultados")
    print("\n 3 - tabla de clasificacio")
    print("\n 0 - salir")
    print("\n")

def entrarDia():
    while true:
        try:
            print("\n")
            print("*** ingrese la fecha del partido ***")
            print("\n")
            dia=int(input("digite el dia (1-31): "))
            if dia>0 and dia<32:
                   return dia
            else:
                    print("debe ingresar un dia valido!!!")
        except:
            print("la fecha debe tener un valor numerico")

def entrarMes():
    while true:
        try:
            mes=int(input("digite el mes (1-12): "))
            if mes>0 and dia<13:
                   return mes
            else:
                    print("debe ingresar un mes valido!!!")
        except:
            print("el dia debe tener un valor numerico")
            
def entrarAño():
    while true:
        try:
            año=int(input("digite un año mayor a 2021 (>2021): "))
            if año>=0:
                   return año
            else:
                    print("debe ingresar un año valido!!!")
        except:
            print("el año debe tener un valor numerico")
def entarRival():
    while true:
        rival=input("ingrese el nombre del equipo rival: ")
        if rival=="":
            print("el nombre no puede estar vacio!!!")
        else:
            return rival

def entrarGolRival():
    while true:
        try:
            golrival=int(input("ingrese los goles del equipo rival: "))
            if golrival>=0:
                return golrival
            else:
                print("no puede ingresar valores negativos !!!")
        except:
            print("el gol debe tener un valor numerico")
            
def entrarGolUisl():
    while true:
        try:
            goluis=int(input("ingrese los goles de la uis: "))
            if goluis>=0:
                return goluis
            else:
                print("no puede ingresar valores negativos !!!")
        except:
            print("el gol debe tener un valor numerico")
def verResultados(lista):
     print("\n")
     print("*** resultados de los partidos ***")
     for i in lista:
         print("\n (str(i,[0]))+"-")+str(i[1])+"-"+str(i[2])+"     "+str(i[3])+"  - "+str(i[4])+"-----"+str(i[6])+" -"+str(i[5]")
def clasificacio(lista):
    jugados=len(lista)
    ganados=0
    empatados=0
    perdidos=0
    puntos=0

    for i in range(0,jugados):
        if(lista[i][6]>lista[i][4]):
            ganados=ganados+1
            puntos=puntos+3
        elif(lista[i][6]==lista[i][4]):
            empatados=empatados+1
            puntos=puntos+1
        else:
            perdidos=perdidos+1
    print("\n ")
    prit("*** tabla de clasificacion de la uis ***")
    print("-----------------------------------------")
    print("\t partidos jugados:   ", jugados)
    print("\t partidos ganados:   ", ganados)
    print("\t partidos empatados:   ",empatados)
    print("\t partidos perdidos:   ", perdidos)
    print()
    print("\t puntos obteidos:    ", puntos, " puntos")

    return true


    
partidos=[]
          
while true:
 menu()
try:
  opction=int(input("\ningrese el numero de la opcion escogida: "))
except:
    opcion=-1

if opcion==1:
    resp="s"
    while resp=="s" or resp=="s":
        partidos.append(entrarDia(), entrarMes(), entrarAño(), entrarRival(),
         entrarGolRival(), "uis", entrarGolUis())
        resp=input("\n ¿desea regristar potro partido? (s/n): ")
    # este print(partidos)es para probar que se ejecuta bien
        print(partidos)
elif opcion==2:
    verResultados(partidos)
        
    
elif opcion==3:
    clasificacio(partidos)
   
elif opcion==4:

elif opcion==0:
 break  
else:
 print("\n la opcion ingresada es incorrecta, indica una opcion valida")
