def is_it_a_palindrome(input):
    if input == input[::-1]:
        palindrome = input[::-1]
        print(input + ' and ' + palindrome + ' are palindromes' )
    else:
        print(input + 'is not a palindrome')

is_it_a_palindrome('kutya')
