import ast
belipermen = ast.literal_eval(input())

jumlahyangdibayar=[]

def hitunguntung(x):
    for element in x:
        if type(element)==list:
            if sum(element) %2 == 0:
                return jumlahyangdibayar.append(sum(element)*2000), hitunguntung(x[1:])
            if sum(element) %2 != 0:
                return jumlahyangdibayar.append(sum(element)*1000), hitunguntung(x[1:])
        else :
            if element %2 == 0:
                return jumlahyangdibayar.append(element*4000), hitunguntung(x[1:])
            if element %2 != 0:
                return jumlahyangdibayar.append(element*3000), hitunguntung(x[1:])


hitunguntung(belipermen)
print(sum(jumlahyangdibayar))
            
