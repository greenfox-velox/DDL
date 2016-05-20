# Create a function that searches for all the palindromes in a string that are at least than 3 characters, and returns a list with the found palindromes. Example:
#
# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['dad', 'dood', 'eve']

def palindromes(string):
    palindrome = []
    if string == string[::-1]:
        palindrome = string[::-1]
        return 'It is one great palindrome'
    else:
        for r in range(len(string)-2):
            for p in range(3,len(string)):
                if string[r:r+p] == string[r:r+p][::-1]:
                    palindrome.append(string[r:r+p])
        return palindrome

print(palindromes('dog goat dad duck doodle never'))
# print(palindromes('eulb god dog blue'))
