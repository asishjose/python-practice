def sort(list):
    for i in range(len(list)-1):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        nums[i],nums[minpos]=nums[minpos],nums[i]

nums=[5,3,8,6,7,2]
sort(nums)
print(nums)