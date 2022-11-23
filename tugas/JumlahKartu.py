import ast
X = ast.literal_eval(input())

from BasicModul import*

def element(X):
    if is_empty(X):
        return 0
    elif is_List(X[0]):
        return element(first_List(X)) + element(tail_List(X))
    else:
        return 1 + element(tail_List(X))

print(element(X))