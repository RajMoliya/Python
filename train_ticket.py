class Train:
    global liseats
    liseats = []
    global totalSeats
    totalSeats =[]
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        for i in range(1,seats+1):
            liseats.append(str(i))
        for i in range(1,seats+1):
            totalSeats.append(str(i))
    def getStatus(self):
        print(f"Name of Train : {self.name}")
        print(f"Number of Seats : {self.seats}")
        print(f"Total of Fare : Rs.{self.fare}")
        print(f"Name of seats available : {liseats}")
    def bookTicket(self):
        if self.seats>0:
            print(f"Your ticket has been booked at seat no. : {self.seats}")
            self.liseats = liseats.remove(liseats[-1])
            self.seats = self.seats - 1
        else:
            print("Train is full")
    def cancelTicket(self):
        a = input("Enter seat no. to cancel Ticket")
        if a in liseats:
            print("Invalid")
        else:
            if a in totalSeats:
                print("Your ticket has been cancelled successfully")
                self.liseats = liseats.append(str(a))
                self.seats = self.seats + 1
            else:
                print("Ivalid")
train1 = Train("RajDhani",75,3)
train1.getStatus()
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
train1.cancelTicket()
train1.cancelTicket()
train1.getStatus()


    