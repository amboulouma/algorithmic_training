mergedlist = sorted(nums1+nums2)
length = len(mergedlist)
if length % 2 == 0:
    return (mergedlist[length//2 - 1] + mergedlist[length//2])/2
else:
    return mergedlist[length//2]
