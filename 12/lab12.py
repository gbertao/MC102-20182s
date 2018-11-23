#!/usr/bin/python3
def swap(array, ori, dest):
    aux = array[ori]
    array[ori] = array[dest]
    array[dest] = aux

def Verify(array):
    for i in range(0, len(array) - 1):
        if array[i] > array[i+1]:
            return False
    return True

def Bubble(array):
    n = len(array)

    Printar(array)
    isOrdered = Verify(array)
    if isOrdered:
        return

    for j in range(0, n):
        for i in range(0, n-1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                Printar(array)
        isOrdered = Verify(array)
        if isOrdered:
            return

def Selection(array):
    n = len(array)

    Printar(array)
    isOrdered = Verify(array)
    if isOrdered:
        return

    for i in range(0, n):
        menor = i
        for j in range(i+1,n):
            if array[j] < array[menor]:
                menor = j
        swap(array,menor, i)
        Printar(array)
        isOrdered = Verify(array)
        if isOrdered:
            return

def Insertion(array):
    n = len(array)
    
    Printar(array)
    isOrdered = Verify(array)
    if isOrdered:
        return

    for i in range(1, n):
        j = i
        while array[j-1] > array[j] and j > 0:
            swap(array, j, j-1)
            j = j-1
        Printar(array)
        isOrdered = Verify(array)
        if isOrdered:
            return

def Printar(array):
    maior = max(array)
    n = len(array)

    print("."*(n+2))
    for i in range(0, maior):
        print(".",end="")
        for j in range(0, n):
            if array[j] >= maior-i:
                print("|",end="")
            else:
                print(" ",end="")
        print(".")
    print("."*(n+2))


sort = 'bubble'
data = input()
dataN = []

funcs={'insertion':Insertion, 'bubble':Bubble, 'selection':Selection}

for i in data.split():
    dataN.append(int(i))

funcs[sort](dataN)
