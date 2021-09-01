"""
Calculadora que permita obtener los intereses sobre un monto variable de prestamo.
Debe incorporar una funcion implicita que reciba al monto del prestamo, al tiempo(en meses como plazos de pago) y la tasa de interes como parametros. Esta funcion debe retornar la cantidad a pagar por cada cuota y la cantidad de cuotas a pagar.
"""

def Calculadora(monto,tiempo,interes):
    
    return  (monto/tiempo)*(interes/100 + 1)   

while True:
    try:
            m = int(input("Ingrese un Monto a Solicitar de Prestamo: "))
            if m > 0:
                print("________________________________________________")
                print("Su monto de solicitud credito es de",m,"$\n")

                while True:
                    try:
                        t = int(input("Ingrese la cantidad de meses de plazo para pagar: "))
                        if t > 0:
                            print("________________________________________________")
                            print("Plazo de",t,"meses para pagar\n")

                            while True:
                                try:
                                    i = float(input("Ingrese los Intereses a someter el prestamo: "))
                                    if i > 0:
                                        print("________________________________________________")
                                        print("Los intereses a cobrar por cada mes son de: ",i,"%\n")
                                        print("________________________________________________________________________________________")
                                        print("Ud debe pagar mensualmente un monto de",Calculadora(m,t,i),"$ por un total de",t,"meses")
                                        print("________________________________________________________________________________________")
                                        break
                                    else:
                                        print("Los intereses den ser positivos!")
                                except:
                                    print("Ingresa un monto de interes valido!")
                            break
                        else:
                            print("El plazo debe ser un numero entero positivo!")
                    except:
                        print("Ingresa un Plazo valido")
                break
            else:
                print("El monto a solcitar debe ser Positivo! Intente de nuevo...")
    except:
        print("Oops! Ese no es un monto valido!. Intenta de nuevo...")
