
def bubble_sort(a):

    for i in range(0, len(a)):
        for j in range( i +1, len(a)-1):
            if a[j ] > a[ j +1]:
                a[j] ,a[ j +1] = a[ j +1] ,a[j]

    return a

x = [2 ,4 ,4 ,8 ,1 ,2 ,6 ,5 ,9]
print(bubble_sort(x))
