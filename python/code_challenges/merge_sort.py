def merge_sort(lst):
    n = len(lst)

    if n > 1:
        mid = n//2
        left = lst[0:mid]
        right = lst[mid:n]

        merge_sort(left)

        merge_sort(right)

        merge(left, right, lst)
    print(f"Sorted List: {lst}")
    return lst


def merge(left, right, lst):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1

        k = k + 1

    # add any remaining values once we've exhausted one sub list
    if i == len(left):
        for x in range(j, len(right)):
            print(f"append remaining entry right {right[x]}")
            lst[k] = right[x]
            k += 1

    else:
        for x in range(i, len(left)):
            print(f"append remaining entry left {left[x]}")
            lst[k] = left[x]
            k += 1


lst = [8, 4, 23, 42, 16, 15]
merge_sort(lst)
