# read in a file and fill dictionary with letter count
import string


file = open('sometext.txt', 'r')

d = dict.fromkeys(string.ascii_lowercase, 0)

while 1:
    char = file.read(1)
    char = char.lower()
    if not char:
        break
    if char.isalpha():
        if char in d.keys():
            d[char] += 1

file.close()

count_sorted = {k: v for k, v in sorted(d.items(), key=lambda item: item[1],reverse=True)}

print(count_sorted)
