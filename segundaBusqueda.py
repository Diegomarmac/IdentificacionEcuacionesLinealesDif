import espera as wait
import mensajes as msj

#  function to check if is bernoulli or LDE
def checkIfIsBOrL(sliceToCheck):
    if "y" in sliceToCheck:
            temporalSliceCut = sliceToCheck.index("y")
            temporalSliceOFQ = sliceToCheck[temporalSliceCut:]
            if "^" in temporalSliceOFQ:
                wait.pensar()
                print(msj.bern)
                msj.IsBern()
            else:
                wait.pensar()
                print(msj.bernA)
                msj.IsBern()
    else:
        print(msj.lDE)
        msj.IsLDE()

# función de ingreso si o no
def decisionEOrT():
    wait.pensar()
    print("Necesito de tu ayuda para poder decidir que tipo de ecuacion es")
    decision = input ("Ayudame, tiene constantes tanto en M(x,y) como en N(x,y) ? \n favor de responder con y para si o con n para no: \n")
    if decision == "y":
        msj.IsTras()
    elif decision == "n":
        msj.IsExact()
    else:
        print(msj.errorCode)