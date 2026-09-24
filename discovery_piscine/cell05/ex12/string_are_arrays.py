import sys
params = sys.argv 
count = 0
if len(params) != 2 :
    print("none")
else:
    for i in params:
        for j in i:
            if j == "z":
                print(j, end = "")


# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex12\\string_are_arrays.py "The character z is found in this string"
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex12\\string_are_arrays.py "Zaz visits the zoo with Zazie"
# python3 C:\\Users\\user\\discovery_piscine\\cell05\\ex12\\string_are_arrays.py "The character Z is not found in this string"