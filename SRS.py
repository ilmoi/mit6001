def merge(left, right):
    ans = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j+=1
    while i < len(left):
        ans.append(left[i])
        i+=1
    while j < len(right):
        ans.append(right[j])
        j+=1
    return ans

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left,right)
    
x = [9,8,7,6,5,4,3,2,1]    
y = merge_sort(x)
print(y)