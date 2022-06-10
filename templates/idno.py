from random2 import *
def idno():
    str="7545"
    ran=""
    for i in range(4):
        ran=ran+"% s" %randint(0,9)
    return(str+ran)
