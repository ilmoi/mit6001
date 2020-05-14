def bubble_sort(L):
    counter = 0
    swap = False
    while not swap:
        swap = True
        for j in range (1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j], L[j-1] = L[j-1], L[j] #swap
            counter+=1
    return L, counter

def selection_sort(L):
    counter = 0
    suffixStart = 0
    while suffixStart != len(L):
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                L[suffixStart], L[i] = L[i], L[suffixStart]
            counter+=1
        suffixStart+=1
    return L, counter

x = [1,5,4,2,3,10,7,6,9,8]
y = [10,9,8,7,6,5,4,3,2,1]
print(bubble_sort(y))
print(selection_sort(y))