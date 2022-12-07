#very simple python way
def containdup(nums):
    # if len(nums) != set(nums):
    #     return True
    # else:
    #     return False
    return len(nums) != len(set(nums))


nums1 = [1,2,3,4,5,6,1]
nums2 = [1]

print(containdup(nums1))
print(containdup(nums2))

#brutal way
def containdup2(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(containdup2(nums1))
print(containdup2(nums2))

#brutal way2
def containdup3(nums):
    a = sorted(nums)
    for i in range(1,len(nums)):
        if(a[i] == a[i-1]):
            return True
    return False

print(containdup3(nums1))
print(containdup3(nums2))