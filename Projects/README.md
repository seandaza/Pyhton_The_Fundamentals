Detalles de la Calculadora Porcentual de Prestamos

# Variables de la Funcion
m = Monto a Solicitar de Prestamo.
t  = Plazos en meses en los que se dispone pagar el préstamo.
i = Tasa de interés a la que se someterá el préstamo mensualmente.

# Expresiones Algebraicas y su Significado

1)  m/t  Representa el monto a pagar bruto por mes.

2)  (m/t)* i/100  Representa el porcentaje a pagar por concepto de interés bruto por mes.

3)  (m/t) + (m/t)* i/100  Representa el monto a pagar por mes MAS el interes del mismo.

    esta ultima expresión se puede factorizar sacando factor común y se obtiene:

                         (m/t)(1 + i/100)
    Y es la que usamos en el retorno de la función Calculadora().


# Ciclos y Condicionales

1)  La estructura de la lógica principal maneja un ciclo

                        while True 

    que permite la usuario volver a intentar el ciclo de operaciones hasta que lo haga de manera correcta.

2) De manera anidada se manejan condicionales del tipo

                        if (condición):
                                print("******")
                        else:
                                print("******")

    que me permiten tambien conducir el flujo correcto de la lógica en el primer caso, y en el segundo caso, muestra al usuario por consola que su debe corregir su ingreso de datos



# Manejo de Excepeciones

Como estamos pidiendo datos al usuario para alamcenarlos en variables que operaremos internamente a través de cálculos; debemos evitar que el usuario ingrese datos NO válidos, que puedan incurrir en errores internos en el flujo de nuestra lógica operacional. Para ello, usamos la siguiente estructura de datos:

                try:
                    i = float(input("Ingrese los intereses a someter el préstamo: "))

                except:
                    print("Ingresa un interes válido")

De tal manera que, en caso de que el usuario ingrese un dato no flotante, se mostrará al usuario por consola que el dato ingresado no es válido


# La Funcion Calculadora ()

Se define al inicio del código y recibe como parámetros justamente las variables monto, tiempo e interés. Esta función retorna la expresion que ya explicamos en la linea 14 de este documento.


                                def Calculadora(monto,tiempo, interes):

                                            return  (m/t)(1 + i/100)

Note que esta función dentro de nuestro flujo de código, se invoca en la linea 31 y sus parámetros son los que justamente hemos guardado en las variables m,t e i y que fueron pedidos como datos de ingreso al usuario interesado en el préstamo.