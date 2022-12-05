def maxsubarray(nums):
    cur = maxi = nums[0]
    for i in nums[1:]:
        cur = max(i, cur+i)
        maxi = max(maxi, cur)
    return maxi

#max() > find maximum in the list
#using that 1]find if next one number's sum is bigger than current sum > if not, current sum will be same
#2]if next sum is bigger than current max, replace it.
#what I understand for this algorythm is that just repeat 0:len, 1:len, 2:len and find what is max for these whole calculation
#the good thing in this calc is that this is very simple and less memory use (save only 2 > maximum sum and current sum)
    
nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maxsubarray(nums))