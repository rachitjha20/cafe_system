#### CAFE SYSTEM ###########



print ("Welcome !!!!!!! Amigo !!!!!")
print()
print("Whate would you like to have??")
print()
print("!!! Here's our Delicious Menu !!! Enjoy!!!")

list1 = ["Pasta", "Coffee", "Tea"]
fd = [element.lower() for element in list1]

prc = [100, 80, 55]
menu = dict(zip(fd,prc))
for item, price in menu.items():
    print(f"\n{item}:{price} ₹\n")
    
total = 0

while True:
    
    choice = str(input("What would you like to have? : ")).lower()
    
    if choice in menu:
        print("\n!!Added!!\n")
        total += menu[choice]
        fur = str(input("Somthing more to add?? : ")).lower()
        if fur == "yes":
            for item, price in menu.items():
                print(f"\n{item}:{price} ₹\n")
        else:
            
            print(f"\nThank you!! Your total sum is {total}₹\n")
            break
    else:
        print(f"Sorry, we do not serve {choice} for now. Would you like to have something else?")

        
