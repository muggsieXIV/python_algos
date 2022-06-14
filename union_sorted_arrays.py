# Union Sorted Arrays
#
# Efficiently combine two already-sorted multiset arrays
# into a new sorted array containing the multiset union.
#
# Unions by default will take the set of dupes
# that has the highest occurrences from one array.
#
# Venn Diagram Visualization (top) https://i.ytimg.com/vi/sdflTUW6gHo/maxresdefault.jpg


def unionSortedArrays(arr, arr2):
    union = []
    occurences = 0
    new_arr = arr + arr2
    new_arr.sort()
    
    # Evaluate each element to obtain a count of duplicates
    for i in range(len(new_arr)):
        # [2, 4, 4, 4, 6, 6, 10, 10, 14, 14]
        eval = new_arr[i]

        if eval not in union:
            count = 0
            
            for j in range(0, len(new_arr)):
                if new_arr[j] == eval:
                    count += 1
                    print('eval: ' + str(eval) + ', count: ' + str(count) + ', occurences: ' + str(occurences))

            if count == occurences:
                union.append(eval)
            
            if count > occurences:
                occurences = count 
                union = []
                union.append(eval)


    print(arr)
    print(arr2)
    print(new_arr)
    print(union)
    return union 

unionSortedArrays([2, 4, 6, 5, 5, 5, 10, 14], [4, 4, 6, 10, 14, 14])
unionSortedArrays([2, 4, 6, 5, 10, 14], [4, 6, 10, 14])
