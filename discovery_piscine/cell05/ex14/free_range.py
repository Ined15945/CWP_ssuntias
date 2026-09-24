import sys
l = []
params = sys.argv 

if len(params) != 3 :
    print("none")
else:
    num1= int(params[1])
    num2 = int(params[2])

    while num1 <= num2:
        l.append(num1)
        num1 += 1
    print(l)

# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex14\\free_range.py 10 14