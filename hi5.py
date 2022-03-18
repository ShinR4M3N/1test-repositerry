number_amount = int(input("how many numbers to be averaged"))
number = 1
total_number = 0
while number <=number_amount:
    enter_number = int(input(f"enter number {number}"))
    number += 1
    total_number += enter_number
print (total_number)

print (total_number/number_amount)
