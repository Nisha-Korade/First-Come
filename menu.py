#Online Order Booking Menu Card#
order=0
while order == 0 :
    menu={
        "Pizza":120,
        "Burger":90,
        "Pasta":80,
        "Coffee":60,
        "Chocolateshake":95,
    }

    print("Welcome to Star Cafe.....")

    print("        Menu")
    print("Pizza : Rs 120\nBurger : Rs 90\nPasta : Rs80\nCoffee : Rs 60\nChocolateshake : Rs 95")

    total_order=0
    odr1=input("Enter the name of item you want to order : ")
    if odr1 in menu:
        total_order += menu[odr1]
        print(f'Your {odr1} has been added to your order')
    else:
        print(f'Ordered item {odr1}is not available yet' )

    another=input("Do you want to anything else(yes/no):")
    if another == 'yes':
        odr2=input("Enter the name of second item which you want to order :")
        if odr2 in menu:
            total_order += menu[odr2]
            print(f"Your {odr2} has been added to your order.")
        else:
            print(f'Ordered item {odr2}is not available yet' )
        

    odr=input("Isn't Your Order is Complete(yes/no):")
    if odr == "no":
        odr3=input("Enter name of item you want to order:")
        if odr3 in menu:
            total_order += menu[odr3]
            print(f"Your item {odr3} has been added to your order.")

        else:
            print(f"Ordered item {odr3} is not available yet")
    print(f'The Total Amount of order to pay is {total_order}')
    print("Thank You for Visiting Our Star Cafe.") 
    order +=1

    