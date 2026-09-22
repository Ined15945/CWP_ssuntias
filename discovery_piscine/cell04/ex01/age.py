age = int(input("Please tell me your age: "))
many_years = [10,20,30]
print(f"You are currently {age} years old.")

for i in range(3):
    print(f"In {many_years[i]} years, you'll be {many_years[i] + age} years old")