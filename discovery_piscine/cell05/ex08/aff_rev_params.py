import sys
params = sys.argv 
i = len(params) -1
if len(params) < 2:
    print("none")
else:
    while i > 0:
        print(params[i])
        i -= 1

# test case 
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex08\\aff_rev_params.py "this" "is" "crazy" "there's" "everywhere!"
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex08\\aff_rev_params.py "Code Ninja" "Numerique" "42"