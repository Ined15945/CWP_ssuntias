num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
final_num = num1 * num2
print(f"{num1} x {num2} = {final_num}")

if final_num > 0:
    print("This number is positive.")
elif final_num < 0:
    print("This number is negative.")
else:
    print("This number is positive and negative.")