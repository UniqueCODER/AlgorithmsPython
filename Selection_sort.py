

def selection_sort(x):
    x_size = range(0, len(x)-1)

    for i in x_size:
        min_val = i
        for j in range(i+1, len(x)):
            if x[j] < x[min_val]:
                min_val = j
        if min_val != i:
            x[min_val], x[i] = x[i], x[min_val]
    return x




print(selection_sort([1, 4, 5, 2, 4, 8]))
