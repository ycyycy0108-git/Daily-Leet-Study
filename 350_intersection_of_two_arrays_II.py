
#1 Brutal
# def intersect(nums1, nums2):
#     out = []
#     v1 = nums1
#     v2 = nums2

#     for i in v1:
#         if i in v2:
#             out.append(i)
#             v2.remove(i)
#     return out

nums1 = [1,2,2,1]
nums2 = [2,2]

def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()

    i1 = i2 = 0
    out = []
    while i1 < len(nums1) and i2 < len(nums2):
        if nums1[i1] == nums2[i2]:
            out.append(nums1[i1])
            i1 += 1
            i2 += 1
        elif nums1[i1] < nums2[i2]:
            i1 += 1
        else:
            i2 += 1
    return out

answer = intersect(nums1, nums2)

print(answer)
