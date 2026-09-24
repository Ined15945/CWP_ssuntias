
import sys
params = sys.argv 
count = 0
if len(params) != 3:
    print("none")
else:
    first = params[1]
    second = params[2].split(" ")
    for i in second:
        if i == first:
            count += 1
    print(count)



# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex09\\scan_it.py "the" "the quick brown fox jumps over the lazy dog"