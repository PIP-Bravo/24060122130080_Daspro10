import ast
bilangan = ast.literal_eval(input())

bilanganprima=[]

from BasicModul import NbElmt

def cekprima(x):
    for element in x:
        if type(element)==list:
            return cekprima(element), cekprima(x[1:])
        elif type(element)==list and NbElmt(element)==1:
            if (element >2 and element %2!=0 and element %3!=0) or element==3 or element==2:
                return bilanganprima.append(element)
            else:
                return 0
        else:
            if (element >2 and element %2!=0 and element %3!=0) or element==3 or element==2:
                return bilanganprima.append(element), cekprima(x[1:])
            else:
                return cekprima(x[1:])

cekprima(bilangan)
print(sum(bilanganprima))