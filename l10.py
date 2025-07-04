# Input key-value pairs from the user and store them in a dictionary
my_dict = {}
n = int(input("How many key-value pairs do you want to enter? "))
for _ in range(n):
    k= input("Enter key: ")
    v = input("Enter value: ")
    my_dict[k] = v

search_k = input("Enter key to search: ")
if search_k in my_dict:
    print(f"Value for '{search_k}':", my_dict[search_k])
else:
    print(f"Key '{search_k}' not found.")