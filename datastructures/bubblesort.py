def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

nums=[6,3,7,9,5,4]
sort(nums)
print(nums)