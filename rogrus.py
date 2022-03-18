def intro():
    print("welcome to DogRus")
    print("would you like to:")

intro()

print ("a for dropping off dog")
print("b for pick up dog")
print("c for print a list of all the dogs currently staying")
print("d for calculating the amount to charge for the stay")
print("e for exit")
your_text = input("your option")
dog_list = []

while your_text == "a" or your_text == "b" or your_text == "c" or your_text == "d":


    if your_text == "a":
                name_of_dog = input("name of dog")
                dog_list.append(name_of_dog)


    elif your_text == "b":
                name_of_dog = input("name of dog")
                if name_of_dog in dog_list:
                        dog_list.remove(name_of_dog)
                        print(f"{name_of_dog} has been removed")
                else:
                        print("no dogs found")
    elif your_text == "c":
                print(dog_list)
                your_text = 0
    elif your_text == "d":
                number_of_days = int(input("enter number of stay"))
                print (number_of_days*22.5)
    your_text =input("would you like to see the menu again?\na for dropping off dog\nb for picking up dog\nc for printing a list of all the dogs currently staying\nd for calculating the amount to charge for the stay\ne for exit\n")
print("goodbye")

