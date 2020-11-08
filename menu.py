def menu():
    print("Play")
    print("Exit")
    choice = input("Enter your choice: ")
    if choice == "Play":
        import P5HW1_RandomNumber_TysonCarlos.py
        P5HW1_RandomNumber_TysonCarlos.main
    elif choice == "Exit":
        exit
    else:
        print("Invalid Choice. Enter Play or Exit")
menu()        

