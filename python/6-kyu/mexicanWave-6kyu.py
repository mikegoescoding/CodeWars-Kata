# MEXICAN WAVE . 
# 6kyu

'''
Task
 	In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
Rules
 	1.  The input string will always be lower case but maybe empty.
2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
Example
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
'''


# # # 1 IN CLASS
# def wave(str):
#     wave_container = []

#     for char_index in range(len(str)):
#         if str[char_index] == " ":
#             continue
#         else:
#             wave_item = f"{str[0:char_index]}{str[char_index].upper()}{str[char_index +1:]}"
#             wave_container.append(wave_item)

#     return wave_container


# 2 IN CLASS . 
def wave(string):
  wave_container = []

  for char_index, char in enumerate(string):
    if char == " ":
      continue
    else:
      wave_item = f"{string[0:char_index]}{char.upper()}{string[char_index + 1:]}"
      wave_container.append(wave_item)

  return wave_container

print(wave("hello there"))



# # 3
# def wave(str):
#     return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]



print(wave("hello"))