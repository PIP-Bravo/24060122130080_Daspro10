def tail(L):
    return L[1::]

def konsi(S,L):
   if L==[]:
     return [S]
   else :
     return L+[S]

def konso(S,L):
   if L==[]:
     return [S]
   else :
     return [S]+L

def inverse(L):
    if is_empty(L):
        return []
    else :
        return konsi(L[0], inverse(tail(L)))

def is_member(L,x):
    if is_empty(L):
        return False
    else:
        if L[0]==x:
            return True
        else:
            return is_member(tail(L),x)

def Rember(x,L):
    if is_empty(L):
        return L
    else:
        if L[0]==x:
            return tail(L)
        else:
            return konso(L[0],Rember(x,tail(L)))

def MultiRember(x,L):
    if is_empty(L):
        return L
    else:
        if L[0]==x:
            return MultiRember(x,tail(L))
        else:
            return konso(L[0],MultiRember(x,tail(L)))

def is_set(L):
    if is_empty(L):
        return True
    else:
        if is_member(tail(L),L[0]):
            return False
        else:
            return is_set(tail(L))

def make_set(L):
    print(L)
    if is_empty(L):
        return L
    else:
        if is_member(tail(L),L[0]):
            return make_set(tail(L))
        else:
            return konso(L[0], make_set(tail(L)))

def is_subset(H1,H2):
    if is_empty(H1):
        return True
    else:
        if not(is_member(H2,H1[0])):
            return False
        else:
            return is_subset(tail(H1),H2)

def is_eq_set(H1,H2):
    return is_subset(H1,H2) and is_subset(H2,H1)



def is_empty(L):
    return L==[]

def NbElmt(S):
    if isinstance(S, list):
        return len(S)
    else:
        return 1

def is_one_element(L):
    if not(is_empty(L)):
        return len(L)==1

def is_empty_LoL(S):
    return S==[]

def is_atom(S):
    return not(is_empty_LoL(S)) and (NbElmt(S))==1

def is_List(S):
    return not(is_atom(S))

def konso_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return [L]+S

def konsi_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return S+[L]

def first_List(S):
    if not(is_empty_LoL(S)):
        return S[0]

def tail_List(S):
    if not(is_empty_LoL(S)):
        return S[1:]

def last_List(S):
    if not(is_empty_LoL(S)):
        return S[-1:]

def head_List(S):
    if not(is_empty_LoL(S)):
        return S[:-1]




def IsEqs(S1,S2):
    if is_empty_LoL(S1) and is_empty_LoL(S2) : 
        return True
    elif not is_empty_LoL(S1) and is_empty_LoL(S2) : 
        return False
    elif is_empty_LoL(S1) and not is_empty_LoL(S2) : 
        return False
    else :
        if is_atom(first_List(S1)) and is_atom(first_List(S2)):
            return first_List(S1)==first_List(S2) and IsEqs(tail_List(S1),tail_List(S2))
        if is_List(first_List(S1)) and is_List(first_List(S2)) and IsEqs(first_List(S1),first_List(S2)):
            return IsEqs(tail_List(S1), tail_List(S2))
        else:
            return False

def Ismember(A,S):
    if is_empty_LoL(S):
        return False
    if not is_empty_LoL(S):
        if is_atom(first_List(S)):
            return A == first_List(S)
        if is_List(first_List(S)):
            return Ismember(A, tail_List(S)) or Ismember(A, first_List(S))


def IsmemberLS(L,S):
    if is_empty_LoL(L) and is_empty_LoL(S):
        return True
    if not is_empty_LoL(L) and is_empty_LoL(S):
        return False
    if is_empty_LoL(L) and not is_empty_LoL(S):
        return False
    else :
        if (is_atom(first_List(S))):
            return IsmemberLS(L,tail_List(S))
        else:
            if IsEqs(L,first_List(S)):
                return True
            else :
                return IsmemberLS(L, tail_List(S))


def Rember(a,S):
    if is_empty_LoL(S):
        return S
    elif (is_atom(first_List(S)) and first_List(S)==a):
        return Rember(a, tail_List(S))
    elif (is_atom(first_List(S)) and first_List(S)!=a):
        return konso_LoL(first_List(S), Rember(a,tail_List(S)))
    elif is_List(first_List(S)):
        return konso_LoL(Rember(a,first_List(S)), Rember(a,tail_List(S)))

def max2(a,b):
    if a>=b:
        return a 
    else :
        return b 

def Max(S):
    if is_one_element(S):
        if is_atom(S):
            return first_List(S)
        if is_List(S):
            Max(first_List(S))
    else :
        if is_atom(S[0]):
            return max2(first_List(S), Max(tail_List(S)))
        if is_List(S[0]):
            return max2(Max(first_List(S)), Max(tail_List(S)))