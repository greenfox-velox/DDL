# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

# output = ''
# string = 'xyxyxyxyxyxyyxy'
#
# for i in string:
#     if i == 'x':
#         i = 'y'
#         output += i
#     else:
#         output += i
# print(output)
#

# def x_to_y(string):
#     if len(string) <= 1:
#         if string == 'x':
#             return 'y'
#         else:
#             return string
#     else:
#         if string[0] == 'x':
#             return 'y' + x_to_y(string[1:])
#         else:
#             return string[0] + x_to_y(string[1:])
#
# print(x_to_y('xyxyxyxyxyxyyxy'))

def x_to_y(string):
    if len(string) <= 0:
        return string
    else:
        if string[0] == 'x':
            return 'y' + x_to_y(string[1:])
        else:
            return string[0] + x_to_y(string[1:])
print(len('xyxyxyxyxyxyyxy'))
print(len(x_to_y('xyxyxyxyxyxyyxy')))
print(x_to_y('x'))
print(x_to_y(''))
