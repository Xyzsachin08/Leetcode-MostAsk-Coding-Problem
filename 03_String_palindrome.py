s = input("Enter a string name: ")
reverse = ""
for ch in s:
    reverse = ch + reverse
    
if s == reverse:
    print("palindrome")
else:
    print("not")
    