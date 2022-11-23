import ast
bilangan = ast.literal_eval(input())

bilanganganjil=[]

from BasicModul import NbElmt

def cekganjil(x):
    for element in x:
        if type(element)==list:
            return cekganjil(element), cekganjil(x[1:])
        elif type(element)==list and NbElmt(element)==1:
            if element %2!=0:
                return bilanganganjil.append(element)
            else:
                return 0
        else:
            if element %2 !=0:
                return bilanganganjil.append(element), cekganjil(x[1:])
            else:
                return cekganjil(x[1:])

cekganjil(bilangan)
print(sum(bilanganganjil))