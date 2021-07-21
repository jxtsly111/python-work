import time
print("welcome to sly Grocery shop")
# items = ["Gari ","Shito ","Milo ","Milk "]
order=(input("please select from the items given, the product you want to order(Gari,Shito,Milo,Drink):"))
time.sleep(2)
print(order.lower())
if order == "Gari".lower():
    foriegnLocal=input("Do you prefer the foriegn or local:" )
    time.sleep(3)
    print(foriegnLocal)
    if foriegnLocal == "foriegn":
        print("your Gari cost GHC25")
    elif foriegnLocal =="local":
        print("your Gari cost GHC20")
    else:
        print("please choose from the option given")
elif order == "Shito":
    foriegnLocal=input("Do you prefer the foriegn or local:" )
    time.sleep(3)
    print(foriegnLocal)
    if foriegnLocal == "foriegn":
        print("your Shito cost GHC25")
    elif foriegnLocal =="local":
        print("your shito cost GHC20")
    else:
        print("please choose from the option given")
elif order == "Milo":
    miloo=input("Do you prefer the Nestle Milo or Richoco:" )
    time.sleep(3)
    print(miloo)
    if miloo == "Nestle Milo":
        print("your Milo cost GHC25")
    elif miloo =="Richoco":
        print("your milo cost GHC20")
    else:
        print("please choose from the option given")
elif order == "Drink":
    alcoholic=input("Do you prefer alcoholic or Non-alcoholic:" )
    time.sleep(3)
    print(alcoholic)
    if alcoholic == "alcoholic":
        print("your drink cost GHC25")
    elif alcoholic =="Non-alcoholic":
        print("your drink cost GHC20")
    else:
        print("please choose from the option given")
else:
    print("please choose the items given")
    pass


print(x*2)

