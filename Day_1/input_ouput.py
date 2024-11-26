#String Formatting
city = input("Enter City Name: ")

name = input("Enter Name: ")

print("I am from",city)

print(f"I am from {city}")

about = f"Hello Dosto, My Name Is {name} And Surname {city}"

other_name = input("Enter Other Name: ")

print(about)

print(about.replace("Dosto",other_name))