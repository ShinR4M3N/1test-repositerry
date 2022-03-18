buy_ticket = input("do you want to buy ticket (Y/N)")
money = 0
adult_seat = 0
student_seat = 0
child_seat = 0
gift_seat = 0

while buy_ticket != "N":
    print("What type of tickets do you want? ")
    print("a for adult")
    print("s for student")
    print("c for child")
    ticket_wanted = str( input("g for gift voucher\n") )

    confirm = input(f"Confirm {ticket_wanted} (Y/N)")



    if confirm == "Y":

        if ticket_wanted == "a":
            money += 12.5
            adult_seat += 1
        elif ticket_wanted == "s":
            money += 9
            student_seat += 1
        elif ticket_wanted == "c":
            money += 7
            child_seat += 1
        elif ticket_wanted == "g":
            gift_seat += 1
        else:
            print("error1")
    buy_ticket = input("do you want to buy another ticket (Y/N)")
total_money = input("do you want to print total money? (Y/N) ")
if total_money == "Y":
    print("money earned today", money)
total_ticket = input("do you want to print total ticket? (Y/N) ")
if total_ticket == "Y":
    print(child_seat+gift_seat+student_seat+adult_seat)
