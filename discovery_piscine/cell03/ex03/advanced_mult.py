i, j = 0,0
while i <= 10:
    print(f"Table de {i}: ", end = "")
    while j <= 10:
        print(i*j,end = " ")
        j += 1
    i += 1
    j = 0
    print()
    