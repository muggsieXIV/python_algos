
# Given an unsorted non-empty array of integers and int k, return the k most frequent elements (in any order)
# You can assume there is always a valid solution
# These example inputs are sorted for readability, but the input is NOT guaranteed to be sorted and the output 
# does NOT need to be in any specific order
# Hard Bonus: make it O(n) time
# [1,2,3,1,5,2], 2]
# should return
# [1,2]


def kMostFrequent(array, k):

    if len(array) <= k:
        return "You must have at least the same number of elements in the array as your k(" + str(k) + ") request amount"

    arr = sorted(array)
    new_arr = []
    
    dic = dict()

    for i in range(0, len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        if arr[i] in dic:
            dic[arr[i]] += 1

    new_arr = sorted(dic, key=dic.get, reverse=True)
    if len(new_arr) > k:
        new_arr = new_arr[0:k]

    return new_arr

print(kMostFrequent([1,2,4,4,4,4,3,7,7,7,7,1,5,5,2,2,2,2,2,5,5,5,5,5], 1))
print(kMostFrequent([1,2,3,1,5,2], 2))
print(kMostFrequent([1,2,3,-11,5,12,-1,3,2], 2))
print(kMostFrequent([1], 2))
