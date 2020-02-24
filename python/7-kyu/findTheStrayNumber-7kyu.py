# FIND THE STRAY NUMBER
# 7KYU

'''
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
'''
# 1
def stray(arr):
	arrIntoSet = set(arr)
	for strayNum in arrIntoSet:
		if arr.count(strayNum) == 1:
			return strayNum

# # 2
# def stray(arr):
#     for x in arr:
#         if arr.count(x) == 1:
#             return x


print(stray([1,1,1,1,1,1,2]))
print(stray([2,3,2,2,2]))
print(stray([3,2,2,2,2]))


'''
Python | set() method
Set, a term in mathematics for a sequence consisting of distinct language is also extended in its language by Python and can easily made using set().

set() method is used to convert any of the iterable to the distinct element and sorted sequence of iterable elements, commonly called Set.

Syntax : set(iterable)



Parameters : Any iterable sequence like list, tuple or dictionary.

Returns : An empty set if no element is passed. Sorted, non-repeating element iterable modified as passed as argument.
'''