# SHORTEST WORD
# 7KYU

"""
x Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

"""
# # 1
# def find_short(s):
#     words = s.split(' ')
#     words.sort(key=len)
#     return len(words[0])

# # 2
# def find_short(s):
#     lengths = []
#     for word in s.split(" "):
#         lengths.append(len(word))
#     return min(lengths)

# # 3
# def find_short(s):
#     return min(len(x) for x in s.split())

# 4
def find_short(s):
    s = s.split() # splits the string into a list of individual words
    l = min(s, key = len) # finds the shortest string in the list
    return len(l) # returns shortest word length
    


print(find_short("bitcoin take over the world maybe who knows perhaps"))