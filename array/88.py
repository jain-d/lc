# Merge Sorted Array

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for number in nums2:
        i = 0
        while i < m:
            if nums1[i] < number:
                if nums1[i + 1] >= number:
                    shift_n_delete(nums1, i + 1, number, m)
                    m += 1
                    break
                i += 1
                continue
            else:
                shift_n_delete(nums1, i, number, m)
                m += 1
                break
        if i == m:
            shift_n_delete(nums1, i, number, m)
            m += 1


def shift_n_delete(array: list[int], index: int, element: int, end: int) -> None:
    for local_index in range(index, end + 1):
        array[local_index] ^= element
        element ^= array[local_index]
        array[local_index] ^= element


first_array = [0,0,3,0,0,0,0,0,0]
second_array = [-1,1,1,1,2,3]
print(first_array, second_array)

merge(first_array, 3, second_array, len(second_array))
print(first_array, second_array)
