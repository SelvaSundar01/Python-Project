import random
from datetime import datetime

class account():
    def __init__(self):
        self.users = {}
        self.bookings = {}

    def signup(self):
        name = input("Enter Your Name   : ")
        number = int(input("Enter Your Number : "))
        password = int(input("Enter Your Password : "))
        otp = random.randrange(1000, 3000)
        print(f"Your otp is       : {otp}")
        user = int(input("Enter otp  : "))
        if user == otp:
            print(f"{name.capitalize()} Registered Successfully...")
            self.users[number] = {'name': name, 'password': password}
        else:
            print("Invalid otp")
            print("\n")
            self.signup()

    def login(self):
        number = int(input("Enter Your Mobile No : "))
        password = int(input("Enter Your Password : "))
        if number in self.users and self.users[number]['password'] == password:
            print(f"Login Successful. Welcome, {self.users[number]['name'].capitalize()}!")
            return self.users[number]['name'], number  # Return user name and number
        else:
            print("\n")
            print("Incorrect details. Please try again.")
            return self.login()


    def cancel_ticket(self, number):
        if number not in self.bookings:
            print("\nNo ticket found to cancel.")
            return

        booking = self.bookings[number]
        print("\nYour current booking:")
        print(f"From: {booking['chosen_place']} To: {booking['chosen_place1']}")
        print(f"Travel: {booking['travel_choice']}")
        print(f"Date: {booking['date_choice']}")
        print(f"Time: {booking['time_choice']}")
        print(f"Pickup: {booking['pick_point']} Drop: {booking['drop_point']}")
        print(f"Seats: {booking['seat_choice']}")
        print(f"Passengers: {[p['name'] for p in booking['person_name']]}")

        confirm = input("\nDo you want to cancel this ticket? (yes/no): ").lower()
        if confirm == 'yes':
            del self.bookings[number]
            print("\nYour ticket has been canceled successfully!")
        else:
            print("\nTicket cancellation aborted.")

class places():
    def __init__(self, place, tplace):
        self.place = place
        self.tplace = tplace

    def listofplace(self):
        print("\nChoose The Available Places..")
        for place in self.place:
            print("\t", place)

    def chooseplace(self):
        placename = input("Place From : ").title()
        if placename not in self.place:
            print("Choose Correct Destination ")
            return self.chooseplace()

        if placename in self.place:
            self.place.remove(placename)
            return placename

    def listofplace1(self):
        print("\nChoose The Available Places..")
        for toplace in self.tplace:
            print("\t", toplace)

    def chooseplace1(self):
        toplacename = input("Place to : ").title()
        if toplacename not in self.tplace:
            print("Choose Correct Destination ")
            return self.chooseplace1()
        if toplacename in self.tplace:
            self.tplace.remove(toplacename)
            print(f"Your Ticket is Confirmed.")
            return toplacename

class travels():
    def __init__(self, travel):
        self.travel = travel

    def listtravel(self):
        for travel in self.travel:
            print("\t", travel)

    def choosetravel(self):
        travelname = input("Choose Your Travelbus : ").title()
        if travelname not in self.travel:
            print("Wrong Travel bus!!! ")
            return self.choosetravel()
        if travelname in self.travel:
            self.travel.remove(travelname)
            return travelname

class times():
    def getdate(self):
        dated = input("Enter Travel Date (dd-mm-yyyy): ")
        try:
            dateobj = datetime.strptime(dated, "%d-%m-%Y")
            return dateobj.strftime('%d-%m-%Y')
        except ValueError:
            print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
            return self.getdate()

    def __init__(self, time):
        self.time = time

    def listtime(self):
        for time in self.time:
            print("\t", time)

    def choosetime(self):
        timename = input("Choose Your Timing : ")
        if timename not in self.time:
            print("Choose Correct Time  ")
            return self.choosetime()

        if timename in self.time:
            self.time.remove(timename)
            return timename

class picks():
    def __init__(self, pick):
        self.pick = pick

    def listpick(self):
        for pick in self.pick:
            print("\t", pick)

    def choosepick(self):
        pickpoint = input("Choose Your PickupPoint : ").title()
        if pickpoint not in self.pick:
            print("Enter Correct Pickpoint ")
            return self.choosepick()

        if pickpoint in self.pick:
            self.pick.remove(pickpoint)
            return pickpoint

class drops():
    def __init__(self, drop):
        self.drop = drop

    def listdrop(self):
        for drop in self.drop:
            print("\t", drop)

    def chooseddrop(self):
        droppoint = input("Choose Your DropPoint : ").title()
        if droppoint not in self.drop:
            print("Enter Correct DropPoint ")
            return self.chooseddrop()

        if droppoint in self.drop:
            self.drop.remove(droppoint)
            return droppoint

