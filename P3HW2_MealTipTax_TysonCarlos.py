   # Tip Calculator
    # 9/24/2020
    # CTI-110 P2HW1 - Meal Tip Tax Calculator
    # Carlos Tyson
    # Enter the cost of dinner, then enter tip as a decimal, then enter tax rate as a decimal. The calculated tip will multipy food_charge by tip_percentage divide by 100. The calculated tax will multipy food_charge by tax percentage divide by 100. Total cost is food_charge + calculated tip + calculated tax.

food_charge = float(input("Enter cost of food: "))
print("Price of meal is", food_charge)
tip_percentage = float(input("Enter Tip Percent of 15, 18, or 20: "))
if tip_percentage == 15:
    print("Tip is", tip_percentage)
elif tip_percentage == 18:
    print("Tip is", tip_percentage)
elif tip_percentage == 20:
    print("Tip is", tip_percentage)
else:
    print(error)
tax_percentage = float(input("Enter Tax Percent: "))
print("Tax is", tax_percentage)

calculated_tip = (food_charge * (tip_percentage / 100))
print("Expected tip amount is", (format(calculated_tip, ".2f")))
calculated_tax = (food_charge * (tax_percentage / 100))
print("Expected tax for meal is", (format(calculated_tax, ".2f")))
total_cost = (food_charge) + (calculated_tip) + (calculated_tax)

print("The total of the meal, including tax and tip is", (format(total_cost, ".2f")))
