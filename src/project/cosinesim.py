import math
#menghitung cosine similarity
def sim(arrA, arrB):
    dot = 0
    sumA = 0
    sumB = 0

    for i in range (len(arrA)):
        dot += arrA[i] * arrB[i]
        sumA += arrA[i] * arrA[i]
        sumB += arrB[i] * arrB[i]

    akar = math.sqrt(sumA*sumB)
    if (akar == 0):
        akar = 1
    
    return dot/akar