# CTI-110
    # P4HW1 - Expenses
    # Carlos Tyson
    # 10/17/2020

def main():
    
    total = 0
    val = 0

    user_input = int(input('Enter Starting amount in account ' '$'))

    another = "Y"

    #the loop will repeat while the user types Y when asked if they want to enter another number
    while another == "Y":
        #asks the user to enter a expense
        val = int(input("Enter expense to add to the total: $ "))
        #asks the user if they want to enter another number
        another = input("Do you want to enter another expense? Y/N ")
        #adds the number entered to the total
        total = total + 1
        val = val + (val)
        
    final = user_input - (val)

    #after the loop ends it outputs the total
    print("Amount in account before expenses subtracted: ", user_input)
    print("Number of expenses entered: ", total)
    print("Amount in account After expenses subtracted is $", final)

#program start
main()
