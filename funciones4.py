#hacer un programa que calcule el iva de un producto y calcule el valor a pagar
#el valor del producto debe ser enviado por argumento, utilizando una funcion.


def iva():
     costo=int(input("cual es el costo del producto: "))
     valor_iva=costo*0.19
     valor_pagar=costo+valor_iva
     print("el iva del producto es: " + str(valor_iva))
     print("el valor a pagar es: ", + valor_pagar)
iva()





#def iva(costo):
   
    #valor_iva=costo*0.19
    #valor_pagar=costo+valor_iva
   # print("el iva del producto es: " + str(valor_iva))
   # print("el valor a pagar es: ", + valor_pagar)
#costo=int(input("cual es el costo del producto: "))
#iva(costo)
