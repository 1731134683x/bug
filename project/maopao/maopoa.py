def sort(array=[]):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[i]
                array[j] = array[j+1]
                array[j+1] = temp 
array1 = list([5,8,6,3,9,2,1,7])
sort(array1)
print(array1)

