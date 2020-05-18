def insertion_sort():
    a = [4, 5, 3, 6, 7, 2, 5]
    n = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            if a[j] > key:
                n += 1
                a[j + 1], a[j] = a[j], key
            j -= 1

    print(a, n)


insertion_sort()
