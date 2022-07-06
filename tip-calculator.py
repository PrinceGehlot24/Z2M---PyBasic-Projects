print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("How much tip would you like to give in % ? 10, 12 or 15 \n"))
people = int(input("How many people to split the bill?\n"))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_head = total_bill / people
cost = round(bill_per_head, 2)
print("Per Head :" + str(cost))
