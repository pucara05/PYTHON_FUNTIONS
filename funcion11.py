#crear un menu por medio de una funcion para ejecutar diferentes programas



#funciones

def menu():
    print("\n")
    print("menu de programas con funciones")
    print("-------------------------------")
    prnt("\n seleciona una opcion")
    print("\n 1 - mayor o menor de edad")
    print("\n 2 - valor a pagar")
    print("\n 3 - descuentos")
    print("\n 4 - valor total de la compra")
    print("\n 0 - salir")
    print("\n")

    def mayor_menor():
        edad=int(input("digite su edad: "))
        if(edad>=18):
            print("eres una persona mayor de edad")
        else:
                print("eres menor de edad")
#hacer una funcion que pida un valor de producto,
#una cantidad calcular el iva y el valor a pagar
                
def valor_pagar():
    monto=float(input("ingrese el monto a pagar: "))
    cantidad=int(input("digite la cantidad a pagar: "))
    valor_compra=monto+cantidad
    iva=valor_compra*0.19
    valor_pagar=valor_compra+iva
    print("su iva es: ", iva, " y su monto es: ", iva)

def descuento():
     #hacer una funcion que pida un numero de productos, si el costo total es,
     #mayor a 100.000 tiene descuento del 12%, de lo contrario tiene descuento,
     #del 5%.
 cantidad=int(input("digite la cantidad de produtos a comprar: ")
    for i in range(cantidad):
    costo=float(input("digite el valor del producto: " + str(i) + ": "))
    costos=costos+costo
     if costos>100000:
        descuento=costos*0.12
     else:
       descuentos=costos*0.05
       valor_pagar=costos-descuento
       print("el valor a pagar de los ", cantidad, " productos es: ", valor_pagar)
def costo_producto(valor_producto,cantidad):
    costoprod=valor_producto*cantidad
    return costoprod
def valor_total(a):
    descuento=a*0.05
    valor=a-descuento
    iva=valor*0.19
    valorTotalPagar=valor+iva
    print("el valor total a pagar es de: ", valorTotalPagar)
            
#cuerpo del programa
while true:
 menu()
try:
  opction=int(input("\ningrese el numero de la opcion escogida: "))
except:
    opcion=-1

if opcion==1:
     mayor_menor()
elif opcion==2:
    valor_pagar()
elif opcion==3:
    descuento()
    elif opcion==4:
#hacer una funcion que reciba el valor del producto y la cantidad y calcule el costo
#ese costo calculado enviarlo a otra funcion que calcule el descuento del 5% y a
#nuevo valor le saque el iva para calcular el valor total a pagar.
valor_producto=float(input("digite el valor del producto: "))
cantidad=int(input("digite la cantida a comprar: "))
costo_produto(valor_producto,cantidad)
a=costo_producto(valor_producto,cantidad)
valor_total(a)
elif opcion==0:
 break  
else:
 print("\n la opcion ingresada es incorrecta, indica una opcion valida")
