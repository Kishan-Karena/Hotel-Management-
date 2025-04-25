import random
from datetime import date

class Hotel:
    def __init__(self):
        self.name = ["KRISH"]
        self.phno = ["8320614026"]
        self.add = ["GANDHINAGAR"]
        self.c_id = [1,]
        self.check_in = ["22/3/2023"]
        self.check_out = ["23/3/2023"]
        self.room = ["Standard Non-AC",]
        self.price = [3500,]
        self.roomno = ["303"]
        self.rs_bill = [2500,]
        self.chk = 0
        self.id = 1
        self.pay = [0,]
        self.day = [1,]
        self.home()
    def home(self):
        print("\t\t\t WELCOME TO HOTEL ANCASA")
        print("\t\t\t 1 Booking")
        print("\t\t\t 2 Rooms Info")
        print("\t\t\t 3 Room Service(Menu Card)")
        print("\t\t\t 4 Payment")
        print("\t\t\t 5 Record")
        ch = int(input("Enter Your Choice :"))
        if ch == 1:
            self.booking()
        elif ch == 2:
            self.Rooms_Info()
        elif ch == 3:
            self.restaurant()
        elif ch == 4 :
            self.payment()
        elif ch == 5:
            self.Record()
        else:
            print("----------------------")
            print("Wrong Choice Entered!!")
            print("Enter Again!!")
            print("----------------------")
            self.home()
    def booking(self):
        self.add_details()
        self.add_room_details()
        self.home()

    def add_details(self):
        c_name = str(input("Name: "))
        id = self.id+1
        self.id+=1
        c_phno = str(input("Phone No.: "))
        c_add = str(input("Address: "))


        c_check_in = str(input("Enter Check In Date In Format DD/MM/YYYY : "))
        c_check_out = str(input("Enter Check Out Date In Format DD/MM/YYYY : "))
        a=c_check_in.split("/")
        b=c_check_out.split("/")
        d0 = date(int(a[2]), int(a[1]), int(a[0]))
        d1 = date(int(b[2]), int(b[1]), int(b[0]))
        diff = d1 - d0
        self.day.append(int(diff.days))


        self.rs_bill.append(int(0))
        self.name.append(c_name)
        self.phno.append(c_phno)
        self.add.append(c_add)
        self.check_in.append(c_check_in)
        self.check_out.append(c_check_out)
        self.c_id.append(id)
        self.pay.append(0)


    def add_room_details(self):
        print("----SELECT ROOM TYPE----")
        print(" 1. Standard Non-AC")
        print(" 2. Standard AC")
        print(" 3. 3-Bed Non-AC")
        print(" 4. 3-Bed AC")
        print(("0. Room Prices"))
        ch = int(input("Enter Your Choice :"))
        if ch==0:
            print(" 1. Standard Non-AC - Rs. 3500")
            print(" 2. Standard AC     - Rs. 4000")
            print(" 3. 3-Bed Non-AC    - Rs. 4500")
            print(" 4. 3-Bed AC        - Rs. 5000")
            ch = int(input("Enter Your Choice :"))
        if ch==1:
            self.room.append('Standard Non-AC')
            print("Room Type- Standard Non-AC")
            self.price.append(3500)
            print("Price- 3500")
        elif ch==2:
            self.room.append('Standard AC')
            print("Room Type- Standard AC")
            self.price.append(4000)
            print("Price- 4000")
        elif ch==3:
            self.room.append('3-Bed Non-AC')
            print("Room Type- 3-Bed Non-AC")
            self.price.append(4500)
            print("Price- 4500")
        elif ch==4:
            self.room.append('3-Bed AC')
            print("Room Type- 3-Bed AC")
            self.price.append(5000)
            print("Price- 5000")
        else:
            print(" Wrong choice..!!")
            print("Enter Again!!")
            self.add_room_details()
        rn = random.randrange(40)+300

        while rn in self.roomno:
            rn = random.randrange(60)+300
        
        self.roomno.append(rn)

        print("")
        print("--------------------------------------------------------")
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
        print("Room No. - ",rn)
        print("Customer Id - ",self.c_id[(len(self.c_id)-1)])
        print("--------------------------------------------------------")
    def Rooms_Info(self):
        print("		 ------ HOTEL ROOMS INFO ------")
        print("")
        print("STANDARD NON-AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed, Television, Telephone,")
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
        print("an attached washroom with hot/cold water.\n")
        print("STANDARD NON-AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed, Television, Telephone,")
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
        print("an attached washroom with hot/cold water + Window/Split AC.\n")
        print("3-Bed NON-AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
        print("Side table, Balcony with an Accent table with 2 Chair and an")
        print("attached washroom with hot/cold water.\n")
        print("3-Bed AC")
        print("---------------------------------------------------------------")
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
        print("1 Side table, Balcony with an Accent table with 2 Chair and an")
        print("attached washroom with hot/cold water + Window/Split AC.\n\n")
        print()
        self.home()
    def restaurant(self):
        cus_id = int(input("Customer Id: "))
        r = 0
        for i in range(len(self.c_id)):
            if self.c_id[i]== cus_id:
                self.chk = 1
                print("-------------------------------------------------------------------------")
                print("						 Hotel AnCasa")
                print("-------------------------------------------------------------------------")
                print("						 Menu Card")
                print("-------------------------------------------------------------------------")
                print("\n BEVARAGES							 26 Dal Fry................ 140.00")
                print("----------------------------------	 27 Dal Makhani............ 150.00")
                print(" 1 Regular Tea............. 20.00	 28 Dal Tadka.............. 150.00")
                print(" 2 Masala Tea.............. 25.00")
                print(" 3 Coffee.................. 25.00	 ROTI")
                print(" 4 Cold Drink.............. 25.00	 ----------------------------------")
                print(" 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00")
                print(" 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00")
                print(" 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00")
                print(" 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00")
                print(" 9 Cheese Toast Sandwich... 70.00")
                print(" 10 Grilled Sandwich........ 70.00	 RICE")
                print("									 ----------------------------------")
                print(" SOUPS								 33 Plain Rice.............. 90.00")
                print("----------------------------------	 34 Jeera Rice.............. 90.00")
                print(" 11 Tomato Soup............ 110.00	 35 Veg Pulao.............. 110.00")
                print(" 12 Hot & Sour............. 110.00	 36 Peas Pulao............. 110.00")
                print(" 13 Veg. Noodle Soup....... 110.00")
                print(" 14 Sweet Corn............. 110.00	 SOUTH INDIAN")
                print(" 15 Veg. Munchow........... 110.00	 ----------------------------------")
                print("									 37 Plain Dosa............. 100.00")
                print(" MAIN COURSE						 38 Onion Dosa............. 110.00")
                print("----------------------------------	 39 Masala Dosa............ 130.00")
                print(" 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00")
                print(" 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00")
                print(" 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00")
                print(" 19 Palak Paneer........... 120.00")
                print(" 20 Chilli Paneer.......... 140.00	 ICE CREAM")
                print(" 21 Matar Mushroom......... 140.00	 ----------------------------------")
                print(" 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00")
                print(" 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00")
                print(" 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00")
                print(" 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00")
                print("Press 0 -to end ")
                ch=1
                while(ch!=0):
                
                    ch=int(input(" -> "))
                    if ch==1 or ch==31 or ch==32:
                        rs=20
                        r=r+rs
                    elif ch<=4 and ch>=2:
                        rs=25
                        r=r+rs
                    elif ch<=6 and ch>=5:
                        rs=30
                        r=r+rs
                    elif ch<=8 and ch>=7:
                        rs=50
                        r=r+rs
                    elif ch<=10 and ch>=9:
                        rs=70
                        r=r+rs
                    elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
                        rs=110
                        r=r+rs
                    elif ch<=19 and ch>=18:
                        rs=120
                        r=r+rs
                    elif (ch<=26 and ch>=20) or ch==42:
                        rs=140
                        r=r+rs
                    elif ch<=28 and ch>=27:
                        rs=150
                        r=r+rs
                    elif ch<=30 and ch>=29:
                        rs=15
                        r=r+rs
                    elif ch==33 or ch==34:
                        rs=90
                        r=r+rs
                    elif ch==37:
                        rs=100
                        r=r+rs
                    elif ch<=41 and ch>=39:
                        rs=130
                        r=r+rs
                    elif ch<=46 and ch>=43:
                        rs=60
                        r=r+rs
                    elif ch==0:
                        pass
                    else:
                        print("Wrong Choice..!!")
                print("Total Bill: ",r)
                self.rs_bill[i] = r
            else:
                pass
        if self.chk == 0:
            print("No Data Found Enter Customer Id Again!!")
            self.restaurant()
        else:
            self.chk = 0
        self.home()
    def payment(self):
        cus_id = int(input("Enter Customer Id :"))
        for i in range(len(self.c_id)):
            if cus_id == self.c_id[i]:
                if self.pay[i] == 0 :
                    print(" Payment")
                    print(" --------------------------------")
                    print(" MODE OF PAYMENT")
                    
                    print(" 1- Credit/Debit Card")
                    print(" 2- Paytm/PhonePe")
                    print(" 3- Using UPI")
                    print(" 4- Cash")
                    x=int(input("-> "))
                    print(type(self.day[i]))
                    print("\n Amount: ",(self.price[i]*self.day[i])+(self.rs_bill[i]))
                    print("\n		 Pay For AnCasa")
                    print(" (y/n)")
                    ch=str(input("->"))

                    if(ch == "Y" or ch == "y"):
                        print("\n\n --------------------------------")
                        print("		 Hotel AnCasa")
                        print(" --------------------------------")
                        print("			 Bill")
                        print(" --------------------------------")
                        print(" Name: ",self.name[i],"\t\n Phone No.: ",self.phno[i],"\t\n Address: ",self.add[i],"\t")
                        print("\n Check-In: ",self.check_in[i],"\t\n Check-Out: ",self.check_out[i],"\t")
                        print("\n Room Type: ",self.room[i],"\t\n Room Charges: ",self.price[i]*self.day[i],"\t")
                        print(" Restaurant Charges: \t",self.rs_bill[i])
                        print(" --------------------------------")
                        print("\n Total Amount: ",(self.price[i]*self.day[i])+(self.rs_bill[i]),"\t")
                        print(" --------------------------------")
                        print("		 Thank You")
                        print("		 Visit Again :)")
                        print(" --------------------------------\n")
                        self.name.pop(i)
                        self.phno.pop(i)
                        self.add.pop(i)
                        self.c_id.pop(i)
                        self.check_in.pop(i)
                        self.check_out.pop(i)
                        self.room.pop(i)
                        self.price.pop(i)
                        self.roomno.pop(i)
                        self.rs_bill.pop(i)
                        self.pay.pop(i)
                        self.day.pop(i)
                self.chk = 1
        if self.chk == 0:
            print("For Enter ID Again Enter 1")
            print("For Go Back Enter 0")
            ch = input("Enter Your Choice :")
            if ch == 1:
                self.payment()
            else:
                self.home()
        else:
            self.chk = 0
        self.home()
    def Record(self):
            print("	 *** HOTEL RECORD ***\n")
            print("| Name	  \t| Phone No. \t| Address	 | Check-In \t| Check-Out	 | Room Type	 \t| Price	 \t|")
            print("----------------------------------------------------------------------------------------------------------------------")
            
            for i in range(len(self.name)):
                print("|",self.name[i],"\t |",self.phno[i],"\t|",self.add[i],"\t|",self.check_in[i],"\t|",self.check_out[i],"\t|",self.room[i],"\t|",self.price[i])
            print("----------------------------------------------------------------------------------------------------------------------")
            self.home()
H = Hotel()