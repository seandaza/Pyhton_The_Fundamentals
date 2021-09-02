"""
Calculadora que permite obtener los intereses sobre un monto variable de préstamo.
Incorpora una función implícita que recibe al monto del préstamo, al tiempo(en meses como plazos de pago)
y la tasa de interés como parámetros. Esta función debe retornar la cantidad a pagar por cada cuota y la 
cantidad de cuotas a pagar.
"""
# Declaramos nuestra función
def Calculadora(monto,tiempo,interes):
    """Esta función recibe como parámetro el monto a prestar, 
    el tiempo de plazo de los pagos y el interés al cuál será 
    sometido el préstamo durante dicho plazo de tiempo.                     

    Esta función retorna el monto a pagar por el usuario cada 
    mes de plazo, junto a sus respectivos intereses.
    """
    
    return  round((monto/tiempo)*(interes/100 + 1),2)      # Esta linea indica la expresión algebraica que regresará la función.

# Declaramos un ciclo dentro del cuál manejaremos exepciones.
# El ciclo While mantiene al usuario dentro dentro del esquema de solicitud en caso de ingresqr un dato inválido.
while True:
    try:
            m = int(input("Ingrese un Monto a Solicitar de Préstamo: "))   # Se castea a entero y se guarda en una variable m el monto solicitado.
            if m > 0:
                print("Su monto de solicitud crédito es de",m,"$\n")       #Se muestra por consola al usuario el monto solicitado.

                while True:
                    try:
                        t = int(input("Ingrese la cantidad de meses de plazo para pagar: "))     # Se castea a entero y se guarda en una variable t el tiempo de plazo.
                        if t > 0:
                            print("Plazo de",t,"meses para pagar\n")       #Se muestra por consola al usuario el tiempo de plazo del préstamo.

                            while True:
                                try:
                                    i = float(input("Ingrese los Intereses a someter el préstamo: "))       # Se castea a entero y se guarda en una variable i los intereses del préstamo.
                                    if i > 0:
                                        print("Los intereses a cobrar por cada mes son de: ",i,"%\n")        #Se muestra por consola al usuario los intereses del préstamo.
                                        print("________________________________________________________________________________________")
                                        print("Ud debe pagar mensualmente un monto de",Calculadora(m,t,i),"$ por un total de",t,"meses")   #Usamos la función que se definió al principio para que muestre el monto a pagar cada mes a partir de los datos m,t,e,i.
                                        print("________________________________________________________________________________________")
                                        break
                                    else:
                                        print("Los intereses den ser positivos!. Intenta de nuevo...")       # muestra por consola alerta de ingreso de dato inválido.
                                except:
                                    print("Ingresa un monto de interes válido!. Intenta de nuevo...")       # muestra por consola alerta de ingreso de dato inválido.
                            break
                        else:
                            print("El plazo debe ser un numero entero positivo!. Intenta de nuevo...")        # muestra por consola alerta de ingreso de dato inválido.
                    except:
                        print("Ingresa un Plazo válido. Intenta de nuevo...")        # muestra por consola alerta de ingreso de dato inválido.
                break
            else:
                print("El monto a solcitar debe ser Positivo!. Intenta de nuevo...")        # muestra por consola alerta de ingreso de dato inválido.
    except:
        print("Oops! Ese no es un monto válido!. Intenta de nuevo...")         # muestra por consola alerta de ingreso de dato inválido.