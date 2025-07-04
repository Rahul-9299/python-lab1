# program to count the number of each character in a given string using a dictionary
s = "my name is rahul bam"
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
