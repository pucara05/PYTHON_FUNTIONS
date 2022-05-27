#se requiere hacer la conversion de pesos colombianos a euros
#escriba una funcion llamada peso_a_euro que reciba como dato de entrada
#el valor a convertir.
#considerar que 1 euro equivale a la fecha a 4500 cop (pesos colombianos)


def peso_a_euro(valor):
    euros=valor/4500
    return euros
    peso_a_euro(50000)
#quitar el print ya que no se necesita en la funcion
#solo se puso para correr el programa y probar
#cuerpo programa
print(peso_a_euro(50000))
