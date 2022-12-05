# def twosum(nums, target):
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#            sum = nums[i]+nums[j]
#            if target == sum:
#                 return [i,j]
# > so brutal O(n^2)

def twosum(nums, target):
    v = {}
    for i,value in enumerate(nums):
        remain = target - nums[i]
        print("nums[i] = ",nums[i])
        if remain in v:
            return [i, v[remain]]
        else:
            v[value] = i
            print("v[value]= ", v[value])
            print(v)

nums = [11,22,33,44,55,66,77,88,99,100]
target = 199

# nums = [3,3]
# target = 6

print(twosum(nums, target))
