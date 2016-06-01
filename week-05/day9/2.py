# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def count_lines(file_name):
    count = 0
    try:
        file = open(file_name)
        f = file.readlines()
        file.close()
        for line in f:
            count += 1
        return count
    except FileNotFoundError:
        return 0

print(count_lines('text.txt'))
print(count_lines('hello.txt'))
