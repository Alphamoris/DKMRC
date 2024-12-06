"A project licensed by Dhanush@Alphamoris"
"if any contact alphamoris45@gmail.com"
import mysql.connector as Module
connectionobj=Module.connect(user="root",password="dk@1234",host="localhost")
cursorobj=connectionobj.cursor()
Display1=print('Welcome to \" DKMRC \" Technology Specialized Hospital')
cursorobj.execute("create database DKMRC")
cursorobj.execute("use DKMRC")
Patient_Table="create table Patients_Table(Patient_ID int primary key,Patient_Name char(30) not null,Type char(15) Default \"General\",Date_Of_Birth date,Address char(100) not null,Phone_No bigint,Age int,Sex enum('Male','Female','Others'))"
Ortho_Table="create table Ortho_Table(Patient_ID int primary key,Patient_Name char(30) not null,Last_Visit_On date,Doctor_ID int not null,Doctor_name char(100) not null,Fees_paid bigint,Pending_Fees bigint)"
Cardiology_Table="create table Cardiology_table(Patient_ID int primary key,Patient_Name char(30) not null,Last_Visit_On date,Doctor_ID int not null,Doctor_name char(100) not null,Fees_paid bigint,Pending_Fees bigint)"
Radiology_Table="create table Radiology_Table(Patient_ID int primary key,Patient_Name char(30) not null,Last_Visit_On date,Doctor_ID int not null,Doctor_name char(100) not null,Fees_paid bigint,Pending_Fees bigint)"
Neurology_Table="create table Neurology_Table(Patient_ID int primary key,Patient_Name char(30) not null,Last_Visit_On date,Doctor_ID int not null,Doctor_name char(100) not null,Fees_paid bigint,Pending_Fees bigint)"
Pediatrics_Table="create table Pediatrics_Table(Patient_ID int primary key,Patient_Name char(30) not null,Last_Visit_On date,Doctor_ID int not null,Doctor_name char(100) not null,Fees_paid bigint,Pending_Fees bigint)"
Psychiatry_Table="create table Psychiatry_Table(Patient_ID int primary key,Patient_Name char(30) not null,Last_Visit_On date,Doctor_ID int not null,Doctor_name char(100) not null,Fees_paid bigint,Pending_Fees bigint)"
Doctors_Table="create table Doctors_table(Doctor_ID int Primary key,Doctor_Name char(40) not null,Type char(40) not null,Available_From_Date date not null,Available_To_Date date not null,Available_From_Time time not null,Available_To_Time time not null,Fees_Per_Hour int,Sex enum(\"Male\",\"Female\",\"Others\"),Address char(100),Age int)"
Feedback_Table="create table Feedback_Table(Patient_ID int not null,Patient_Name char(50),Feedback varchar(1000))"
cursorobj.execute(Patient_Table)
cursorobj.execute(Ortho_Table)
cursorobj.execute(Cardiology_Table)
cursorobj.execute(Radiology_Table)
cursorobj.execute(Neurology_Table)
cursorobj.execute(Pediatrics_Table)
cursorobj.execute(Psychiatry_Table)
cursorobj.execute(Doctors_Table)
cursorobj.execute(Feedback_Table)
Display2=print("We offer Happieness In The Highest Form Of Health")
def Login_Page():
    Display3=print('''Kindly Choose your Category
          (1)ADMIN
          (2)USER''')
    
