import sys

op1=float(sys.argv[1])
op=sys.agrv[2]
op2=float(sys.argv[3])

def addition(nb1,signe,nb2):
    if signe=='+':
        return nb1+nb2
    return None

def soustraction(nb1,signe,nb2):
    if signe=='-':
        return nb1-nb2
    return None

def multiplication(nb1,signe,nb2):
    if signe=='*':
        return nb1*nb2
    return None