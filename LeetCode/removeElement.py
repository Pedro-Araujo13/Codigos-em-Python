def removeElements(nums:list, val:int):
    while val in nums:
        nums.remove(val)
    return nums


print(removeElements([0,1,2,2,3,0,4,2], 2)) 