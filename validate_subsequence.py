## Validate Subsequence 
# Given two non-empty arrays of integers, write a function that 
# determines whether the second array is a subsequence of the 
# first one. 

# A subsequence of an array is a set of numbers that arent necessarily adjacent
#  in the array but that are in the same order as they appear in the array. For 
# instance, the numbers [1 3, 4] form a subsequence of the array [1, 2, 3, 4], 
# and so do the numbers [2, 4]. Note that a single number in an array and the 
# array itself are both valid subsequences of the array. 

one = [5, 1, 22, 25, 6, -1, 8, 10]
two = [1, 6, -1, 10]


def validate_subsequence(array, sequence):

    # If sequence is an integer that is itself a subsequence, return True
    if sequence in array:
        return True

    # If missing input data, handle error
    if not array or not sequence:
        error = "Failed, missing inputs"
        return error

    # if sequence has more elements than arrray then it cannot be a subsequence, handle error
    if len(array) < len(sequence):
        return False

    # if sequence is equal to an unordered array, return True 
    sorted_sequence = sorted(sequence)
    sorted_array = sorted(array)
    if sorted_sequence == sorted_array:
        return True

    # Evaluate sequence data to the array
    for i in range(0, len(sequence)):
        
        # If sequence is not in array
        if sequence[i] not in array:
            return False

        # If sequence has more duplicate values than array, it cannot be a subsequence, return False
        if sequence.count(sequence[i]) > array.count(sequence[i]):
            return False

        # Else Tests Pass
        else:
            pass

    return True


test = validate_subsequence(one, two)
print(test)
