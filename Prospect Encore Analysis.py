import pymysql as db  #Required Database
import os          #os module
conn=db.connect("localhost","root","","showroom") #Building Connection
cur=conn.cursor()


#  #  #   #    #    #    #   <Admin Module>   #   #   #    #  #  # # 



def createuser():    #For create new user showroom
    userid=input("Enter the New userID: ")
    userpass=input("Enter the password: ")
    usertype=input("""Enter the type of user: 
    1)admin or monitor
    Enter the choice: """)
    name=input("Enter the full name of user: ")
    phone=input("Enter the phone no. of user: ")
    email=input("Enter the email of user: ")
    status="activated"
    qry=f"insert into employee values('{userid}','{userpass}','{usertype}','{name}','{phone}','{email}','{status}')"
    cur.execute(qry)
    conn.commit()
def viewusers():
    print("All users are following....")
    qry="select * from employee"
    cur.execute(qry)
    res=cur.fetchall()
    for val in res:
        print([val])
    conn.commit()
def viewprospect():
    print("All prospect are following....")
    qry="select * from prospect"
    cur.execute(qry)
    res=cur.fetchall()
    for val in res:
        print([val],end='\n')
    conn.commit()
def changepassword():
    choice=input("""Enter the choice: 
    1)Self 
    2)Others 
    Enter the input: """)
    if choice=='1':        
        userid=input("Enter the userID: ")
        userpass=input("Enter the old password: ")
        queryy="select * from employee"
        cur.execute(queryy)
        res=cur.fetchall()
        for i in res:
            if i[0]==userid and i[1]==userpass:
                password=input("Enter the new password: ")
                qry=f"update employee set user_pass='{password}' where user_id='{userid}' and user_pass='{userpass}'"
                cur.execute(qry)
                conn.commit()
                print("Password Changed Successfully.")
                if i[0]==userid and i[1]==userpass:
                    break
        else:
            if i[0]!=userid and i[1]!=userpass:
                print("User Id or Password Incorrect")
    elif choice=='2':
        userid=input("Enter the userID: ")
        queryy="select * from employee"
        cur.execute(queryy)
        res=cur.fetchall()
        for i in res:
            if i[0]==userid:
                password=input("Enter the new password: ")
                qry=f"update employee set user_pass='{password}' where user_id='{userid}'"
                cur.execute(qry)
                conn.commit()
                print("Password Changed Successfully.")
                if i[0]==userid:
                    break
        else:
            if i[0]!=userid:
                print("User Id Incorrect")
def searchprospect():
    choice=input("""Enter the choice of searching: 
    1)By ProsID 
    2)By Priority 
     Enter your choice: """)
    if choice=='1':
        pros_id=input("Enter the ID of prospect: ")
        qry=f"select * from prospect where pros_id={pros_id}"
        cur.execute(qry)
        res=cur.fetchall()
        for val in res:
            print([val])
    elif choice=='2':
        priority=input("Enter the priority: ")
        qry=f"select * from prospect where priority='{priority}'"
        cur.execute(qry)
        res=cur.fetchall()
        for val in res:
            print([val])
    conn.commit()
def accountstatus():
    choice=input("""Do you want to activate/deactivate account: 
    1)Activate 
    2)Deactivate 
    Enter Your Choice:  """)
    if choice=='1':
        username=input("Enter the user Id: ")
        userphone=input("Enter the user phone no.: ")
        qry=f"update employee set status='activated' where user_id='{username}' and phone='{userphone}'"
        cur.execute(qry)
        conn.commit()
        print("Account activated successfully.")
    elif choice=='2':
        username=input("Enter the user Id: ")
        userphone=input("Enter the user phone no.: ")
        qry=f"update employee set status='deactivated' where user_id='{username}' and phone='{userphone}'"
        cur.execute(qry)
        conn.commit()
        print("Account deactivated successfully.")
def mainmenuadmin():
    while True:
        os.system('cls')
        choice=input("""Enter the choice: 
        1)Create User 
        2)View All Users
        3)View All Prospect 
        4)Change Password
        5)Search Prospect
        6)Activiate/Deacticate Account
        7)Signout
        Enter the choice:  """)
        if choice=='1':
            createuser()
        elif choice=='2':
            viewusers()
        elif choice=='3':
            viewprospect()
        elif choice=='4':
            changepassword()
        elif choice=='5':
            searchprospect()
        elif choice=='6':
            accountstatus()
        elif choice=='7':
            print("Signout Successfully.")
            exit()
        else:
            print("Enter valid input.")
        os.system('pause')





#  #  #   #    #    #    #   <Monitor Module>   #   #   #    #  #  # #



def addprospect():
    prosid=input("Enter the serial no.: ")
    prosname=input("Enter the prospect name: ")
    prosphone=input("Enter the contact no. of prospect: ")
    prosaddress=input("Enter the address of prospect: ")
    model=input("Enter the interested model of prospect: ")
    color=input("Enter the interested color of prospect: ")
    date=input("Enter the date of visit prospect: ")
    priority=input("Enter the priority of prospect: ")
    qry=f"insert into prospect values('{prosid}','{prosname}',{prosphone},'{prosaddress}','{model}','{color}','{date}','{priority}')"
    cur.execute(qry)
    conn.commit()
    print("Your data saved successfully.")
