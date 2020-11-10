from removeduplicate import removeduplicatex
from jumlahkata import jumlahKata
from cosinesim import sim

def inputKata(b):
    i = 0
    count = 0
    for word in b.split():
        count += 1

    new = ['' for i in range (count)]

    for word in b.split():
        new[i] = word
        i += 1
    
    return new

def listToString(s):  
    str1 = ""  
    for i in s:  
        str1 += i   
    # return string   
    return str1  

def gabungarray(first,add):
    size = len(first) + len(add) - 1
    newarr = ['' for i in range (size)]
    for i in range(len(first)):
        newarr[i]=first[i]
    for i in range(len(first),size):
        newarr[i]=add[i-len(first)]

    return newarr

def removeduplicatex(T):
    M = []

    for string in T:
        if string in M:
            continue
        M.append(string)

    return M

def jumlahKata(T, Q):
    C = [0 for i in range(len(Q))]
    for i in range(len(Q)):
        for j in range(len(T)):
            if T[j] == Q[i]:
                C[i] += 1
    return C
