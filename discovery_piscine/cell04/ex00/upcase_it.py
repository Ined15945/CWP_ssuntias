word = input("Give me a word: ")
upper = ""
for i in word:
    if "a" <= i <= "z":
        upper += chr(ord(i) - 32)
    else:
        upper += i

print(upper)