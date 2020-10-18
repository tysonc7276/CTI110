   # Tip Calculator
    # 9/24/2020
    # CTI-110 P2HW1 - Meal Tip Tax Calculator
    # Carlos Tyson
    # This program calculates the price of a meal with tip and tax.
    # This program will not move forward if you enter the wrong tip percentage.
    # This program will ask to enter another tip amount if desired

def main():
    food_charge = float(input("Enter cost of food: "))
    print("Price of meal is", food_charge)
    while True:
        try:
            tip_percentage = float(input("Enter Tip Percent of 16, 18, or 20: "))
            if tip_percentage == 16 or tip_percentage == 18 or tip_percentage == 20:
                print("Tip is", tip_percentage)
                break;
            else:
                print("Incorrect tip entered, please try again")
        except:
            continue
    

    tax_percentage = float(input("Enter Tax Percent: "))
    print("Tax is", tax_percentage)

    calculated_tip = (food_charge * (tip_percentage / 100))
    print("Expected tip amount is", (format(calculated_tip, ".2f")))
    calculated_tax = (food_charge * (tax_percentage / 100))
    print("Expected tax for meal is", (format(calculated_tax, ".2f")))
    total_cost = (food_charge) + (calculated_tip) + (calculated_tax)

    print("The total of the meal, including tax and tip is", (format(total_cost, ".2f")))

    while True:
        answer = input("Do you want to calculate a different tip? (y/n): ")
        if answer == 'y':
            main()
        else:
            print("Goodbye")
            break
main()
