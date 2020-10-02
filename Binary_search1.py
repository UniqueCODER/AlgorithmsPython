

def binary_search(seq,elements):
    begin_index = 0
    end_index = len(seq)-1

    while begin_index <=end_index:
        midpoint = begin_index +(end_index-begin_index) // 2
        midpoint_value=seq[midpoint]

        if midpoint_value == elements:
            return midpoint

        elif elements < midpoint_value:
            end_index = midpoint -1


        else:
            begin_index = midpoint +1
    return  None

x = [2, 4, 4, 8, 1, 2, 6, 5, 9]
a = 8

print(binary_search(x,a))