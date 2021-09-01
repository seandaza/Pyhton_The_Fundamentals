"""
Calculadora que permite obtener los intereses sobre un monto variable de préstamo.
Incorpora una función implícita que recibe al monto del préstamo, al tiempo(en meses como plazos de pago)
y la tasa de interés como parámetros. Esta función debe retornar la cantidad a pagar por cada cuota y la 
cantidad de cuotas a pagar.
"""

def Calculadora(monto,tiempo,interes):
    
    return  round((monto/tiempo)*(interes/100 + 1),2)

while True:
    try:
            m = int(input("Ingrese un Monto a Solicitar de Préstamo: "))
            if m > 0:
                print("Su monto de solicitud crédito es de",m,"$\n")

                while True:
                    try:
                        t = int(input("Ingrese la cantidad de meses de plazo para pagar: "))
                        if t > 0:
                            print("Plazo de",t,"meses para pagar\n")

                            while True:
                                try:
                                    i = float(input("Ingrese los Intereses a someter el préstamo: "))
                                    if i > 0:
                                        print("Los intereses a cobrar por cada mes son de: ",i,"%\n")
                                        print("________________________________________________________________________________________")
                                        print("Ud debe pagar mensualmente un monto de",Calculadora(m,t,i),"$ por un total de",t,"meses")
                                        print("________________________________________________________________________________________")
                                        break
                                    else:
                                        print("Los intereses den ser positivos!. Intenta de nuevo...")
                                except:
                                    print("Ingresa un monto de interes válido!. Intenta de nuevo...")
                            break
                        else:
                            print("El plazo debe ser un numero entero positivo!. Intenta de nuevo...")
                    except:
                        print("Ingresa un Plazo válido. Intenta de nuevo...")
                break
            else:
                print("El monto a solcitar debe ser Positivo!. Intenta de nuevo...")
    except:
        print("Oops! Ese no es un monto válido!. Intenta de nuevo...")