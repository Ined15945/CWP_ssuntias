import sys
params = sys.argv 
if len(params) != 2:
    print("none")
else:
    print(params[1].lower())


# test case 
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex07\\downcase_it.py "LUCIOLE"
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex07\\downcase_it.py "This exercise is quite easy!"

