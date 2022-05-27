#crear un menu por medio de una funcion para ejecutar diferentes programas



#funciones

def menu():
    print("\n")
    print("menu de programas con funciones")
    print("-------------------------------")
    prnt("\n seleciona una opcion")
    print("\n 1 - mayor o menor de edad")
    print("\n 0 - salir")
    print("\n")

    def mayor_menor():
        edad=int(input("digite su edad: "))
        if(edad>=18):
            print("eres una persona mayor de edad")
        else:
                print("eres menor de edad")

#cuerpo del programa

 while true:
     menu()
     try:
         opction=int(input("\ningrese el numero de la opcion escogida: "))
         except:
             opcion=-1

             if opcion==1:
                 mayor_menor()
                 elif opcion==0:
                     break
                    else:
 print("\n la opcion ingresada es incorrecta, indica una opcion valida")