def Tables_Menu():
        Display4=print('''Plaease Choose Your Department
            (1)Ortho
            (2)Cardiology
            (3)Radiology
            (4)Neurology
            (5)Pediatrics
            (6)psychiatry
            (7)Patient Details
            (8)Doctor Details''')
        def Return():
            Display6=print('''(1)Return To The Login Page
(2)Return To The Tables Menu''')
            Input24=input("Enter The Numeral:")
            if Input24=="1":
                    Login_Page()
                    Basic()
            elif Input24=="2":
                    Tables_Menu()                       
            else:
                print("Enter A Valid Numeral")
                Tables_Menu()

            
        Input10=input("Enter The Numeral:")
        if Input10=="1":
            print('''Menu:
        (1)To Insert New Record
        (2)To update the Record
        (3)To Fetch Information''')      
            Input11=input("Enter The Numeral:")
            if Input11=="1":
                Input2=int(input("How Many Records Are To Be Inserted:"))
                for loop1 in range(1,Input2+1):
                    Display5=print("Enter The Patient_ID",loop1)
                    Input3=int(input(":"))
                    Display6=print("Enter Patient_Name",loop1)
                    Input4=input(":")
                    Display7=print("Enter Last Visit Date",loop1)
                    Input5=input(":")
                    Display8=print("Enter Doctor_ID",loop1)
                    Input6=int(input(":"))
                    Display9=print("Enter Doctor_Name",loop1)
                    Input7=input(":")
                    Dispaly10=print("Enter Fees_Paid",loop1)
                    Input8=int(input(":"))
                    Display11=print("Enter Pending Fees",loop1)
                    Input9=int(input(":"))
                    Insert_Record="Insert into Ortho_Table Values(%s,\"%s\",\"%s\",%s,\"%s\",%s,%s)"%(Input3,Input4,Input5,Input6,Input7,Input8,Input9)
                    cursorobj.execute(Insert_Record)
                    connectionobj.commit()
                print("All Records Are Inserted Successfully")    
                Return()
            elif Input11=="2":
                Input19=int(input("How Many Records You Need To Update:"))
                Display5=print('''Which Column Would You Like To Update
    (1)Patient_Name
    (2)Last Visit Date
    (3)Doctor ID
    (4)Doctor Name
    (5)Fees Paid
    (6)Pending Fees''')
                Input20=input("Enter The Numeral:")
                if Input20=="1":
                  for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Patient_Name:")
                      Update_P_Name="update Ortho_Table set Patient_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                  print("Records Are Updated Successfully")
                  Return()
                elif Input20=="2":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Last_Visit_Date:")
                      Update_P_Name="update Ortho_Table set Last_Visit_On=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="3":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_ID:")
                      Update_P_Name="update Ortho_Table set Doctor_ID=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()

                elif Input20=="4":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_Name:")
                      Update_P_Name="update Ortho_Table set Doctor_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="5":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Fees_Paid:")
                      Update_P_Name="update Ortho_Table set Fees_Paid=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="6":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Pending_Fees:")
                      Update_P_Name="update Ortho_Table set Pending_Fees=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                else:
                    print("Enter A Valid Numeral!!")
                    Tables_Menu()
            elif Input11=="3":
                Display8=print('''(1)Retrieve Records Using Patient_ID
    (2)Retrieve Records using Last Visit Date
    (3)Retrieving Records Who Have Pending Fees''')
                Input25=input("Enter The Numeral:")
                if Input25=="1":
                    print('''(1)Retrieve Records Using Specific Patient_ID
    (2)Retrieve Records Using specific Interval of Patient_ID''')
                    Input26=input("Enter The Numeral:")
                    if Input26=="1":
                        Input27=int(input("How Many Records You Need to Retrieve:"))
                        for loop3 in range(1,Input27+1):
                            Display9=print("Enter Patient_ID",loop3)
                            Input27=input(":")
                            Retrieve_Record1="select * from Ortho_Table where Patient_ID=%s"%(Input27)
                            cursorobj.execute(Retrieve_Record1) 
                            Retrieved_Records1=cursorobj.fetchone()
                            print(Retrieved_Records1)
                        Return()    
                    elif Input26=="2":
                        Input28=input("Enter Starting Patient_ID:")
                        Input29=input("Enter Ending Patient_ID:")
                        Retrieve_Record2="select * from Ortho_Table where Patient_ID Between %s and %s"%(Input28,Input29)
                        cursorobj.execute(Retrieve_Record2)
                        Retrieved_Records2=cursorobj.fetchall()
                        for loop4 in Retrieved_Records2:
                            print(loop4)
                        Return()    
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                elif Input25=="2":
                    Input30=input("Enter From Date:")
                    Input31=input("Enter To Date:")
                    Retrieve_Record3="select * from Ortho_Table Where Last_Visit_On Between \"%s\" And \"%s\""%(Input30,Input31)
                    cursorobj.execute(Retrieve_Record3)
                    Retrieved_Records3=cursorobj.fetchall()
                    for loop4 in Retrieved_Records3:
                        print(loop4)
                    Return()    
                elif Input25=="3":
                    Retrieve_Record4="select * from Ortho_Table where Pending_Fees Is Not null"
                    cursorobj.execute(Retrieve_Record4)
                    Retrieved_Records4=cursorobj.fetchall()
                    for loop5 in Retrieved_Records4:
                        print(loop5)
                    Return()
                else:
                    print("Enter A Valid Numeral")
                    Tables_Menu()
            else:
                print("Enter A Valid Numeral")
                Tables_Menu()
        if Input10=="2":
            print('''Menu:
        (1)To Insert New Record
        (2)To update the Record
        (3)To Fetch Information''')
            Input11=input("Enter The Numeral:")
            if Input11=="1":
                Input2=int(input("How Many Records Are To Be Inserted:"))
                for loop1 in range(1,Input2+1):
                    Display5=print("Enter The Patient_ID",loop1)
                    Input3=int(input(":"))
                    Display6=print("Enter Patient_Name",loop1)
                    Input4=input(":")
                    Display7=print("Enter Last Visit Date",loop1)
                    Input5=input(":")
                    Display8=print("Enter Doctor_ID",loop1)
                    Input6=int(input(":"))
                    Display9=print("Enter Doctor_Name",loop1)
                    Input7=input(":")
                    Dispaly10=print("Enter Fees_Paid",loop1)
                    Input8=int(input(":"))
                    Display11=print("Enter Pending Fees",loop1)
                    Input9=int(input(":"))
                    Insert_Record="Insert into Cardiology_Table Values(%s,\"%s\",\"%s\",%s,\"%s\",%s,%s)"%(Input3,Input4,Input5,Input6,Input7,Input8,Input9)
                    cursorobj.execute(Insert_Record)
                    connectionobj.commit()
                print("All Records Are Inserted Successfully")    
                Return()
            elif Input11=="2":
                Input19=int(input("How Many Records You Need To Update:"))
                Display5=print('''Which Column Would You Like To Update
    (1)Patient_Name
    (2)Last Visit Date
    (3)Doctor ID
    (4)Doctor Name
    (5)Fees Paid
    (6)Pending Fees''')
                Input20=input("Enter The Numeral:")
                if Input20=="1":
                  for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Patient_Name:")
                      Update_P_Name="update Cardiology_Table set Patient_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                  print("Records Are Updated Successfully")
                  Return()
                elif Input20=="2":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Last_Visit_Date:")
                      Update_P_Name="update Cardiology_Table set Last_Visit_On=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="3":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_ID:")
                      Update_P_Name="update Cardiology_Table set Doctor_ID=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()

                elif Input20=="4":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_Name:")
                      Update_P_Name="update Cardiology_Table set Doctor_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="5":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Fees_Paid:")
                      Update_P_Name="update Cardiology_Table set Fees_Paid=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="6":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Pending_Fees:")
                      Update_P_Name="update Cardiology_Table set Pending_Fees=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                else:
                    print("Enter A Valid Numeral!!")
                    Tables_Menu()
            elif Input11=="3":
                Display8=print('''(1)Retrieve Records Using Patient_ID
    (2)Retrieve Records using Last Visit Date
    (3)Retrieving Records Who Have Pending Fees''')
                Input25=input("Enter The Numeral:")
                if Input25=="1":
                    print('''(1)Retrieve Records Using Specific Patient_ID
    (2)Retrieve Records Using specific Interval of Patient_ID''')
                    Input26=input("Enter The Numeral:")
                    if Input26=="1":
                        Input27=int(input("How Many Records You Need to Retrieve:"))
                        for loop3 in range(1,Input27+1):
                            Display9=print("Enter Patient_ID",loop3)
                            Input27=input(":")
                            Retrieve_Record1="select * from Cardiology_Table where Patient_ID=%s"%(Input27)
                            cursorobj.execute(Retrieve_Record1) 
                            Retrieved_Records1=cursorobj.fetchone()
                            print(Retrieved_Records1)
                        Return()    
                    elif Input26=="2":
                        Input28=input("Enter Starting Patient_ID:")
                        Input29=input("Enter Ending Patient_ID:")
                        Retrieve_Record2="select * from Cardiology_Table where Patient_ID Between %s and %s"%(Input28,Input29)
                        cursorobj.execute(Retrieve_Record2)
                        Retrieved_Records2=cursorobj.fetchall()
                        for loop4 in Retrieved_Records2:
                            print(loop4)
                        Return()    
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                elif Input25=="2":
                    Input30=input("Enter From Date:")
                    Input31=input("Enter To Date:")
                    Retrieve_Record3="select * from cardiology_Table Where Last_Visit_On Between \"%s\" And \"%s\""%(Input30,Input31)
                    cursorobj.execute(Retrieve_Record3)
                    Retrieved_Records3=cursorobj.fetchall()
                    for loop4 in Retrieved_Records3:
                        print(loop4)
                    Return()    
                elif Input25=="3":
                    Retrieve_Record4="select * from Cardiology_Table where Pending_Fees Is Not null"
                    cursorobj.execute(Retrieve_Record4)
                    Retrieved_Records4=cursorobj.fetchall()
                    for loop5 in Retrieved_Records4:
                        print(loop5)
                    Return()
                else:
                    print("Enter A Valid Numeral")
                    Tables_Menu()
            else:
                print("Enter A Valid Numeral")
                Tables_Menu()
        if Input10=="3":
            print('''Menu:
        (1)To Insert New Record
        (2)To update the Record
        (3)To Fetch Information''')
            Input11=input("Enter The Numeral:")
            if Input11=="1":
                Input2=int(input("How Many Records Are To Be Inserted:"))
                for loop1 in range(1,Input2+1):
                    Display5=print("Enter The Patient_ID",loop1)
                    Input3=int(input(":"))
                    Display6=print("Enter Patient_Name",loop1)
                    Input4=input(":")
                    Display7=print("Enter Last Visit Date",loop1)
                    Input5=input(":")
                    Display8=print("Enter Doctor_ID",loop1)
                    Input6=int(input(":"))
                    Display9=print("Enter Doctor_Name",loop1)
                    Input7=input(":")
                    Dispaly10=print("Enter Fees_Paid",loop1)
                    Input8=int(input(":"))
                    Display11=print("Enter Pending Fees",loop1)
                    Input9=int(input(":"))
                    Insert_Record="Insert into Radiology_Table Values(%s,\"%s\",\"%s\",%s,\"%s\",%s,%s)"%(Input3,Input4,Input5,Input6,Input7,Input8,Input9)
                    cursorobj.execute(Insert_Record)
                    connectionobj.commit()
                print("All Records Are Inserted Successfully")    
                Return()
            elif Input11=="2":
                Input19=int(input("How Many Records You Need To Update:"))
                Display5=print('''Which Column Would You Like To Update
    (1)Patient_Name
    (2)Last Visit Date
    (3)Doctor ID
    (4)Doctor Name
    (5)Fees Paid
    (6)Pending Fees''')
                Input20=input("Enter The Numeral:")
                if Input20=="1":
                  for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Patient_Name:")
                      Update_P_Name="update Radiology_Table set Patient_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                  print("Records Are Updated Successfully")
                  Return()
                elif Input20=="2":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Last_Visit_Date:")
                      Update_P_Name="update Radiology_Table set Last_Visit_On=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="3":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_ID:")
                      Update_P_Name="update Radiology_Table set Doctor_ID=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()

                elif Input20=="4":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_Name:")
                      Update_P_Name="update Radiology_Table set Doctor_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="5":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Fees_Paid:")
                      Update_P_Name="update Radiology_Table set Fees_Paid=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="6":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Pending_Fees:")
                      Update_P_Name="update Radilology_Table set Pending_Fees=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                else:
                    print("Enter A Valid Numeral!!")
                    Tables_Menu()
            elif Input11=="3":
                Display8=print('''(1)Retrieve Records Using Patient_ID
    (2)Retrieve Records using Last Visit Date
    (3)Retrieving Records Who Have Pending Fees''')
                Input25=input("Enter The Numeral:")
                if Input25=="1":
                    print('''(1)Retrieve Records Using Specific Patient_ID
    (2)Retrieve Records Using specific Interval of Patient_ID''')
                    Input26=input("Enter The Numeral:")
                    if Input26=="1":
                        Input27=int(input("How Many Records You Need to Retrieve:"))
                        for loop3 in range(1,Input27+1):
                            Display9=print("Enter Patient_ID",loop3)
                            Input27=input(":")
                            Retrieve_Record1="select * from Radiology_Table where Patient_ID=%s"%(Input27)
                            cursorobj.execute(Retrieve_Record1) 
                            Retrieved_Records1=cursorobj.fetchone()
                            print(Retrieved_Records1)
                        Return()    
                    elif Input26=="2":
                        Input28=input("Enter Starting Patient_ID:")
                        Input29=input("Enter Ending Patient_ID:")
                        Retrieve_Record2="select * from Radiology_Table where Patient_ID Between %s and %s"%(Input28,Input29)
                        cursorobj.execute(Retrieve_Record2)
                        Retrieved_Records2=cursorobj.fetchall()
                        for loop4 in Retrieved_Records2:
                            print(loop4)
                        Return()    
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                elif Input25=="2":
                    Input30=input("Enter From Date:")
                    Input31=input("Enter To Date:")
                    Retrieve_Record3="select * from Radiology_Table Where Last_Visit_On Between \"%s\" And \"%s\""%(Input30,Input31)
                    cursorobj.execute(Retrieve_Record3)
                    Retrieved_Records3=cursorobj.fetchall()
                    for loop4 in Retrieved_Records3:
                        print(loop4)
                    Return()    
                elif Input25=="3":
                    Retrieve_Record4="select * from Radiology_Table where Pending_Fees Is Not null"
                    cursorobj.execute(Retrieve_Record4)
                    Retrieved_Records4=cursorobj.fetchall()
                    for loop5 in Retrieved_Records4:
                        print(loop5)
                    Return()
                else:
                    print("Enter A Valid Numeral")
                    Tables_Menu()
            else:
                print("Enter A Valid Numeral")
                Tables_Menu()
        if Input10=="4":
            print('''Menu:
        (1)To Insert New Record
        (2)To update the Record
        (3)To Fetch Information''')                  
            Input11=input("Enter The Numeral:")
            if Input11=="1":
                Input2=int(input("How Many Records Are To Be Inserted:"))
                for loop1 in range(1,Input2+1):
                    Display5=print("Enter The Patient_ID",loop1)
                    Input3=int(input(":"))
                    Display6=print("Enter Patient_Name",loop1)
                    Input4=input(":")
                    Display7=print("Enter Last Visit Date",loop1)
                    Input5=input(":")
                    Display8=print("Enter Doctor_ID",loop1)
                    Input6=int(input(":"))
                    Display9=print("Enter Doctor_Name",loop1)
                    Input7=input(":")
                    Dispaly10=print("Enter Fees_Paid",loop1)
                    Input8=int(input(":"))
                    Display11=print("Enter Pending Fees",loop1)
                    Input9=int(input(":"))
                    Insert_Record="Insert into Neurology_Table Values(%s,\"%s\",\"%s\",%s,\"%s\",%s,%s)"%(Input3,Input4,Input5,Input6,Input7,Input8,Input9)
                    cursorobj.execute(Insert_Record)
                    connectionobj.commit()
                print("All Records Are Inserted Successfully")    
                Return()
            elif Input11=="2":
                Input19=int(input("How Many Records You Need To Update:"))
                Display5=print('''Which Column Would You Like To Update
    (1)Patient_Name
    (2)Last Visit Date
    (3)Doctor ID
    (4)Doctor Name
    (5)Fees Paid
    (6)Pending Fees''')
                Input20=input("Enter The Numeral:")
                if Input20=="1":
                  for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Patient_Name:")
                      Update_P_Name="update Neurology_Table set Patient_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                  print("Records Are Updated Successfully")
                  Return()
                elif Input20=="2":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Last_Visit_Date:")
                      Update_P_Name="update Neurology_Table set Last_Visit_On=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="3":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_ID:")
                      Update_P_Name="update Neurology_Table set Doctor_ID=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()

                elif Input20=="4":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_Name:")
                      Update_P_Name="update Neurology_Table set Doctor_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="5":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Fees_Paid:")
                      Update_P_Name="update Neurology_Table set Fees_Paid=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="6":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Pending_Fees:")
                      Update_P_Name="update Neurology_Table set Pending_Fees=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                else:
                    print("Enter A Valid Numeral!!")
                    Tables_Menu()
            elif Input11=="3":
                Display8=print('''(1)Retrieve Records Using Patient_ID
    (2)Retrieve Records using Last Visit Date
    (3)Retrieving Records Who Have Pending Fees''')
                Input25=input("Enter The Numeral:")
                if Input25=="1":
                    print('''(1)Retrieve Records Using Specific Patient_ID
    (2)Retrieve Records Using specific Interval of Patient_ID''')
                    Input26=input("Enter The Numeral:")
                    if Input26=="1":
                        Input27=int(input("How Many Records You Need to Retrieve:"))
                        for loop3 in range(1,Input27+1):
                            Display9=print("Enter Patient_ID",loop3)
                            Input27=input(":")
                            Retrieve_Record1="select * from Neurology_Table where Patient_ID=%s"%(Input27)
                            cursorobj.execute(Retrieve_Record1) 
                            Retrieved_Records1=cursorobj.fetchone()
                            print(Retrieved_Records1)
                        Return()    
                    elif Input26=="2":
                        Input28=input("Enter Starting Patient_ID:")
                        Input29=input("Enter Ending Patient_ID:")
                        Retrieve_Record2="select * from Neurology_Table where Patient_ID Between %s and %s"%(Input28,Input29)
                        cursorobj.execute(Retrieve_Record2)
                        Retrieved_Records2=cursorobj.fetchall()
                        for loop4 in Retrieved_Records2:
                            print(loop4)
                        Return()    
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                elif Input25=="2":
                    Input30=input("Enter From Date:")
                    Input31=input("Enter To Date:")
                    Retrieve_Record3="select * from Neurology_Table Where Last_Visit_On Between \"%s\" And \"%s\""%(Input30,Input31)
                    cursorobj.execute(Retrieve_Record3)
                    Retrieved_Records3=cursorobj.fetchall()
                    for loop4 in Retrieved_Records3:
                        print(loop4)
                    Return()    
                elif Input25=="3":
                    Retrieve_Record4="select * from Neurology_Table where Pending_Fees Is Not null"
                    cursorobj.execute(Retrieve_Record4)
                    Retrieved_Records4=cursorobj.fetchall()
                    for loop5 in Retrieved_Records4:
                        print(loop5)
                    Return()
                else:
                    print("Enter A Valid Numeral")
                    Tables_Menu()
            else:
                print("Enter A Valid Numeral")
                Tables_Menu()
        if Input10=="5":
            print('''Menu:
        (1)To Insert New Record
        (2)To update the Record
        (3)To Fetch Information''')
            Input11=input("Enter The Numeral:")
            if Input11=="1":
                Input2=int(input("How Many Records Are To Be Inserted:"))
                for loop1 in range(1,Input2+1):
                    Display5=print("Enter The Patient_ID",loop1)
                    Input3=int(input(":"))
                    Display6=print("Enter Patient_Name",loop1)
                    Input4=input(":")
                    Display7=print("Enter Last Visit Date",loop1)
                    Input5=input(":")
                    Display8=print("Enter Doctor_ID",loop1)
                    Input6=int(input(":"))
                    Display9=print("Enter Doctor_Name",loop1)
                    Input7=input(":")
                    Dispaly10=print("Enter Fees_Paid",loop1)
                    Input8=int(input(":"))
                    Display11=print("Enter Pending Fees",loop1)
                    Input9=int(input(":"))
                    Insert_Record="Insert into Pediatrics_Table Values(%s,\"%s\",\"%s\",%s,\"%s\",%s,%s)"%(Input3,Input4,Input5,Input6,Input7,Input8,Input9)
                    cursorobj.execute(Insert_Record)
                    connectionobj.commit()
                print("All Records Are Inserted Successfully")    
                Return()
            elif Input11=="2":
                Input19=int(input("How Many Records You Need To Update:"))
                Display5=print('''Which Column Would You Like To Update
    (1)Patient_Name
    (2)Last Visit Date
    (3)Doctor ID
    (4)Doctor Name
    (5)Fees Paid
    (6)Pending Fees''')
                Input20=input("Enter The Numeral:")
                if Input20=="1":
                  for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Patient_Name:")
                      Update_P_Name="update Pediatrics_Table set Patient_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                  print("Records Are Updated Successfully")
                  Return()
                elif Input20=="2":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Last_Visit_Date:")
                      Update_P_Name="update Pediatrics_Table set Last_Visit_On=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="3":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_ID:")
                      Update_P_Name="update Pediatrics_Table set Doctor_ID=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()

                elif Input20=="4":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_Name:")
                      Update_P_Name="update Pediatrics_Table set Doctor_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="5":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Fees_Paid:")
                      Update_P_Name="update Pediatrics_Table set Fees_Paid=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="6":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Pending_Fees:")
                      Update_P_Name="update Pediatrics_Table set Pending_Fees=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                else:
                    print("Enter A Valid Numeral!!")
                    Tables_Menu()
            elif Input11=="3":
                Display8=print('''(1)Retrieve Records Using Patient_ID
    (2)Retrieve Records using Last Visit Date
    (3)Retrieving Records Who Have Pending Fees''')
                Input25=input("Enter The Numeral:")
                if Input25=="1":
                    print('''(1)Retrieve Records Using Specific Patient_ID
    (2)Retrieve Records Using specific Interval of Patient_ID''')
                    Input26=input("Enter The Numeral:")
                    if Input26=="1":
                        Input27=int(input("How Many Records You Need to Retrieve:"))
                        for loop3 in range(1,Input27+1):
                            Display9=print("Enter Patient_ID",loop3)
                            Input27=input(":")
                            Retrieve_Record1="select * from Pediatrics_Table where Patient_ID=%s"%(Input27)
                            cursorobj.execute(Retrieve_Record1) 
                            Retrieved_Records1=cursorobj.fetchone()
                            print(Retrieved_Records1)
                        Return()    
                    elif Input26=="2":
                        Input28=input("Enter Starting Patient_ID:")
                        Input29=input("Enter Ending Patient_ID:")
                        Retrieve_Record2="select * from Pediatrics_Table where Patient_ID Between %s and %s"%(Input28,Input29)
                        cursorobj.execute(Retrieve_Record2)
                        Retrieved_Records2=cursorobj.fetchall()
                        for loop4 in Retrieved_Records2:
                            print(loop4)
                        Return()    
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                elif Input25=="2":
                    Input30=input("Enter From Date:")
                    Input31=input("Enter To Date:")
                    Retrieve_Record3="select * from Pediatrics_Table Where Last_Visit_On Between \"%s\" And \"%s\""%(Input30,Input31)
                    cursorobj.execute(Retrieve_Record3)
                    Retrieved_Records3=cursorobj.fetchall()
                    for loop4 in Retrieved_Records3:
                        print(loop4)
                    Return()    
                elif Input25=="3":
                    Retrieve_Record4="select * from Pediatrics_Table where Pending_Fees Is Not null"
                    cursorobj.execute(Retrieve_Record4)
                    Retrieved_Records4=cursorobj.fetchall()
                    for loop5 in Retrieved_Records4:
                        print(loop5)
                    Return()
                else:
                    print("Enter A Valid Numeral")
                    Tables_Menu()
            else:
                print("Enter A Valid Numeral")
                Tables_Menu()
        if Input10=="6":
            print('''Menu:
        (1)To Insert New Record
        (2)To update the Record
        (3)To Fetch Information''')
            Input11=input("Enter The Numeral:")
            if Input11=="1":
                Input2=int(input("How Many Records Are To Be Inserted:"))
                for loop1 in range(1,Input2+1):
                    Display5=print("Enter The Patient_ID",loop1)
                    Input3=int(input(":"))
                    Display6=print("Enter Patient_Name",loop1)
                    Input4=input(":")
                    Display7=print("Enter Last Visit Date",loop1)
                    Input5=input(":")
                    Display8=print("Enter Doctor_ID",loop1)
                    Input6=int(input(":"))
                    Display9=print("Enter Doctor_Name",loop1)
                    Input7=input(":")
                    Dispaly10=print("Enter Fees_Paid",loop1)
                    Input8=int(input(":"))
                    Display11=print("Enter Pending Fees",loop1)
                    Input9=int(input(":"))
                    Insert_Record="Insert into Psychiatry_Table Values(%s,\"%s\",\"%s\",%s,\"%s\",%s,%s)"%(Input3,Input4,Input5,Input6,Input7,Input8,Input9)
                    cursorobj.execute(Insert_Record)
                    connectionobj.commit()
                print("All Records Are Inserted Successfully")    
                Return()
            elif Input11=="2":
                Input19=int(input("How Many Records You Need To Update:"))
                Display5=print('''Which Column Would You Like To Update
    (1)Patient_Name
    (2)Last Visit Date
    (3)Doctor ID
    (4)Doctor Name
    (5)Fees Paid
    (6)Pending Fees''')
                Input20=input("Enter The Numeral:")
                if Input20=="1":
                  for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Patient_Name:")
                      Update_P_Name="update Psychiatry_Table set Patient_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                  print("Records Are Updated Successfully")
                  Return()
                elif Input20=="2":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Last_Visit_Date:")
                      Update_P_Name="update Psychiatry_Table set Last_Visit_On=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="3":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_ID:")
                      Update_P_Name="update Psychiatry_Table set Doctor_ID=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()

                elif Input20=="4":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_Name:")
                      Update_P_Name="update Psychiatry_Table set Doctor_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="5":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Fees_Paid:")
                      Update_P_Name="update Psychiatry_Table set Fees_Paid=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="6":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Total_Pending_Fees:")
                      Update_P_Name="update Psychiatry_Table set Pending_Fees=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                else:
                    print("Enter A Valid Numeral!!")
                    Tables_Menu()
            elif Input11=="3":
                Display8=print('''(1)Retrieve Records Using Patient_ID
    (2)Retrieve Records using Last Visit Date
    (3)Retrieving Records Who Have Pending Fees''')
                Input25=input("Enter The Numeral:")
                if Input25=="1":
                    print('''(1)Retrieve Records Using Specific Patient_ID
    (2)Retrieve Records Using specific Interval of Patient_ID''')
                    Input26=input("Enter The Numeral:")
                    if Input26=="1":
                        Input27=int(input("How Many Records You Need to Retrieve:"))
                        for loop3 in range(1,Input27+1):
                            Display9=print("Enter Patient_ID",loop3)
                            Input27=input(":")
                            Retrieve_Record1="select * from Psychiatry_Table where Patient_ID=%s"%(Input27)
                            cursorobj.execute(Retrieve_Record1) 
                            Retrieved_Records1=cursorobj.fetchone()
                            print(Retrieved_Records1)
                        Return()    
                    elif Input26=="2":
                        Input28=input("Enter Starting Patient_ID:")
                        Input29=input("Enter Ending Patient_ID:")
                        Retrieve_Record2="select * from Psychiatry_Table where Patient_ID Between %s and %s"%(Input28,Input29)
                        cursorobj.execute(Retrieve_Record2)
                        Retrieved_Records2=cursorobj.fetchall()
                        for loop4 in Retrieved_Records2:
                            print(loop4)
                        Return()    
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                elif Input25=="2":
                    Input30=input("Enter From Date:")
                    Input31=input("Enter To Date:")
                    Retrieve_Record3="select * from Psychiatry_Table Where Last_Visit_On Between \"%s\" And \"%s\""%(Input30,Input31)
                    cursorobj.execute(Retrieve_Record3)
                    Retrieved_Records3=cursorobj.fetchall()
                    for loop4 in Retrieved_Records3:
                        print(loop4)
                    Return()    
                elif Input25=="3":
                    Retrieve_Record4="select * from Psychiatry_Table where Pending_Fees Is Not null"
                    cursorobj.execute(Retrieve_Record4)
                    Retrieved_Records4=cursorobj.fetchall()
                    for loop5 in Retrieved_Records4:
                        print(loop5)
                    Return()
                else:
                    print("Enter A Valid Numeral")
                    Tables_Menu()
            else:
                print("Enter A Valid Numeral")
                Tables_Menu()
        if Input10=="7":
            print('''Menu:
        (1)To Insert New Record
        (2)To update the Record
        (3)To Fetch Information''')
            Input11=input("Enter The Numeral:")
            if Input11=="1":
                Input2=int(input("How Many Records Are To Be Inserted:"))
                for loop1 in range(1,Input2+1):
                    Display5=print("Enter The Patient_ID",loop1)
                    Input3=int(input(":"))
                    Display6=print("Enter Patient_Name",loop1)
                    Input4=input(":")
                    Display7=print("Enter Department",loop1)
                    Input5=input(":")
                    Display8=print("Enter Date_Of_Birth",loop1)
                    Input6=input(":")
                    Display9=print("Enter Address",loop1)
                    Input7=input(":")
                    Dispaly10=print("Enter Phone_No",loop1)
                    Input8=int(input(":"))
                    Display11=print("Enter Age",loop1)
                    Input9=int(input(":"))
                    Diaplay12=print("Enter Gender",loop1)
                    Input10=input(":")
                    Insert_Record="Insert into Patients_Table Values(%s,\"%s\",\"%s\",\"%s\",\"%s\",%s,%s,\"%s\")"%(Input3,Input4,Input5,Input6,Input7,Input8,Input9,Input10)
                    cursorobj.execute(Insert_Record)
                    connectionobj.commit()
                print("All Records Are Inserted Successfully")    
                Return()
            elif Input11=="2":
                Input19=int(input("How Many Records You Need To Update:"))
                Display5=print('''Which Column Would You Like To Update
    (1)Patient_Name
    (2)Department
    (3)Date Of Birth
    (4)Address
    (5)Phone_No
    (6)Age
    (7)Gender''')
                Input20=input("Enter The Numeral:")
                if Input20=="1":
                  for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Patient_Name:")
                      Update_P_Name="update Patients_Table set Patient_Name=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                  print("Records Are Updated Successfully")
                  Return()
                elif Input20=="2":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Department:")
                      Update_P_Name="update Patients_Table set Type=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="3":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter Date Of Birth:")
                      Update_P_Name="update Patients_Table set Date_Of_Birth=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()

                elif Input20=="4":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The Address:")
                      Update_P_Name="update Patients_Table set Address=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="5":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Phone_No:")
                      Update_P_Name="update Patients_Table set Phone_No=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="6":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The Age:")
                      Update_P_Name="update Patients_Table set Age=%s where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="7":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Patient_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter Gender:")
                      Update_P_Name="update Patients_Table set Sex=\"%s\" where Patient_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()    
                else:
                    print("Enter A Valid Numeral!!")
                    Tables_Menu()
            elif Input11=="3":
                Display8=print('''(1)Retrieve Records Using Patient_ID
    (2)Retrieve Records using Age Group
    (3)Retrieve Records By Department''')
                Input25=input("Enter The Numeral:")
                if Input25=="1":
                    print('''(1)Retrieve Records Using Specific Patient_ID
    (2)Retrieve Records Using specific Interval of Patient_ID''')
                    Input26=input("Enter The Numeral:")
                    if Input26=="1":
                        Input27=int(input("How Many Records You Need to Retrieve:"))
                        for loop3 in range(1,Input27+1):
                            Display9=print("Enter Patient_ID",loop3)
                            Input27=input(":")
                            Retrieve_Record1="select * from Patients_Table where Patient_ID=%s"%(Input27)
                            cursorobj.execute(Retrieve_Record1) 
                            Retrieved_Records1=cursorobj.fetchone()
                            print(Retrieved_Records1)
                        Return()    
                    elif Input26=="2":
                        Input28=input("Enter Starting Patient_ID:")
                        Input29=input("Enter Ending Patient_ID:")
                        Retrieve_Record2="select * from Patients_Table where Patient_ID Between %s and %s"%(Input28,Input29)
                        cursorobj.execute(Retrieve_Record2)
                        Retrieved_Records2=cursorobj.fetchall()
                        for loop4 in Retrieved_Records2:
                            print(loop4)
                        Return()    
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                elif Input25=="2":
                    Input30=input("Enter From Age:")
                    Input31=input("Enter To Age:")
                    Retrieve_Record3="select * from Patients_Table Where Age Between %s And %s"%(Input30,Input31)
                    cursorobj.execute(Retrieve_Record3)
                    Retrieved_Records3=cursorobj.fetchall()
                    for loop4 in Retrieved_Records3:
                        print(loop4)
                    Return()    
                elif Input25=="3":
                    Input35=input("Enter The Department:")
                    Retrieve_Record4="select * from Patients_Table where Type=\"%s\""%(Input35)
                    cursorobj.execute(Retrieve_Record4)
                    Retrieved_Records4=cursorobj.fetchall()
                    for loop5 in Retrieved_Records4:
                        print(loop5)
                    Return()
                else:
                    print("Enter A Valid Numeral")
                    Tables_Menu()
            else:
                print("Enter A Valid Numeral")
                Tables_Menu()
        if Input10=="8":
            print('''Menu:
        (1)To Insert New Record
        (2)To update the Record
        (3)To Fetch Information''')
            Input11=input("Enter The Numeral:")
            if Input11=="1":
                Input2=int(input("How Many Records Are To Be Inserted:"))
                for loop1 in range(1,Input2+1):
                    Display5=print("Enter The Doctor_ID",loop1)
                    Input3=int(input(":"))
                    Display6=print("Enter Doctor_Name",loop1)
                    Input4=input(":")
                    Display7=print("Enter Department",loop1)
                    Input5=input(":")
                    Display8=print("Enter Available From Date",loop1)
                    Input6=input(":")
                    Display9=print("Enter Available To Date",loop1)
                    Input7=input(":")
                    Display10=print("Enter Available From Time",loop1)
                    Input8=input(":")
                    Dispaly11=print("Enter Avaialable To Time",loop1)
                    Input9=input(":")
                    Display12=print("Enter Fees Per Hour",loop1)
                    Input10=int(input(":"))
                    Display13=print("Enter Gender",loop1)
                    Input11=input(":")
                    Display14=print("Enter Address",loop1)
                    Input12=input(":")
                    Display15=print("Enter Age",loop1)
                    Input13=int(input(":"))
                    Insert_Record="Insert into Doctors_Table Values(%s,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",%s,\"%s\",\"%s\",%s)"%(Input3,Input4,Input5,Input6,Input7,Input8,Input9,Input10,Input11,Input12,Input13)
                    cursorobj.execute(Insert_Record)
                    connectionobj.commit()
                print("All Records Are Inserted Successfully")    
                Return()
            elif Input11=="2":
                Input19=int(input("How Many Records You Need To Update:"))
                Display5=print('''Which Column Would You Like To Update
    (1)Doctor_Name
    (2)Department
    (3)Available From Date
    (4)Avaialable To Date
    (5)Avaialable From Time
    (6)Available To Time
    (7)Fees Per Hour
    (8)Gender
    (9)Address
    (10)Age''')
                Input20=input("Enter The Numeral:")
                if Input20=="1":
                  for loop2 in range(1,Input19+1):
                      Display6=print("Enter Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Doctor_Name:")
                      Update_P_Name="update Doctors_Table set Doctor_Name=\"%s\" where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                  print("Records Are Updated Successfully")
                  Return()
                elif Input20=="2":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter New Department:")
                      Update_P_Name="update Doctors_Table set Type=\"%s\" where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="3":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Avaialable From Date:")
                      Update_P_Name="update Doctors_Table set Avaialable_From_Date=\"%s\" where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="4":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Avaialable To Date:")
                      Update_P_Name="update Doctors_Table set Avaialable_To_Date=\"%s\" where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="5":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Avaialable From Time:")
                      Update_P_Name="update Doctors_Table set Avaialable_From_Time=\"%s\" where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="6":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Available To Time:")
                      Update_P_Name="update Doctors_Table set Available_To_Time=\"%s\" where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="7":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter Fees Per Hour:")
                      Update_P_Name="update Doctors_Table set Fees_Per_Hour=\"%s\" where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="8":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The Gender:")
                      Update_P_Name="update Doctors_Table set Sex=\"%s\" where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="9":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The New Address:")
                      Update_P_Name="update Doctors_Table set Address=\"%s\" where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                elif Input20=="10":
                    for loop2 in range(1,Input19+1):
                      Display6=print("Enter The Doctor_ID",loop2)
                      Input21=input(":")
                      Input22=input("Enter The Age:")
                      Update_P_Name="update Doctors_Table set Age=%s where Doctor_ID=%s"%(Input22,Input21)
                      cursorobj.execute(Update_P_Name)
                      connectionobj.commit()
                    print("Records Are Updated Successfully")
                    Return()
                     
                else:
                    print("Enter A Valid Numeral!!")
                    Tables_Menu()
            elif Input11=="3":
                Display8=print('''(1)Retrieve Records Using Doctor_ID
    (2)Retrieve Records using Avaialability
    (3)Retrieve Records by Department''')
                Input25=input("Enter The Numeral:")
                if Input25=="1":
                    print('''(1)Retrieve Records Using Specific Doctor_ID
    (2)Retrieve Records Using specific Interval of Doctor_ID''')
                    Input26=input("Enter The Numeral:")
                    if Input26=="1":
                        Input27=int(input("How Many Records You Need to Retrieve:"))
                        for loop3 in range(1,Input27+1):
                            Display9=print("Enter Patient_ID",loop3)
                            Input27=input(":")
                            Retrieve_Record1="select * from Doctors_Table where Doctor_ID=%s"%(Input27)
                            cursorobj.execute(Retrieve_Record1) 
                            Retrieved_Records1=cursorobj.fetchone()
                            print(Retrieved_Records1)
                        Return()    
                    elif Input26=="2":
                        Input28=input("Enter Starting Doctor_ID:")
                        Input29=input("Enter Ending Doctor_ID:")
                        Retrieve_Record2="select * from Doctors_Table where Patient_ID Between %s and %s"%(Input28,Input29)
                        cursorobj.execute(Retrieve_Record2)
                        Retrieved_Records2=cursorobj.fetchall()
                        for loop4 in Retrieved_Records2:
                            print(loop4)
                        Return()    
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                elif Input25=="2":
                    print('''(1)Retrieve Records of Doctors Avaialable Now
(2)Retrieve Records Of Doctors By Date
(3)Retrieve Records of Doctors By Time ''')
                    Input30=input("Enter The Numeral:")
                    if Input30=="1":
                        Cur_Date="select curdate()"
                        Date=cursorobj.execute(Cur_Date)
                        Cur_Time="select curtime()"
                        Time=cursorobj.execute(Cur_Time)
                        Retrieve_Record3="select * from Doctors_Table Where \"%s\" Between Avaialable_From_Time And Avaialable_To_Time And \"%s\" Between Avaialable_From_Date And Avaialable_To_Date"%(Time,Date)
                        cursorobj.execute(Retrieve_Record3)
                        Retrieved_Records3=cursorobj.fetchall()
                        for loop4 in Retrieved_Records3:
                            print(loop4)
                        Return()
                    elif Input30=="2":
                        Input45=input("Enter The Date You Want To Check:")
                        Retrieve_Record3="select * from Doctors_Table Where \"%s\" Between Available_From_Date And Available_To_Date"%(Input45)
                        cursorobj.execute(Retrieve_Record3)
                        Retrieved_Records3=cursorobj.fetchall()
                        for loop4 in Retrieved_Records3:
                            print(loop4)
                        Return()
                    elif Input30=="3":
                        Input46=input("Enter The Time You Want To Check:")
                        Retrieve_Record3="select * from Doctors_Table Where \"%s\" Between Available_From_Time And Available_To_Time"%(Input46)
                        cursorobj.execute(Retrieve_Record3)
                        Retrieved_Records3=cursorobj.fetchall()
                        for loop4 in Retrieved_Records3:
                            print(loop4)
                        Return()
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                        
                elif Input25=="3":
                    print('''Which Department Doctors List Do you Want
(1)Ortho Department
(2)Cardiology Department
(3)Radiology Department
(4)Neurology Department
(5)Pediatrics Department
(6)Psychiatry Department''')
                    Input22=input("Enter The Numeral:")
                    if Input22=="1":
                        Retrieve_Record4="select * from Doctors_Table where Type=\"Ortho\""
                        cursorobj.execute(Retrieve_Record4)
                        Retrieved_Records4=cursorobj.fetchall()
                        for loop5 in Retrieved_Records4:
                            print(loop5)
                        Return()
                    elif Input22=="2":
                        Retrieve_Record4="select * from Doctors_Table where Type=\"Cardiology\""
                        cursorobj.execute(Retrieve_Record4)
                        Retrieved_Records4=cursorobj.fetchall()
                        for loop5 in Retrieved_Records4:
                            print(loop5)
                        Return()
                    elif Input22=="3":
                        Retrieve_Record4="select * from Doctors_Table where Type=\"Radiology\""
                        cursorobj.execute(Retrieve_Record4)
                        Retrieved_Records4=cursorobj.fetchall()
                        for loop5 in Retrieved_Records4:
                            print(loop5)
                        Return()
                    elif Input22=="4":
                        Retrieve_Record4="select * from Doctors_Table where Type=\"Neurology\""
                        cursorobj.execute(Retrieve_Record4)
                        Retrieved_Records4=cursorobj.fetchall()
                        for loop5 in Retrieved_Records4:
                            print(loop5)
                        Return()
                    elif Input22=="5":
                        Retrieve_Record4="select * from Doctors_Table where Type=\"Pediatrics\""
                        cursorobj.execute(Retrieve_Record4)
                        Retrieved_Records4=cursorobj.fetchall()
                        for loop5 in Retrieved_Records4:
                            print(loop5)
                        Return()
                    elif Input22=="6":
                        Retrieve_Record4="select * from Doctors_Table where Type=\"Psychiatry\""
                        cursorobj.execute(Retrieve_Record4)
                        Retrieved_Records4=cursorobj.fetchall()
                        for loop5 in Retrieved_Records4:
                            print(loop5)
                        Return()
                    else:
                        print("Enter A Valid Numeral")
                        Tables_Menu()
                else:
                    print("Enter A Valid Numeral")
                    Tables_Menu()
            else:
                print("Enter A Valid Numeral")
                Tables_Menu()
