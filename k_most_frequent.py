
# Given an unsorted non-empty array of integers and int k, return the k most frequent elements (in any order)
# You can assume there is always a valid solution
# These example inputs are sorted for readability, but the input is NOT guaranteed to be sorted and the output does NOT need to be in any specific order
# Hard Bonus: make it O(n) time
# [1,2,3,1,5,2], 2]
# should return
# [1,2]




def kMostFrequent(array, k):
    arr = sorted(array)
    new_arr = []

    for i in range(0, len(arr) - 1):

        # If element is not already accounted for, search for it k times
        if arr[i] not in new_arr:
            k_times = False
            for element in range(1, k):
                if arr[i] != arr[i + element]:
                    k_times = False 
                else:
                    k_times = True
            if k_times == True:
                new_arr.append(arr[i])
    return new_arr 

print(kMostFrequent([1,2,3,7,7,7,7,1,5,5,2,5], 3))
