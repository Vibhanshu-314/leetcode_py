def duplicate_removal(nums):
    slow=0
    n=len(nums)
    for fast in range(1,n):
        if nums[fast]!=nums[slow]:
            slow+=1
            
            nums[fast]=nums[slow]
    return slow+1 

nums=[1,1,2,2,3]
print(duplicate_removal(nums))