print("You are young business entrepreneur looking to make some money, sadly you start a bit poor but hey you have ambition!")
print("In this game you will make need to make money but also enough money to sustain yourself and your business.")
print("You make choices each day (Represented in turns) that will determine the future of your business.")

import random
Player_Name = input("What is your name?: ")
Company_Name = input("What is the name of your company?: ")
Current_Money = 100
Day = 0
Company_pay = 0
#Taxes = 

input("Are you ready to start? Press enter to continue: ")
print("/")

round_status = True
while round_status == True:

    def random_name():
        first_names=('John','Andy','Joe')
        last_names=('Johnson','Smith','Williams')
        name_created=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(3))
    
    Day = Day + 1
    1q
    print(f" It is now day {Day}. You have {Current_Money} dollars")
    print(f"Your company, {Company_Name} is making {Company_pay} dollars per day.")
    print("/")

    choice = True
    while choice == True:
        print("What will you do?")
        print("[1] Hire a worker / [2] Buy a facility / [3] Manage Finances / [4] Do Nothing")
        action = input("")

        if action == "1" or "2" or "3" or "4":
            break
        else:
            print("i cant understand that")
    
    if action == "1":
        random_name()

        print("you chose [1] Hire a worker. You go to labour.com to find someone to employ so both of you can make money.")
        print("/")
        print("These are the workers available today. Pick which one of these you whould like to employ")
        print(f"{name_created}")


    if action == "2":
        print("you chose 2")
    if action == "3":
        print("you chose 3")
    if action == "4":
        print("you chose 4")

    input("Ready for the next day?: ")