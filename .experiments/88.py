# Merge Sorted Array

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1_pointer = m - 1
    nums2_pointer = n - 1

    for index in range(len(nums1)-1, -1, -1):
        if nums1_pointer > -1 and nums2_pointer > -1:
            if nums1[nums1_pointer] >= nums2[nums2_pointer]:
                nums1[index] = nums1[nums1_pointer]
                nums1[nums1_pointer] = 0
                nums1_pointer -= 1
                print(nums1)
                _ = input("")
                continue
            nums1[index] = nums2[nums2_pointer]
            nums2_pointer -= 1
            print(nums1)
            _ = input("")
        elif nums1_pointer > -1:
            nums1[index] = nums1[nums1_pointer]
            nums1[nums1_pointer] = 0
            nums1_pointer -= 1
        elif nums2_pointer > -1:
            nums1[index] = nums2[nums2_pointer]
            nums2_pointer -= 1
        else:
            return



first_array = [0,0,3,0,0,0,0,0,0]
second_array = [-1,1,1,1,2,3]
print(first_array, second_array)

merge(first_array, 3, second_array, len(second_array))
print(first_array, second_array)
