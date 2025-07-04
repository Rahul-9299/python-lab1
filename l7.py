# Merge two dictionaries and sum the values of common keys
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged = dict1.copy()
for k, v in dict2.items():
    if k in merged:
        merged[k] += v
    else:
        merged[k] = v

print("Merged dictionary:", merged)