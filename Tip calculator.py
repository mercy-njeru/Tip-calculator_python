print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? £\n"))
tip = float(input("What percentage tip would you like to give? \n"))
people = int(input("How many people to split the bill? \n"))

worked_tip = (tip/100)*bill
person_pay = round(((bill + worked_tip)/ people), 2)

print(f"Each person should pay: £ {person_pay}")