import sys
# file.py is index 0 so need to -1
num_params = len(sys.argv) - 1

print(f"Number of parameters: {num_params}.")


# test case 
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex04\\parameters.py "this" "is" "crazy" "there's" "everywhere!"
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex04\\parameters.py "initiation"