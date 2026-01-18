nums=[0,1,0,3,12]
non_zero=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[non_zero],nums[i]=nums[i],nums[non_zero]
        non_zero+=1
        print(nums)