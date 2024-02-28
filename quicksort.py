def quicksort(L):
    if len(L) <= 1:
        return L # si la lista tiene un elemento o menos lo retornara
    else:
        pivot = L[0] # el pivote sera el primer número de la lista
        less = [x for x in L[1:] if x <= pivot] # divide los números menores que el pivote
        greater = [x for x in L[1:] if x > pivot] # divide los números mayores que el pivote
        return quicksort(less) + [pivot] + quicksort(greater) # retorna la lista ya ordenada

# Ejemplo de lista:
print(quicksort([3,6,8,10,1,2,1]))