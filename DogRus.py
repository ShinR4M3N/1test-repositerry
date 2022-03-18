def intro():
    print("welcome to DogRus")
    print("would you like to:")
    print ("1 for dropping off dog")
    print("2 for pick up dog")
    print("3 for print a list of all the dogs currently staying")
    print("4 for calculating the amount to charge for the stay")
    print("5 for exit")
intro()
dog_list = []
def pick_up():
    name_of_dog = input("name of dog")
    dog_list.append(name_of_dog)
    print(f"your {name_of_dog} has been added to the list")


def drop_off():
    name_of_dog = input("name of dog")
    if name_of_dog in dog_list:
                        dog_list.remove(name_of_dog)
                        print(f"{name_of_dog} has been removed")
    else:
                        print("no dogs found")

def print_dog():
    print(dog_list)

def calculating():
    number_of_days = int(input("enter number of stay"))
    print (number_of_days*22.5)

your_text = input("your option")
while your_text != "5":
    if your_text == "1":
        pick_up()
    elif your_text == "2":
        pick_up()

















