import ast
ninja5jenis = ast.literal_eval(input())

terbaiktiapdivisi=[]

from BasicModul import NbElmt

def terbaik(x):
    for element in x:
        if type(element)==list:
            return terbaik(element), terbaik(x[1:])
        elif type(element)==list and NbElmt(element)==1:
            return terbaiktiapdivisi.append(element)
        else :
            return terbaiktiapdivisi.append(max(x))

terbaik(ninja5jenis)
print(sum(terbaiktiapdivisi)*1000000)