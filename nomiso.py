# “abcde”, “edcba” => True
# “aaaa”, “aaa” => False
# “abbb”, “aaab” => False

# Implementing to support test cases. 
# def getDict(str):
#     dic = dict()
#     for char in str:
#         if char in dic:
#             return False
#         if char not in dic:
#             dic[char] = char
#             return dic
#     return dic

def enaigram(str, str2):
    # sort the string 
    sorted_str = sorted(str)
    sorted_str2 = sorted(str2)

    # If strings match, then true, else false
    if sorted_str == sorted_str2:
        return True
    else:
        return False

print(enaigram('abcde', 'edcba'))
print(enaigram('aaaa', 'aaa'))
print(enaigram('abbb', 'aaab'))
