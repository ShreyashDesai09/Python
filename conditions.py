num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))

choice = input("Enter The Options: + - * /:")

if choice == "+":
    ans = num1 + num2
    print("Addition:",ans)
elif choice == "-":
    ans = num1 - num2
    print("Sub:",ans)
elif choice == "*":
    ans = num1 * num2
    print("Multiplication:",ans)
elif choice == "/":
    ans = num1 / num2
    print("Division:",ans)
else:
    print("Wrong Choice")