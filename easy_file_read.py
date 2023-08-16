def read_file():
    '''Opens file for reading.'''
    f = open("easy_mode.txt", "r")
    result = f.readlines()
    f.close()
    return result


def strip_and_split(item):
    '''Removes \n and \t. Also, separates elements in contents list;
 Strips and splits items in contents'''
    for i in range(len(item)):
        item[i] = item[i].strip("\n")
        item[i] = item[i].split("\t")

    return item

'''
# Prints usable functions
print()
print("Usable functions:")
print("read_file()")
print("strip_and_split()")
print('\n')
'''

# read_file
contents = read_file()

# strip_and_split
contents = strip_and_split(contents)
