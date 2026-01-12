
def removeElement( nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[slow]=nums[i]
                slow+=1
        return slow  
nums=[2,2,3,4,5,5]
val=2
print(removeElement(nums,val))     
    