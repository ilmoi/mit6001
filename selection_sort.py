def selection_sort(L):
    suffixStore = 0 #some sort of index
    while suffixStore != len(L):
        for i in range(suffixStore, len(L)): #slice the list from that index till the end
            if L[i] < L[suffixStore]: #if current element  smaller than that at index
                L[suffixStore], L[i] = L[i], L[suffixStore] #swap the two, it's equivalent to (a,b) = (b,a). 
        suffixStore += 1
                