# “abcde”, “edcba” => True
# “aaaa”, “aaa” => False
# “abbb”, “aaab” => False


# # Fails some test cases 
# def enneagram(str, str2):
#     # sort the string 
#     sorted_str = sorted(str)
#     sorted_str2 = sorted(str2)

#     # If strings match, then true, else false
#     if sorted_str == sorted_str2:
#         return True
#     else:
#         return False


def anagram(str, str2):
    dic1 = dict()
    dic2 = dict()
    # Create dictionary 

    for char in str:
        if char not in dic1:
            dic1[char] = 0 
        else:
            dic1[char] += 1

    for char in str2:
        if char not in dic2:
            dic2[char] = 0 
        else:
            dic2[char] += 1

    if dic1 == dic2: 
        return True 
    else: return False 


print(anagram('abcde', 'edcba'))
print(anagram('aaaa', 'aaa'))
print(anagram('abbb', 'aaab'))
