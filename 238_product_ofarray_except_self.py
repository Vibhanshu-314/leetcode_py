def productExceptSelf(nums):
    """
    Given an integer array nums, return an array answer such that 
    answer[i] is equal to the product of all the elements of nums except nums[i].
    """
    n = len(nums)
    answer = [1] * n
    
    # First pass: calculate product of all elements to the left
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Second pass: calculate product of all elements to the right
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer


# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]