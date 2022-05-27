
# /*
#     Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#     You may assume that each input would have exactly one solution, and you may not use the same element twice.
#     Bonus: Make it O(n) time
# */


def two_sum(arr, target):
    new_arr = []
    for i in range(0, len(arr)):
        for x in range(0, len(arr)):
            if arr[i] + arr[x] == target:
                new_arr.append([arr[i], arr[x]])

    return new_arr


print(two_sum([2,4,5,7,10], 12))
