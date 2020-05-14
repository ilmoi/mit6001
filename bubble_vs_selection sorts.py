def bubble_sort(L):
    #    counter = 0 #counts how many times had to "loop through"
    swap = False  # initialize
    while not swap:
        swap = True  # default assumption that this is the last loop
        for j in range(1, len(L)):  # for each item
            if L[j-1] > L[j]:  # if the one before is bigger
                swap = False  # oops! not the last! will have to loop again!
                L[j], L[j-1] = L[j-1], L[j]  # swap
                print(L)
#            counter+=1
    return L,  # counter


def selection_sort(L):
    #    counter = 0
    suffixStart = 0
    while suffixStart != len(L):
        # +1 here is important, otherwise you're doing double work when i == suffixStart
        for i in range(suffixStart+1, len(L)):
            if L[i] < L[suffixStart]:
                L[suffixStart], L[i] = L[i], L[suffixStart]
                print(L)
#            counter+=1
        suffixStart += 1
    return L,  # counter


x = [1, 5, 4, 2, 3, 10, 7, 6, 9, 8]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
z = [5, 4, 3, 2, 1]

# print(bubble_sort(z))
print(selection_sort(z))

# interesting. If the list is easy (like x), then bubble sort is quicker.
# If the list is hard (like y), then selection sort is quicker
