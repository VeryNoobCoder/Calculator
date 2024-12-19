calc = float(input("Enter Number: "))
calc1 = float(input("Enter Number: "))

operator = input("Enter (+, -, *, /)")

if operator == "+":
    result = calc + calc1
    print(f"{result}")
elif operator == "-":
    result = calc - calc1
    print(f"{result}")
elif operator == "*":
    result = calc * calc1
    print(f"{result}")
elif operator ==  "/":
    if calc1 !=0:
        result = calc / calc1
        print(f"{result}")
    else:
        print("Not divisible by 0")

