word = input("")
change = ""
for i in word:
    if "a" <= i <= "z":
        change += chr(ord(i) - 32)
    elif "A" <= i <= "Z":
        change += chr(ord(i) + 32)

print(change)