string = input("Enter a string: ")
count = 0
for ch in string:
    if ch.lower() in "a e i o u":
        count+=1
print("number is vowels= ",count)