# Square Every Digit
# 7kyu
'''
Problem Description: 
Welcome. In this kata, you are asked to square every digit of a number.
For example, if we run 9119 through the function, 811181 will come out, because 9² is 81 and 1² is 1.
Note: The function accepts an integer and returns an integer
'''

# SOLUTION 1
# def square_digits(num):
#     ans = ''
#     for i in str(num):
#         ans += str(int(i)**2)
#     return int(ans)

# SOLUTION 2
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits(9119))