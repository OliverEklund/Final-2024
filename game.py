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
worker_1 = {'name':"John Deadbeat",'pay':20, 'upkeep':5, 'cost':25} 
worker_1_employed = False

worker_2 = {'name':"Stig godemann", 'pay':100, 'upkeep':30, 'cost':100}
worker_2_employed = False

worker_3 = {'name':"Arg Katt", 'pay':35, 'upkeep':10, 'cost':40}
worker_3_employed = False

worker_4 = {'name':"Allosaur the Cheat", 'pay':500, 'upkeep':100, 'cost':1000}
worker_4_employed = False

#Facilities
Facility_1_Name = "Real Burgers, Burger Place"
Facility_1_pay = 300
Facility_1_upkeep = 60
Facility_1_cost = 300
Facility_1_bought = False

Facility_2_Name = "Vik's Legally Distinct Vehicles"
Facility_2_pay = 500
Facility_2_upkeep = 100
Facility_2_cost = 700
Facility_2_bought = False

input("Are you ready to start? Press enter to continue: ")
print("/")

round_status = True
while round_status == True:

    
    Day = Day + 1
    print("/")
    print(f" It is now day {Day}. You have {Current_Money} dollars")
    print(f"Your company, {Company_Name} is making {Company_pay} dollars per day. Your daily upkeep is {Upkeep}")
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
        print("These are the workers available fow now. Pick which one of these you whould like to employ")
        print("/")
        
        if worker_1_employed== False:
            print(f"[1] {worker_1}")
        if worker_2_employed == False:
            print(f"[2] {worker_2}")
        if worker_3_employed == False:
            print(f"[3] {worker_3}")
        if worker_4_employed == False:
            print(f"[4] {worker_4}")
        print("/")

        employee_choice = input("")
        if employee_choice == "1" and worker_1_employed == False:
            print(f"You have hired {worker_1.get('name')}")
            worker_1_employed = True
            Company_pay = Company_pay + worker_1.get('pay')
            Upkeep = Upkeep + worker_1.get('upkeep')
            Current_Money = Current_Money - worker_1.get('cost')

        if employee_choice == "2" and worker_2_employed == False:
            print(f"You have hired {worker_2.get('name')}")
            worker_2_employed = True
            Company_pay = Company_pay + worker_2.get('pay')
            Upkeep = Upkeep + worker_2.get('upkeep')
            Current_Money = Current_Money - worker_2.get('cost')

        if employee_choice == "3" and worker_3_employed == False:
            print(f"You have hired {worker_3.get('name')}")
            worker_3_employed = True
            Company_pay = Company_pay + worker_3.get('pay')
            Upkeep = Upkeep + worker_3.get('upkeep')
            Current_Money = Current_Money - worker_3.get('cost')

        if employee_choice == "4" and worker_4_employed == False:
            print(f"You have hired {worker_4.get(name)}")
            worker_4_employed = True
            Company_pay = Company_pay + worker_4.get('pay')
            Upkeep = Upkeep * worker_4.get('upkeep')
            Current_Money = Current_Money - worker_4.get('cost')

    if action == "2":

        print("you chose [2] Buy a Facility. You go to Cheap_Franchise.com too look for one to buy.")
        print("/")
        print("These are the facilities available at the moment")
        print("/")

        if Facility_1_bought == False:
            print(f"[1] {Facility_1_Name}/ Income:{Facility_1_pay}/ Upkeep:{Facility_1_upkeep}/ Cost:{Facility_1_cost}")
        if Facility_2_bought == False:
            print(f"[2] {Facility_2_Name}/ Income:{Facility_2_pay}/ Upkeep:{Facility_2_upkeep}/ Cost:{Facility_2_cost}")
        
        Franchise_choice = input("")
        if Franchise_choice == "1" and Facility_1_bought == False:
            print(f"You have bought {Facility_1_Name}")
            Facility_1_bought = True
            Company_pay = Company_pay + Facility_1_pay
            Upkeep = Upkeep + Facility_1_upkeep
            Current_Money = Current_Money - Facility_1_cost
        
        if Franchise_choice == "2" and Facility_2_bought == False:
            print(f"You have bought {Facility_1_Name}")
            Facility_2_bought = True
            Company_pay = Company_pay + Facility_2_pay
            Upkeep = Upkeep + Facility_2_upkeep
            Current_Money = Current_Money - Facility_2_cost


    if action == "3":

        print("you chose [3] Manage Finances.")
        print("")

    if action == "4":
        print("you chose 4")


    Current_Money = Current_Money + (Company_pay - Upkeep)
    if Current_Money <0:
        print("You are bankrupt and you now live in a homeless shelter")
        break
    input("Ready for the next day?: ")

print("the end")