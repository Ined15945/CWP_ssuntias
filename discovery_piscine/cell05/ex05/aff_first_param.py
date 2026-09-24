import sys
params = sys.argv 
if len(params) > 1:
    print(params[1])
else:
    print("none")

# test case 
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex05\\aff_first_param.py "this" "is" "crazy" "there's" "everywhere!"
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex05\\aff_first_param.py "initiation"
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex05\\aff_first_param.py "Code Ninja" "Numerique" "42"
