m = 1
while 0 < m:

    class Train:
        def __init__(self,name,fare,seats):
            self.name = name
            self.fare = fare
            self.seats = seats

        def getFareInfo(self):
            print("*************")
            print(f"The name of the train is {self.name}")
            print(f"The seats available are {self.seats}")
            print("*************")

        def getFare(self):
            print(f"The fare of {self.name} express is {self.fare}")

        def bookTkt(self):
            if(self.seats > 0 ):
                print(f"Congrats !!! Your seat has been booked. Your seat no is {self.seats}")
                self.seats = self.seats - 1

            else:
                print("Sorry this train is full ... Please try for TATKAL")

        def cancelTkt(self):
            if(self.seats > 0):
                print("Your ticket has been cancelled !!! , We will miss you :( ")
                self.seats = self.seats + 1
            else:
                print("Cancellation failed")


    y = input("Select options : Get fare info press(f), Book ticket(b), Cancel Ticket(c), Exit(e) \t \n")
    x = input("Select train name Rajdhani(r),Garib Rath(g) \t \n")


    if(x == "r"):
        x = "Rajdhani"
        print(f"Selected option is : {x} \n")
    elif( x == "g"):
        x = "GaribRath"
        print(f"Selected option is : {x} \n")
    else:
        print("Something went wrong :( please make a right choice.")
        break

    Check = Train( x , "90 RS" , 100)

   


    if (y == "f"):
        y = "Fare Info"
        print(f"Selected option is : {y} \n")
        Check.getFareInfo()
        
        
    elif(y == "b"):
        y = "Book Ticket"
        print(f"Selected option is : {y} \n")
        Check.bookTkt()

        while 0 < m:
            ni = input("Do you want to book a ticket again ? (y)/(n) \t \n") 
            if(ni == "y"):
                Check.bookTkt()
            elif(ni == "n"):
                break   
            

    elif(y == "c"):
        y = "Cancel Ticket"
        print(f"Selected option is : {y} \n")
        Check.cancelTkt()

    elif(y == "e"):
        y = "***Exit***"
        print(f"Selected option is : {y} \n")
        m = m -2
    else:
        print("Something went wrong :( please make a right choice.")
        break

        

        

