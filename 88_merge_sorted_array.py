# def merge(nums1, m, nums2, n):
    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# while m > 0 and n > 0: # first m, n should be larger than 0
#     if nums1[m-1] >= nums2[n-1]: # if last variable of nums1 list is larger or same then nums2's last variable
#         nums1[m+n-1] = nums1[m-1] # nums1(final)'s last variable will be nums1's last component
#         m -= 1 #-1 m so move on to next variable
#     else:
#         nums1[m+n-1] = nums2[n-1] #nums2's variable will put instead
#         n -= 1
# if n > 0: #if m or n is 0, then..
#     nums1[:n] = nums2[:n] # nums2's n

if m > 0 and n > 0:
    v1 = [nums1[i] for i in range(m)]
    v2 = [nums2[i] for i in range(n)]
    v1.extend(v2)
    nums1 = sorted(v1)
else:
    nums1[:n] = nums2[:n]
#don't know why but for function below while fuction

print(nums1)