def viewprospectmonitor():
    print("All prospect are following....")
    qry="select * from prospect"
    cur.execute(qry)
    res=cur.fetchall()
    for val in res:
        print([val],end='\n')
def updateprospect():
    prosname=input("Enter the name of prospect: ")
    prosaddress=input("Enter the address of prospect: ")
    qry="update prospect set "
    choice=input("""Enter the choice: 
    1)Prospect Phone
    2)Interested Model
    3)Interested Color
    4)Priority
    Enter the Input: """)
    if choice=='1':
        val=input("Enter the new phone: ")
        qry+=f"pros_phone='{val}' where pros_name='{prosname}' and pros_address='{prosaddress}'"
    elif choice=='2':
        val=input("Enter the Interested Model: ")
        qry+=f"interested_model='{val}' where pros_name='{prosname}' and pros_address='{prosaddress}'"
    elif choice=='3':
        val=input("Enter the Interested Color: ")
        qry+=f"interested_color='{val}' where pros_name='{prosname}' and pros_address='{prosaddress}'"
    elif choice=='4':
        val=input("Enter the Priority: ")
        qry+=f"priority='{val}' where pros_name='{prosname}' and pros_address='{prosaddress}'"
    
    cur.execute(qry)
    conn.commit()
    print("Updated Successfully....")
def searchprospectmonitor():
    choice=input("""Enter the choice of searching: 
    1)By ProsID 
    2)By Priority 
     Enter your choice: """)
    if choice=='1':
        pros_id=input("Enter the ID of prospect: ")
        qry=f"select * from prospect where pros_id={pros_id}"
        cur.execute(qry)
        res=cur.fetchall()
        for val in res:
            print([val])
    elif choice=='2':
        priority=input("Enter the priority: ")
        qry=f"select * from prospect where priority='{priority}'"
        cur.execute(qry)
        res=cur.fetchall()
        for val in res:
            print([val])
    conn.commit()
def changepasswordmonitor():
    userid=input("Enter the userID: ")
    userpass=input("Enter the old password: ")
    queryy="select * from employee"
    cur.execute(queryy)
    res=cur.fetchall()
    for i in res:
        if i[0]==userid and i[1]==userpass:
            password=input("Enter the new password: ")
            qry=f"update employee set user_pass='{password}' where user_id='{userid}' and user_pass='{userpass}'"
            cur.execute(qry)
            conn.commit()
            print("Password Changed Successfully.")
            if i[0]==userid and i[1]==userpass:
                break
    else:
        if i[0]!=userid and i[1]!=userpass:
            print("User Id or Password Incorrect")
def mainmenumonitor():
    while True:
        os.system('cls')
        choice=input("""Enter the choice: 
        1)Add Prospect
        2)View Prospect
        3)Update Prospect
        4)Search Prospect
        5)Change Password
        6)Signout
        Enter the choice: 
        """)
        if choice=='1':
            addprospect()
        elif choice=='2':
            viewprospectmonitor()
        elif choice=='3':
            updateprospect()
        elif choice=='4':
            searchprospectmonitor()
        elif choice=='5':
            changepasswordmonitor()
        elif choice=='6':
            print("Signout Successfully.")
            exit()
        os.system('pause')




#  #  #   #    #    #    #   <Authentication Module>   #   #   #    #  #  # #




def login():
    def admin():
        userid=input("Enter the user Id: ")
        userpass=input("Enter the user password: ")
        qry='select * from employee'
        cur.execute(qry)
        res=cur.fetchall()
        for val in res:
            if val[0]==userid and val[1]==userpass:
                if val[2]=='admin':
                    if val[-1]=='activated':
                        mainmenuadmin()
                        break
                    else:
                        print("Account deactivated.")
                        break
        else:
            if val[0]!=userid and val[1]!=userpass:
                print("User Id or password incorrect.")
    def monitor():
        userid=input("Enter the user Id: ")
        userpass=input("Enter the user password: ")
        qry='select * from employee'
        cur.execute(qry)
        res=cur.fetchall()
        for val in res:
            if val[0]==userid and val[1]==userpass:
                if val[2]=='monitor':
                    if val[-1]=='activated':
                        mainmenumonitor()
                        break
                    else:
                        print("Account deactivated.")
                        break
        else:
            if val[0]!=userid and val[1]!=userpass:
                print("User Id or password incorrect.")
    while True:
        os.system('cls')
        choice=input("""Enter the choice:
    1)Admin
    2)Monitor
    Enter the input: """)
        if choice=='1':
            admin()
        elif choice=='2':
            monitor()
        else:
            print("Enter valid input.")
        os.system('pause')
login()

cur.close()
conn.close()