def Return_User():
    print('''(1)Return To Login Page
(2)Return To User Menu''')
    Input60=input("Enter The Numeral:")
    if Input60=="1":
        Login_Page()
        Basic()
    elif Input60=="2":
        User_Menu()
    else:
        print("Enter A Valid Numeral")
        User_Menu()
def User_Menu():
    print("We Provide The Following Facilities")
    print('''(1)Get Information About You, By Using Patient_ID
(2)Check The Availability Of Doctors
(3)Obatain Bill
(4)Give Feedback About The Hospital''')
    Input22=input("Enter The Numeral:")
    if Input22=="1":
        Input34=input("Enter Your Patient_ID:")
        Retrieve_Record4="select * from Patients_Table where Patient_ID=%s"%(Input34)
        cursorobj.execute(Retrieve_Record4)
        Retrieved_Records4=cursorobj.fetchall()
        for loop5 in Retrieved_Records4:
            print(loop5)
        print("Obatained Your Information Successfully")
        Return_User()
    elif Input22=="2":
        Cur_Date="select curdate()"
        Date=cursorobj.execute(Cur_Date)
        Cur_Time="select curtime()"
        Time=cursorobj.execute(Cur_Time)
        Retrieve_Record3="select * from Doctors_Table Where \"%s\" Between Avaialable_From_Time And Avaialable_To_Time And \"%s\" Between Avaialable_From_Date And Avaialable_To_Date"%(Time,Date)
        cursorobj.execute(Retrieve_Record3)
        Retrieved_Records3=cursorobj.fetchall()
        for loop4 in Retrieved_Records3:
            print(loop4)
        print("Obatained The Information Successfully")
        Return_User()
    elif Input22=="3":
        Input34=input("Enter Your Patient_ID:")
        Input35=input("Enter Your Department:")
        Retrieve_Record4="select Patient_ID.Patients_Table,Patient_Name.Patients_Table,Pending_Fees.\"%s\",\"Bill Amount = \",Fees_Paid.\"%s\" as \"Total Fees\" from Patients_Table,\"%s\"_Table where Patient_ID=%s"%(Input35,Input35,Input35,Input34)
        cursorobj.execute(Retrieve_Record4)
        Retrieved_Records4=cursorobj.fetchall()
        for loop5 in Retrieved_Records4:
            print(loop5)
        print("Obatained Your Information Successfully")
        Return_User()
    elif Input22=="4":
        Input45=input("Enter Your Patient_ID:")
        Input46=input("Enter Your Name:")
        Input47=input("Enter Your Feedback:")
        Retrieve_Record4="insert into Feedback_Table values(%s,\"%s\",\"%s\")"%(Input45,Input46,Input47)
        cursorobj.execute(Retrieve_Record4)
        print('''Thank You For Your Feedback
Your Opinion Really Mean To Us
\"THANK YOU FOR CHOOSING DKMRC TECNOLOGY SPECIALIZED HOSPITAL\"''')
        Return_User()
    else:
        print("Enter A Valid Numeral")
        Tables_Menu()
def Basic():
    Input1=input("Enter The Numeral:")
    if Input1=="1":
        print("Welcome Admin")        
        Tables_Menu()
    elif Input1=="2":
        print("welcome User")
        User_Menu()
    else:
        Login_Page()
              
Login_Page()
Basic()

              
              
              
              
            
            
          
            
            
        
      

      
        

