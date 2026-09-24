import sys
params = sys.argv 
count = 0
if len(params) < 2:
    print("none")
else:
    for i in params:
        print(f"{i}: {len(i)}")
    
    



# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex11\\count_it.py "Hello"
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex11\\count_it.py "Game" "of" "Thrones"