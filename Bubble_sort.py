def bubble_sort(a):
    if len(a)<1:
        return a
    else:
        for i in range(len(a)):
            for j in range(0, len(a) - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

    return a

x = [2, 4, 4, 8, 1, 2, 6, 5, 9]
print(bubble_sort(x))
