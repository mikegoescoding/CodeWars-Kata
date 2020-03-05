# Name Shuffler
# 8kyu

'''
Write a function that returns a string in which firstname is swapped with last name.

Example: name_shuffler('john McClane'); => "McClane john"
'''


def name_shuffler(name):

    # split elements of string separated by space 
    shuffler = name.split(' ')

    # reverse list of elements 
    # suppose we have list of elements list = [1,2,3,4],  
    # list[0]=1, list[1]=2 and index -1 represents, 
    # the last element list[-1]=4 ( equivalent to list[3]=4 ) 
    # So, shuffler elements[-1::-1] here we have three arguments 
    # first is -1 that means start from last element 
    # second argument is empty that means move to end of list 
    # third argument is difference of steps 
    shuffler = shuffler[-1::-1]

    # now join elements with space 
    shuffledName = ' '.join(shuffler)

    # now return the shuffledName
    return shuffledName

    
print(name_shuffler('john McClane'))