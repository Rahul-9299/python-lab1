#Python function that accepts a list and returns a new list with only the even numbers from the original list.
naturnal_number=[1,3,2,4,5,6,7,8,9,0]
even=[]
for i in naturnal_number:
    if i%2==0:
        even.append(i)
print("list of even numbers:",even)
        
