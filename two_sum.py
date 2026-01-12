# two_sum problem
# approach 1: using the brut force 

arr=[2,7,11,15]
target=9

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(f"{arr[i],arr[j]}")
            
            
            
            
# approach 2 : using the two pointer approach
arr=[2,7,11,15]
target=9
left=0
right=len(arr)-1
while left<right:
    current_sum=arr[left]+arr[right]
    if current_sum==target:
        print(f"{arr[left],arr[right]}")
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1
        
        
        