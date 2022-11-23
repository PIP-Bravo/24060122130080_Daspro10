import ast
S= ast.literal_eval(input())
x= int(input())

from BasicModul import*

def bar(S):
    for element in S:
        if type(element)==list and NbElmt(S) !=1:
            return konso_LoL(bar(element), bar(S[1:]))
        if type(element)==list and NbElmt(S) ==1:
            return [bar(element)]
        if type(element)==list and NbElmt(element)==1:
            if element % x ==0:
                return []
            else:
                return S
        else:
            if element %x == 0 and NbElmt(S)!=1:
                return bar(MultiRember(element,S))
            if element %x == 0 and NbElmt(S)==1:
                return Rember(element,S)
            else:
                if NbElmt(S)==1:
                    return [element]
                else:
                    return konso_LoL(element, bar(S[1:]))

print(bar(S))