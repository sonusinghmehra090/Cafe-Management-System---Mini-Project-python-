# menu
running=True
while running:

    totalbill=[]
    menurunning=True

    while menurunning:
        print("Welcome to our restaurant. Here's the menu")
        print("Pizza: Rs 40\nPasta : Rs 50\nBurger : Rs 60 \nSalad: Rs 70 \nCoffee: Rs 80\nExit")
        order=input("Enter your item you want to order = ").lower().strip()
        
        if order=="pizza":
            print("anything else ?")
            choice=input("enter [y]|[n] ").lower().strip()
            if choice == "y":
                totalbill.append(40)
                continue 
            else:
                totalbill.append(40)
                print("your total bill :",sum(totalbill))
                running=False
                menurunning=False



        if order=="pasta":
            print("anything else ?")
            choice=input("enter [y]|[n] ").lower().strip()
            if choice == "y":
                totalbill.append(50)
                continue 
            else:
                totalbill.append(50)
                print("your total bill :",sum(totalbill))
                running=False
                menurunning=False
                

        if order=="burger":
            print("anything else ?")
            choice=input("enter [y]|[n] ").lower().strip()
            if choice == "y":
                totalbill.append(60)
                continue 
            else:
                totalbill.append(60)
                print("your total bill :",sum(totalbill))
                running=False
                menurunning=False
        
        if order=="salad":
            print("anything else ?")
            choice=input("enter [y]|[n] ").lower().strip()
            if choice == "y":
                totalbill.append(70)
                continue 
            else:
                totalbill.append(70)
                print("your total bill :",sum(totalbill))
                running=False
                menurunning=False
        
        if order=="coffee":
            print("anything else ?")
            choice=input("enter [y]|[n] ").lower().strip()
            if choice == "y":
                totalbill.append(80)
                continue 
            else:
                totalbill.append(80)
                print("your total bill :",sum(totalbill))
                running=False
                menurunning=False

        if order=="exit":
            print("OKAY HAVE A NICE DAY !")
            running=False
            menurunning=False



        
