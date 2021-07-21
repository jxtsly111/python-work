import time
country = input("please enter your country name,country should be in this section(australia,ghana,nigeria):")
print(country)
if country == "australia":
    print("we will ask you some questions concerning australia")
    time.sleep(2)
    sport = input("Has your country won the world cup before(yes or no):")
    print("sport")
    if sport == "yes":
        print("Your country has a good remark")
    elif sport =="no":
        print("Best wishes to your country for the upcoming world cup tournament")
    else:
        print("please stick to the option")
        pass
elif country =="ghana":
    print("we will ask you some questions concerning Ghana")
    time.sleep(2)
    sport = input("Has your country won the world cup before(yes or no):")
    print("sport")
    if sport == "yes":
        print("Your country has a good remark")
    elif sport =="no":
        print("Best wishes to your country for the upcoming world cup tournament")
    else:
        print("please stick to the option")
        pass
elif country =="nigeria":
    print("we will ask you some questions concerning nigeria")
    time.sleep(2)
    sport = input("Has your country won the world cup before(yes or no):")
    print("sport")
    if sport == "yes":
        print("Your country has a good remark")
    elif sport =="no":
        print("Best wishes to your country for the upcoming world cup tournament")
    else:
        print("please stick to the option")
        pass
else:
    print("please stick to the option given")


    pass