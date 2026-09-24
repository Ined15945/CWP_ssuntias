import sys
l = []
params = sys.argv 

for i in range(1, len(params)):
    if params[i].endswith("ism"):
            pass
    else:
        l.append(params[i] + "ism")

if len(l) == 0:
    print("none")
else:
    for i in l:
        print(i)

# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex13\\append_it.py "parallel" "egoism" "human"