print("You are young business entrepreneur looking to make some money, sadly you start a bit poor but hey you have ambition!")
print("In this game you will make need to make money but also enough money to sustain yourself and your business.")
print("You make choices each day (Represented in turns) that will determine the future of your business.")

from random import randint
Player_Name = input("What is your name?: ")
Company_Name = input("What is the name of your company?: ")
Current_Money = 100
Day = 0
Company_pay = 0
Upkeep = 0

#WORKERS:
worker_1_name = "John Deadbeat"
worker_1_pay = 15
worker_1_upkeep = 1
worker_1_cost = 20
worker_1_employed = False

worker_2_name = "Stig godemann"
worker_2_pay = 1.2 #20% more money
worker_2_upkeep = 30
worker_2_cost = 100
worker_2_employed = False

worker_3_name = "Arg Katt"
worker_3_pay = 30
worker_3_upkeep = 10
worker_3_cost = 15
worker_3_employed = False

worker_4_name = "Allosaur the Cheat"
worker_4_pay = 2
worker_4_upkeep = 0.7 #30% less upkeep
worker_4_cost = 120
worker_4_employed = False

input("Are you ready to start? Press enter to continue: ")
print("/")

round_status = True
while round_status == True:

    
    Day = Day + 1
    print("/")
    print(f" It is now day {Day}. You have {Current_Money} dollars")
    print(f"Your company, {Company_Name} is making {Company_pay} dollars per day. Your daily upkeep is {worker_1_upkeep}")
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

        print("you chose [1] Hire a worker. You go to labour.com to find someone to employ so both of you can make money.")
        print("/")
        print("These are the workers available today. Pick which one of these you whould like to employ")
        print("/")
        
        if worker_1_employed == False:
            print(f"[1] {worker_1_name}/ Income:{worker_1_pay}/ Salary:{worker_1_upkeep}/ Cost:{worker_1_cost}")
        if worker_2_employed == False:
            print(f"[2] {worker_2_name}/ Income:20% more total money/ Salary:{worker_2_upkeep}/ Cost:{worker_2_cost}")
        if worker_3_employed == False:
            print(f"[3] {worker_3_name}/ Income:{worker_3_pay}/ Salary:{worker_3_upkeep}/ Cost:{worker_3_cost}")
        if worker_4_employed == False:
            print(f"[4] {worker_4_name}/ Income:{worker_4_pay}/ Salary:30% less upkeep/ Cost:{worker_4_cost}")
        print("/")

        employee_choice = input("")
        if employee_choice == "1" and worker_1_employed == False:
            print(f"You have hired {worker_1_name}")
            worker_1_employed = True
            Company_pay = Company_pay + worker_1_pay
            Upkeep = Upkeep + worker_1_upkeep
            Current_Money = Current_Money - worker_1_cost

        if employee_choice == "2" and worker_2_employed == False:
            print(f"You have hired {worker_2_name}")
            worker_2_employed = True
            Company_pay = Company_pay * worker_2_pay
            Upkeep = Upkeep + worker_2_upkeep
            Current_Money = Current_Money - worker_2_cost

        if employee_choice == "3" and worker_3_employed == False:
            print(f"You have hired {worker_3_name}")
            worker_3_employed = True
            Company_pay = Company_pay + worker_3_pay
            Upkeep = Upkeep + worker_3_upkeep
            Current_Money = Current_Money - worker_3_cost

        if employee_choice == "4" and worker_4_employed == False:
            print(f"You have hired {worker_4_name}")
            worker_4_employed = True
            Company_pay = Company_pay + worker_4_pay
            Upkeep = Upkeep * worker_4_upkeep
            Current_Money = Current_Money - worker_4_cost

    if action == "2":
        print("you chose 2")
    if action == "3":
        print("you chose 3")
    if action == "4":
        print("you chose 4")


    Current_Money = Current_Money + (Company_pay - Upkeep)
    input("Ready for the next day?: ")