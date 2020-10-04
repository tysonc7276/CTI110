   # Tip Calculator
    # 9/24/2020
    # CTI-110 P2HW1 - Meal Tip Tax Calculator
    # Carlos Tyson
    # Enter the cost of dinner, then enter tip as a decimal, then enter tax rate as a decimal. The calculated tip will multipy food_charge by tip_percentage. The calculated tax will multipy food_charge by tax percentage. Total cost is food_charge + calculated tip + calculated tax.

food_charge = float(input("Enter cost of food: "))
tip_percentage = float(input("Enter Tip Percent: "))
tax_percentage = float(input("Enter Tax Percent: "))

calculated_tip = (food_charge * tip_percentage)
print(calculated_tip)
calculated_tax = (food_charge * tax_percentage)
print(calculated_tax)
total_cost = (food_charge) + (calculated_tip) + (calculated_tax)

print("The total of the meal, including tax and tip is", total_cost)
