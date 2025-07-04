# Count how many times each name appears in a list using a dictionary
names = ["rahul","sashank","nischal","ram","shyam","hari","sita","ram","sita","rahul"]
name_count = {}
for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1
print(name_count)