class persons():
    def __init__(self, person):
        self.person = person

    def listperson(self):
        for person in self.person:
            print("\t", person)

    def chooseperson(self):
        person_detail = input("How Many Person (One Person / Two Person :").title()
        if person_detail not in self.person:
            print("Enter a valid option (One Person/Two Person)")
            return self.chooseperson()
        else:
            self.person.remove(person_detail)
            if person_detail == "One Person":
                return self.enter_person_detail(1)
            if person_detail == "Two Person":
                return self.enter_person_detail(2)

    def enter_person_detail(self, num):
        details = []
        for i in range(num):
            print(f"Enter Person {i + 1} Details:")
            name = input("Enter Name: ").title()
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ").title()

            mobile = input("Enter Mobile No: ")
            details.append({"name": name, "age": age, "gender": gender, "mobile": mobile})
        return details

class seats():
    def __init__(self, seat):
        self.seat = seat

    def listseat(self):
        for seat in self.seat:
            print("\t", seat)

    def chooseseat(self):
        seatname = input("Choose The Seat No : ").title()
        if seatname not in self.seat:
            print("Enter Correct Seat No : ")
            return self.chooseseat()

        if seatname in self.seat:
            self.seat.remove(seatname)
            return seatname

class ticket():
    def ticketsumary(self, booking):
        print("Name           :", " and ".join([person['name'].title() for person in booking['person_name']]))
        print(f"Chosen Place   : {booking['chosen_place']} to {booking['chosen_place1']}")
        print(f"Travel         : {booking['travel_choice']}")
        print(f"Date           : {booking['date_choice']}")
        print(f"Timing         : {booking['time_choice']}")
        print(f"Pickup Point   : {booking['pick_point']}")
        print(f"Drop Point     : {booking['drop_point']}")
        print(f"Seat No        : {booking['seat_choice']}")
        print("\nThank you for booking with us!\n")

place = ["Chennai", "Madurai", "Palani", "Trichy", "Salem", "Thoothukudi"]
tplace = ["Bangalore", "Chennai", "Tenkasi", "Kerala", "Coimbatore", "Erode"]
travel = ["Selva Travels", "Sundar Travels", "Nat Travels", "Komban Travels"]
time = ["8pm to 5am", "7pm to 3am", "9pm to 6am", "10pm to 4am", "11pm to 7am"]
pick = ["Koyambedu", "Tambaram", "Ecr", "Kilambhakkam"]
drop = ["Trichy New Bus Stand", "Trichy Tollgate", "Trichy Old Bus Stand"]
person = ["One Person", "Two Person", "Three Person"]
seat = ["A1", "B1", "C1", "A2 A3", "B2 B3", "C2 C3"]

user_detail = account()
placed = places(place, tplace)
traveld = travels(travel)
timed = times(time)
picked = picks(pick)
droped = drops(drop)
personed = persons(person)
seated = seats(seat)
genrate = ticket()

menu = """
     1. Sign Up
     2. Login
     3. Book Ticket
     4. Cancel Ticket
     5. Exit
"""

while True:
    print("\n")
    print("Welcome To Bus Ticket Booking...")
    print(menu)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_detail.signup()

    elif choice == 2:
        name, user_number = user_detail.login()

    elif choice == 3:
        placed.listofplace()
        chosen_place = placed.chooseplace()

        placed.listofplace1()
        chosen_place1 = placed.chooseplace1()

        print("\nList of Travelbus")
        traveld.listtravel()
        travel_choice = traveld.choosetravel()

        print("\nEnter Your Travel Date ")
        date_choice = timed.getdate()

        print("\nList of Timing")
        timed.listtime()
        time_choice = timed.choosetime()

        print("\nList of Pickup Points")
        picked.listpick()
        pick_point = picked.choosepick()

        print("\nList of Drop Points")
        droped.listdrop()
        drop_point = droped.chooseddrop()

        print("\nList of Seats")
        seated.listseat()
        seat_choice = seated.chooseseat()

        print("\nList of Persons")
        personed.listperson()
        person_name = personed.chooseperson()

        booking = {
            "chosen_place": chosen_place,
            "chosen_place1": chosen_place1,
            "travel_choice": travel_choice,
            "date_choice": date_choice,
            "time_choice": time_choice,
            "pick_point": pick_point,
            "drop_point": drop_point,
            "seat_choice": seat_choice,
            "person_name": person_name
        }

        # Store the booking details for the user
        user_detail.bookings[user_number] = booking
        genrate.ticketsumary(booking)

    elif choice == 4:
        user_detail.cancel_ticket(user_number)

    elif choice == 5:
        print("Thank you for using our service!")
        break
    else:
        print("Invalid choice! Please try again.")
