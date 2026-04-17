def removeDuplicates(nums:list):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i] # k vai servir como um auxiliar
            k += 1
        else:
            continue
    return k

print(removeDuplicates([1,1,2]))    