MAX_LINES = 3

def deposite():
    while True:
        amount = input("Enter Amount :")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                # print(f"Amount = {amount} ")
                break
            else:
                print("Enter Amount Greater than 0")             
        else:
            print("ENTER A NUMBER")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter Number of Lines to bet on (1-" + str(MAX_LINES) +")?")
        if lines.isdigit():
            lines = int(lines)
            if  1 <= lines <= MAX_LINES:
                # print(f" {lines} Line ")
                break
            else:
                print("Enter Valid Number of Lines")             
        else:
            print("ENTER A NUMBER")

    return lines

def main():
    balance = deposite()
    lines = get_number_of_lines()
    print(f"Your balance {balance} & Lines {lines}")

main()
            
