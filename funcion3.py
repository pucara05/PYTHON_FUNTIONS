# hacer un programa que calcule el iva de un producto y calcule el valor a pagar,
#utilizando una funcion.

def iva():
    costo=int(input("cual es el coto del produto: "))
    valor_iva=costo*0.19
    valor_pagar=costo+valor_iva
    print("el iva del producto es: " + str(valor_iva))
    print("el valor a pagar es: ", valor_pagar)


# cuerpo del programa
iva()
