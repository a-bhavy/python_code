def twosum(nums,target):
    for index,i in enumerate(nums):
        # print(index,i)
        for indexj, j in enumerate(nums[index+1 :]):
            #print(indexj+1 + index,j)
            if i+j == target:
                print([index,indexj +index +1])


nums = [3,2,4]
target = 6
twosum(nums,target)



