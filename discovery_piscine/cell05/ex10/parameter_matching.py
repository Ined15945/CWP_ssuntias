import sys
params = sys.argv 
count = 0
if len(params) != 2:
    print("none")
else:
    word = params[1]
    matcher = input("What was the parameter? ")
    if word == matcher:
        print("Good job!")
    else:
        print("Nope, sorry...")



# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex10\\parameter_matching.py "Hello"