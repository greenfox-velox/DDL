def palindrome_maker(input):
    palindrome = input + input[::-1]
    return palindrome

print(palindrome_maker('kutya'))
