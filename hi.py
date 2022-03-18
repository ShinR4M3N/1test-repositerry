price = int(input("price "))
print ((price),"$")
item = int(input("type 1 for food, and 2 for electrical"))
print (item)
if price >=10 and item == 1:
    print (price - price*0.4)
if price >=10 and item == 2:
    print (price - price*0.3)
elif price >=10 and item >2:
    print (price - price*0.2)
else:
    print (price)
