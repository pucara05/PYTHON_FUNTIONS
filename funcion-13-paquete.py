# una empresa requiere discriminar si un paquete puede ser enviado o no de acuerdo a su
#peso y su volumen. la empresa considera que el paquete puede ser enviado si su peso es
#menor a 2 kg y si  su volumen es menor a 0.027 m3.
#escriba una funcion llamada procesar_dato que reciba dos datos: el peso y el volumen de
# un paquete (el primer parametro recibido por la funcion debe ser el peso y el segundo
#el volumen). esta funcion debe retornar verdadero si el paquete puede ser enviado y
#retornar falso si el paquete no puede ser enviado

#funciones

def procesar_dato(peso,volumen):
    if peso<2 and volumen<0.027:
        return true
    else:
        return false
procesar_dato(5,3)
    
