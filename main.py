print("Welcome to the tip calculator")
total_bill = input("What was the total bill? ")
tip_amount = input("How much tip would you like to give in percent? ")
people_amount = input("How many people to split the bill? ")

total_bill = int(total_bill)
tip_amount = int(tip_amount) / 100
people_amount = int(people_amount)

total_with_tip = total_bill + (total_bill * tip_amount)
final_bill_per_person = round(total_with_tip / people_amount, 2)

print(f"The total bill is: {total_with_tip}€")
print(f"Each person should pay: {final_bill_per_person}€")