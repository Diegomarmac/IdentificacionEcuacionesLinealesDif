import espera as wait
import mensajes as msj

def checkIfIsSepOrVar(listToCheck,sliceToCheck):
    if listToCheck[0] == "y": # Reviso que esté escrita como yo quiero
        wait.pensar()
        if listToCheck[1] == "'":
            temporalMark  = sliceToCheck.index("y")
            temporalMark -= 1
            stop          = False

            if sliceToCheck.count("y") > 1:
                print(msj.separables)
                msj.IsSep()
            elif sliceToCheck.count("y") == 0:
                print(msj.errorCode)
            else:
                while stop == False:
                    if temporalMark == 0:
                        print(msj.errorCode)
                        stop = True 
                    elif sliceToCheck[temporalMark] == " ":
                        temporalMark -= 1
                    elif sliceToCheck[temporalMark] == "+":
                        if sliceToCheck[temporalMark - 1] == "x" or sliceToCheck[temporalMark - 2] == "x":
                            msj.IsVar()
                            stop = True
                        else: temporalMark -= 1
                    elif sliceToCheck[temporalMark] == "^":
                        print(msj.separables)
                        msj.IsSep()
                        stop = True
                    elif sliceToCheck[temporalMark] == "-":
                        if sliceToCheck[temporalMark - 1] == "^" or sliceToCheck[temporalMark - 2] == "^":
                            print(msj.separables)
                            msj.IsSep()
                            stop = True
                        elif sliceToCheck[temporalMark - 1] == "x" or sliceToCheck[temporalMark - 2] == "x":
                            msj.IsVar()
                            stop = True
                        else: temporalMark -= 1
                    elif sliceToCheck[temporalMark] == "x":
                        print(msj.separables)
                        msj.IsSep()
                        stop = True
                    elif sliceToCheck[temporalMark] == ")":
                        msj.IsVar()
                        stop = True
                    elif sliceToCheck[temporalMark] == "/":
                        temporalMark -= 1
                    elif sliceToCheck[temporalMark] == "y":
                        print(msj.separables)
                        msj.IsSep()
                        stop = True
                    else: temporalMark -= 1

        else: print(msj.errorCode)
    else: print(msj.errorCode)