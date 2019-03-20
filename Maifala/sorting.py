def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    sorted = items.copy()
    for n in range (len(sorted)):
        for j in range(len(sorted)-1-n):
            if sorted[j] > sorted[j+1]:
                sorted[j], sorted[j+1] = sorted[j+1], sorted[j]

    return sorted


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''


    if len(items) <2: return items
    result,mid = [], int(len(items)/2)


    n= merge_sort(items[:mid])
    m=merge_sort(items[mid:])

    while (len(n)>0) and (len(m)>0):
        if n[0] > m[0]:result.append(m.pop(0))
        else:result.append(n.pop(0))

    result.extend(m+n)

    return result


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    len_n = len(items)

    if len_n <= 1:
        return items

    pivot = items[len_n-1]
    small = []
    large = []
    dup = []

    for n in items:
        if n < pivot:
            small.append(n)
        elif n > pivot:
            large.append(n)
        elif n == pivot:
            dup.append(n)

    small = quick_sort(small)
    large = quick_sort(large)

    return  small + dup + large
