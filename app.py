import espera          as wait
import mensajes        as msj
import primeraBusqueda as pB
import segundaBusqueda as sB

msj.welcome() #Inicio del programa :)
equation      = input ("Ingrese la ecuacion: ")
endOfSlice    = equation.index("=")
leftFunction  = equation[:endOfSlice]
rightFunction = equation[endOfSlice:]

if equation.count("=") == 0: print(msj.errorCode) # manejo de entradas incorrectas, reviso que haya uno y solo un signo de igual
elif equation.count("=") > 1: print(msj.errorCode)
else:
    if equation.index("=") == 3: 
        pB.checkIfIsSepOrVar(equation, rightFunction)
    elif equation.index("=") == 1:
        sB.decisionEOrT()
    elif equation.index("=") == 2:
        if equation[0]:
            sB.decisionEOrT()
        else: pB.checkIfIsSepOrVar(equation, rightFunction)
    else:
        wait.pensar()
        if "'" in leftFunction:
            print("la funcion Q está del lado derecho")
            sB.checkIfIsBOrL(rightFunction)
        elif "'" in rightFunction: 
            print("la funcion Q está del lado izq.")
            sB.checkIfIsBOrL(leftFunction)
        else: print(msj.errorCode)