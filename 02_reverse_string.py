'''
# usingh slicing
s = input("Enter a string name: ")
reverse = s[::-1]
print("Reverse string is :",reverse)


#using for loop

s = input("Enter a string name :")
reverse = " "
for ch in s:
    reverse = ch+reverse
    
print("Reverse string",reverse)
'''

#using while loop
s = input("Enter a string: ")
i = len(s)-1
while i>=0:
    print(s[i],end=" ")
    i -=1 
    
