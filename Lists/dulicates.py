def removeDuplicates(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
    return L1


r = removeDuplicates([1, 2, 3, 4], [12, 2, 3, 4])
print(r)
