def cock(array=[]):
    for i in range(len(array)//2):
        sorted = True
        for j in range(i,len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                sorted = False
            if sorted:
                break
        sorted = True
        for j in range(len(array)-i-1,i,-1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j-1] = array[j]
                array[j] = temp
                sorted = False
            if sorted:
                break


array1 = list([3,4,14,1,5,6,7,8,1,-1,0,9,11])
cock(array1)
print(array1) 

