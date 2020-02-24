# GHOSTBUSTERS
# 7KYU

'''
Oh no! Ghosts have reportedly swarmed the city. It's your job to get rid of them and save the day!

In this kata, strings represent buildings while whitespaces within those strings represent ghosts.

So what are you waiting for? Return the building(string) without any ghosts(whitespaces)!

Example:

ghostBusters("Sky scra per");
Should return: "Skyscraper"

If the building contains no ghosts, return the string:
"You just wanted my autograph didn't you?"

'''


def ghostBusters(building):
    # METHOD 1
    # if building.find(" ") == -1:
    #     return "You just wanted my autograph didn't you?"
    # else:
    #     return building.replace(" ", "")

    # METHOD 2
    if " " not in building:
        return "You just wanted my autograph didn't you?"
    else:
        return building.replace(" ", "")




print(ghostBusters("Sky scra per"))
print(ghostBusters("NoSpacesHere"))