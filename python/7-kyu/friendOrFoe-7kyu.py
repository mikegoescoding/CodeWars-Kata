# FRIEND OR FOE?
# 7KYU

'''
Problem Description: Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has 4 letters in it, you can be sure that it has to be a friend of yours!

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.

'''


def friend(x):
    my_friends = []
    for name in x:
        if len(name) == 4:
            # my friends are 4 letters, if not 4 letters - not my friend
            my_friends.append(name)

    return my_friends


print(friend(["Ryan", "Kieran", "Mark", ]))