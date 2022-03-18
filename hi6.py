number=1
password = "ddong"
pwc = input("enter password ")
while password != pwc and number < 3:
    print("try again")
    pwc = input("enter password ")
    number += 1
if pwc == password:
    print("cheonjae")
else:
    print("access den")
