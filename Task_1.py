import random
def curse_kitchen():
    print("\n\n\t\t......The Cursed Kitchen......")
    print("You are trapped in this magical kitchen.If you wish to break free and escape, you must cook the right dishes.\nBut remember cooking isn't so easy. "
      "Your cooking must please the magical kitchen. One wrong decision can make you trapped here forever.")
    while(True):
        print("\n\nYou get the following....")
        print("1. egg dish\n2. Sweet Dish")
        choice=input("\nType your choice[Egg dish/sweet dish] : ").lower()
        time=input("How long do you intend to cook [short/medium/long] :").lower()
        secret=input("Would you like to add secret spices provided by the Magical Box ? [yes/no] :").lower()
        decision=random.choice(["explosion","fail","success"])
        if(choice=="egg dish"):
            if(time=="medium" and secret=="yes" and decision=="success"):
                print("CONGRATULATIONS!!!!....You have prepared a perfect dish...And therby you break the curse...You can escape!!")
            elif(decision=="fail"):
                print("Your Dish tastes horrible....You are still Trapped!!")
            elif(decision=="explosion"):
                print("Oh No!!....Your Dish have exploded the kitchen!!")
        if(choice=="sweet dish"):
            if (time == "medium" and secret == "yes" and decision == "success"):
                print("CONGRATULATIONS!!!!....You have prepared a perfect Sweet dish...And therby you break the curse...You can escape!!")
            elif (decision == "fail"):
                print("Your Dish tastes horrible....You are still Trapped!!")
            elif (decision == "explosion"):
                print("Oh No!!....Your Dish have exploded the kitchen!!")

        play_again=input("\nDo You Want to Try another dish? [yes/no] : ").lower()
        if(play_again=='no'):
            print("\n\nThankyou for playing The Cursed Kitchen...Hope to see you soon!!!!!")
            break


curse_kitchen()