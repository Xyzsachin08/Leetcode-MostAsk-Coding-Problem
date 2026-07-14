n = int(input("Enter a number: "))
temp = n
rev = 0

while temp > 0:
    r = temp%10
    temp//= 10
    rev = rev*10+r
    
if rev == n:
    print("No is palindrome")
else:
    print("No is not palindrome")