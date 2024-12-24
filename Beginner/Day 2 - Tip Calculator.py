print("Welcome to the tip calculator")

bill=float(input("What was the total amount on the bill?"))
tip=int(input("How much percentage do you want to tip? 10, 12, or 15?"))
people=int(input("How many people are splitting the bill?"))

bill=bill+bill*(tip/100)
amount=round((bill/people),2)

print("Each person should pay",amount)
