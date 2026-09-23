
origin =  [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array: {origin}")

for i in range(len(origin)):
    origin[i] = origin[i] + 2
    
for i in origin[:]:
    if i <= 5 :
        origin.remove(i)

print(f"New array: {origin}")