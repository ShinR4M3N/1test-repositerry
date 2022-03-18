print("hi there")
would_you_like = str(input("would you to pick 'Fun is the sun'(F) or 'Active Kidz' (A) or 'Exit this program'(X) "))




children_list_1 = []
children_list_2 = []
average_age_1 = 0
total_number_1 = 0
average_age_2 = 0
total_number_2 = 0

while would_you_like == "F" or would_you_like == "A":

        your_name =input("what is your name")
        your_age = int(input("what is your age"))
        if your_age > 15:
            print("sorry you're too old")
        elif your_age < 5:
            print("sorry you're too young")
        if would_you_like == "F":
            children_list_1.append(your_name)
            children_list_1.append(your_age)
            total_number_1 += 1
            average_age_1 += your_age
        elif would_you_like == "A":
            children_list_2.append(your_name)
            children_list_2.append(your_age)
            total_number_2 += 1
            average_age_2 += your_age
        else:
            print("wrong number")



else:
    print("goodbye")


print(f"list 1: {children_list_1}")
print(f"list 2: {children_list_2}")

if total_number_1 != 0:
    print(f"list 1 total kids: {total_number_1}")
    print(f"list 1 average age: {average_age_1/total_number_1}")
else:
    print("no kid/Children in Fun in the sun")
if total_number_2 != 0:
    print(f"list 2 total kids: {total_number_2}")
    print(f"list 2 average age: {average_age_2/total_number_2}")
else:
    print("no kid/Children in Active kidz")

