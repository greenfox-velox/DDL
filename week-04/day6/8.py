# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

# output = ''
# string = 'xyxyxyxyxyxyyxy'
#
# for i in string:
#     if i == 'x':
#         pass
#     else:
#         output += i
# print(output)

def del_x(string):
    if len(string) <= 0:
        return string
    else:
        if string[0] == 'x':
            return '' + del_x(string[1:])
        else:
            return string[0] + del_x(string[1:])

print(del_x('x1x2x3x4x5x6x7x8x9'))
