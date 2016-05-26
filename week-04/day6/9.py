# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

# output = ''
#
# for i in string:
#     output += i + '*'
# print(output)

def plus_star(string):
    output = ''
    if len(string) <= 1:
        return string
    else:
        output += string[0] + '*'
        return output + plus_star(string[1:])

print(plus_star('xyxyxyxyxyxyyxy'))
