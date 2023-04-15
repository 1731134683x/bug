import time
def bubble(array=[]):
    last_index = 0
    sort_border = len(array)-1
    while(1): 
    # 确保遍历整个列表
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_sorted = False
                last_index = j
        print(array)
        sort_border = last_index
        if is_sorted:
            break
start= time.time()
a = list([1,5,3,2,4,8,9,4,6,5,6,1,8,3,1,7,11,55,333])
bubble(a)
end = time.time()
print(a)
print('%s'%(end-start))


