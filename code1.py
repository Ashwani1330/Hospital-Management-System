import time
from sys import exit
import mysql.connector as sql

con = sql.connect(host = "localhost", user = "root", password = "ENG249/94MySQL", database = "Project")  #Open a connection to MySQL Database
if con.is_connected():  #Checks connection
    print("Successfully connected.")
cursor = con.cursor()  #Creates cursor instance

print("""|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|
                         HOSPITAL MANAGEMENT SYSTEM
|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_| \n""")

print("""
         |_-_-_-_-_-_-_________________________________-_-_-_-_-_-_|
         |                   Login/Sign-up Page                    |
         ||_-_-_-_-_-_---------------------------------_-_-_-_-_-_|| 
                     
                     1. Login
                     2. Sign-up as a new user
                     3. Update User-credentials
""")


def signup(): 
    signchoice = input("\nWould you like to sign-up for a new account?...(Yes/No): ")
    if signchoice == "Yes" or signchoice == "YES" or signchoice == "yes":
        print("\n\n\t\tNew User Sign-up\n")
        New_user = input("\nEnter Name: ")
        New_Password = input("\nCreate Password: ")  
        New_Password_confm = input("Confirm your Password: ")  
        while New_Password_confm != New_Password:  #Prompts the user to re-enter correct password when confirmed password and password entered are not the same
            print("\nPlease ReEnter your password again:  ")
            New_Password = input("Create Password: ")
            New_Password_confm = input("Confirm your Password: ")
        u_signup = "INSERT INTO login(User, Password) Values ('{}', '{}')".format(New_user, New_Password)  #Inserts User's username and password in login table of MySQL
        cursor.execute(u_signup)  #Executes the SQL query u_signup
        con.commit()  #Commits the changes to MySQL database
        print("\nSucessfully Registered!🔒")
        return("Welcome!")       
    else:
        print("\n\t\tThanks for visiting!\n")  
        return(exit())  #Exits the system when user don't want to sign in


def login():
    print("\n\t\tExisting User Login")
    count = 0
    User = input("\nEnter Username: ")
    Password = input("\nEnter Password: ")
    cursor.execute("select * from login")  #SQL retrieves all the data of table login
    u_total = cursor.fetchall()  #Fetches all the records in the resultset
    u_list = []
    for row in u_total:  #Processing u_total tuple one row at a time
        u_list.append(row)  #Appends one row in u_list at a time
    for i in u_list:
        if i[0] == User:
            if i[1] == Password:
                print("Welcome!")  #Username & Password found correct 
            elif i[1] != Password:  #Username is correct but Password is incorrect
                print("Wrong Password! Please try again.")
                for j in range(3):     
                    while count <= 3: #Five chances to enter correct password
                        Password = input("Enter Password: ")
                        if i[1] == Password:  
                            return("\nWecome!")  #Exits the fuction login() when password found correct
                        print("Wrong Password! Please try again.")
                        count += 1
                    if j == 2:  #Condition for exiting the system
                        break
                    print("\nYou have entered your password incorrect 5 times. Please wait 60 seconds to enter password again.\n")
                    time.sleep(60)  #Waits the user for 60 seconds before entering password again 
                    count = 0  #Sets count value back to zero
                print("\nYou have entered wrong password multiple times. Try Again later!\n")
                print("\n\t\tThanks for visiting!\n")
                return(exit())  #Exits the system
            break  #Breaks the loop when Username & Password found correct  
    else:  
        print("\nNo user found with this username!")
        return signup()  #Prompts the user to signup() function if the username entered is incorrect or not in the database
        

def cred_check():
    print("\n\t\tUser Old Credentials check")
    count = 0
    u_old = input("\nEnter old username: ")
    passwd_old = input("\nEnter old password: ")
    
    cursor.execute("select * from login")
    u_total = cursor.fetchall()
    u_list = []
    for row in u_total:
        u_list.append(row)
    for i in u_list:
        if i[0] == u_old:
            if i[1] == passwd_old:
                print("Welcome!")  #Username & Password found correct 
            elif i[1] != passwd_old:  #Username is correct but Password is incorrect
                print("Wrong Password! Please try again.")
                for j in range(3):    
                    while count <= 3: #Five chances to enter correct password
                        passwd_old = input("Enter Password: ")
                        if i[1] == passwd_old:  
                            return("Wecome!")  #Exits the fuction login() when password found correct
                        print("Wrong Password! Please try again.")
                        count += 1
                    if j == 2:  #Condition for exiting the system
                        break
                    print("\nYou have entered your password incorrect 5 times. Please wait 60 seconds to enter password again.\n")
                    time.sleep(60)  #Waits the user for 60 seconds before entering password again 
                    count = 0  #Sets count value back to zero
                print("\nYou have entered wrong password multiple times. Try Again later!\n")
                print("\n\t\tThanks for visiting!\n")
                return(exit())  #Exits the system
            break  #Breaks the loop when Username & Password found correct  
    else:  
        print("\nNo user found with this username!")
        return signup()  #Prompts the user to signup() function if the username entered is incorrect or not in the database

def update_credentials(u_old): 
    print("\n\t\tUser Credentials Updater\n")
    u_update = input("\nEnter new Username: ")  
    passwd_update = input("\nEnter new Password: ")  
    passwd_update_cnfm = input("Confirm Password: ")
    while passwd_update_cnfm != passwd_update:  #Prompts the user to re-enter correct password when confirmed password and new password entered are not the same
            print("Please ReEnter your password again:  ")
            passwd_update = input("\nEnter new Password: ")
            passwd_update_cnfm = input("\nConfirm Password: ")
    update_cmd = ("UPDATE login SET User = ('{}'), Password = ('{}') where User = ('{}')".format(u_update, passwd_update, u_old))  #Updates User's username and password in login table of MySQL
    cursor.execute(update_cmd)  #Executes the SQL query update_cmd
    con.commit()  #Commits the changes to MySQL database
    return ("\nSuccessfully Updated!🔐")
    
while True:  
    choose = int(input("Enter your choice: "))
    if choose == 1:
        task = login()
        print(task)
        break
    elif choose == 2:
        task = signup()
        print(task)
        break
    elif choose == 3:
        task = cred_check()
        print(task)
        break
    else:
        print("\nPlease enter your Choice between (1-3)\n")
        continue  #Prompts user back to enter the choice of choice not between (1-3)

print("""
                 ||___________ENTER YOUR CHOICE______________||
                  
                     ____________________________________
                     | 1. Register Patient's details    |
                     | 2. Register Doctor's details     |
                     | 3. Register Worker's details     |
                     |----------------------------------|
                     | 4. Total Patient's details       |
                     | 5. Total Doctor's details        |
                     | 6. Total Worker's details        |
                     |----------------------------------|
                     | 7. Particular Patient's detail   |
                     | 8. Particular Doctor's details   | 
                     | 9. Particular Worker's details   |
                     |----------------------------------|
                     | 10. Update Patient's Status      |                     
                     | 11. Delete Patient's Record      |
                     |----------------------------------|
                     | 12. Feedback                     |
                     | 13. Exit the System              |
                     ------------------------------------""")
            




def patient_register():
    print("\nPATIENT REGISTERATION\n")
    p_name = input("Enter Patient's name: ")
    p_gender = input("Enter Patient's gender: ")
    p_age = int(input("Enter Patient's age: "))
    p_ailment = input("Enter Patient's ailment: ")
    p_phone_no = int(input("Enter Patient's phone number: "))
    p_status = input("Enter your current Status.....(Ill/Well): ")    
    
    p_insert = "INSERT INTO patient(Name, Gender, Age, Ailment, Phone_Number, Current_Status) Values ('{}', '{}', {}, '{}', {}, '{}')".format(p_name, p_gender, p_age, p_ailment, p_phone_no, p_status)  #Inserts patient details in patient table of MySQL
    cursor.execute(p_insert)  #Executes the SQL query p_insert
    con.commit()  #Commits the changes to MySQL databse
    return "\nSucessfully Registered!😃😃😄"

def doctor_register():
    print("\nDOCTOR REGISTERATION\n")
    d_name = input("Enter Doctor's name: ")
    d_gender = input("Enter Doctor's gender: ")
    d_dept = input("Enter Doctor's department: ")
    d_phone_no = int(input("Enter Doctor's phone number: "))
    d_email = input("Enter Doctor's email address: ")
    
    d_insert = "INSERT INTO doctor(Name, Gender, Department, Phone_Number, Email_Address) Values ('{}', '{}', '{}', {}, '{}')".format(d_name, d_gender, d_dept, d_phone_no, d_email)
    cursor.execute(d_insert)
    con.commit()
    return "\nSucessfully Registered!😃😃😄"

def worker_register():
    print("\nWORKER REGISTERATION\n")
    w_name = input("Enter Worker name: ")
    w_gender = input("Enter Worker's gender: ")
    w_age = int(input("Enter Worker's age: "))
    w_worktype = input("Enter type of Work: ")
    w_phone_no = int(input("Enter Worker's phone number: "))

    w_insert = "INSERT INTO worker(Name, Gender, Age, WorkType, Phone_Number) VALUES ('{}', '{}', {}, '{}', '{}')".format(w_name, w_gender, w_age, w_worktype, w_phone_no)
    cursor.execute(w_insert)
    con.commit()
    return "\nSucessfully Registered!😃😃😄"

def patient_total():
    cursor.execute("select * from patient")  #SQL retrieves all the data of table login
    p_total = cursor.fetchall()  #Fetches all the records in the resultset
    print("\nTotal patient details: \n")
    p_list = []  #Creates an empty list
    for row in p_total:  #Processing p_total tuple one row at a time
        p_list.append(row)  #Appends one row in u_list at a time
    for i in p_list:  #Transverse the p_list list one row stored as tuple in p_list at a time
        print(i, end = "\n\n")  #Prints one row at a time
    return ""

def doctor_total():
    cursor.execute("select * from doctor")
    d_total = cursor.fetchall()
    print("\nTotal doctor details: \n")
    d_list = []
    for row in d_total:
        d_list.append(row)
    for i in d_list:
        print(i, end = "\n\n")
    return ""

def worker_total():
    cursor.execute("select * from worker")
    w_total = cursor.fetchall()
    print("\nTotal worker details: \n")
    w_list = []
    for row in w_total:
        w_list.append(row)
    for i in w_list:
        print(i, end = "\n\n")
    return ""

def patient_particular():
    cursor.execute("select * from patient")  #SQL retrieves all the data of table login
    p_total = cursor.fetchall()  #Fetches all the records in the resultset
    p_list = []
    for row in p_total:
        p_list.append(row)
    p_desired = input("Enter the name of the patient whose details you want to view: ")
    p_desired_cmd = "select * from patient where Name = ('{}')".format(p_desired)  #SQL retrieves the data of the desired patient from the table patient
    cursor.execute(p_desired_cmd)  #Executes the query p_desired_cmd
    p_data = cursor.fetchall()  #Fetches the record of the desired patient from the resultset
    for i in p_list:
        if i[1] == p_desired:  #Checks if the desired patient is in the p_list list
            for row in p_data:
                return(row)
    else:
        return("Sorry, patient does not exist.")  #No patient found in the table patient of name p_desired 

def doctor_particular():
    cursor.execute("select * from doctor")
    d_total = cursor.fetchall()
    d_list = []
    for row in d_total:
        d_list.append(row)
    d_desired = input("\nEnter the name of the doctor whose details you want to know: ")
    print()     #empty line
    d_desired_cmd = "select * from doctor where Name = ('{}')".format(d_desired)
    cursor.execute(d_desired_cmd)
    d_data = cursor.fetchall()
    for i in d_list:
        if i[1] == d_desired:
            for row in d_data:
                return(row)
    else:
        return("Sorry, the Doctor does not exist.")
  
def worker_particular():
    cursor.execute("select * from worker")
    w_total = cursor.fetchall()
    w_list = []
    for row in w_total:
        w_list.append(row)
    w_desired = input("Enter the name of the worker whose details you want to know: ")
    w_desired_cmd = "select * from worker where Name = ('{}')".format(w_desired)
    cursor.execute(w_desired_cmd)
    w_data = cursor.fetchall()
    for i in w_list:
        if i[1] == w_desired:
            for row in w_data:
                return(row)
    else:
        return("Sorry, the Worker does not exist.") 

def patient_update():
    p_name = input("\nEnter the name of the patient whose record you want to update: ")
    cursor.execute("select * from patient")
    p_total = cursor.fetchall()
    p_list = []
    for row in p_total:  #Processing p_total tuple one row at a time
        p_list.append(row)   #Appends one row in u_list at a time
    for i in p_list:
        if i[1] == p_name:   #Checks if the desired patient is in the p_list list
            p_ailment = input("\nDo you want to update details about Patient's ailment...(Yes/No): ")  #Asks the user if user wants to update patients's ailment
            if p_ailment == "yes" or p_ailment == "YES" or p_ailment == "Yes":
                p_ailment_new = input("\nEnter patient's current ailment: ")
                p_status = input("\nEnter the patient's current status.....(Ill/Well): ")
                p_cmd = ("UPDATE patient SET Ailment = ('{}'), Current_Status = ('{}') where Name = ('{}')".format(p_ailment_new, p_status, p_name))  #Updates patient's ailment, current status with name p_name in patient table of MySQL
            else:  #If user does not want to update patient's ailment
                p_status = input("\nEnter the patient's current status: ")
                p_cmd = ("UPDATE patient SET Current_Status = ('{}') where Name = ('{}')".format(p_status, p_name))  #Updates patient's current status with name p_name in patient table of MySQL
            cursor.execute(p_cmd)  #Executes the query p_cmd
            con.commit()  #Commits changes to the MySQL database
            return("Succesfully Updated Patient's Current Status!")
    else:
        return("No Patient with this name exists.")  #No patient found in the table patient of name p_name

def patient_delete():
    p_name = input("\nEnter the name of the patient whose record you want to delete: ")
    cursor.execute("select * from patient")
    p_total = cursor.fetchall()
    p_list = []
    for row in p_total:
        p_list.append(row)
    for i in p_list:
        if i[1] == p_name:
            p_cmd = ("DELETE from patient where Name = ('{}')".format(p_name))  #Deletes the patient's record with name p_name in patient table of MySQL
            cursor.execute(p_cmd)  #Executes the query p_cmd
            con.commit()  #Commits the changes to MySQL database
            return("Successfully deleted Patient's Record!")
    else:
        return("No Patient with this name exists. Could not delete any record!")  #No patient found in the table patient of name p_name

def feedback():
    print("\n\t\tFeedack")
    f_name = input("\nEnter your name: ")
    f_rate = int(input("\nPlease rate our system(0-10): "))
    f_feedback = input("\nTell us about you experience: ")
    f_insert = "INSERT into feedback(Name, Rating, Feedback) Values ('{}', {}, '{}')".format(f_name, f_rate, f_feedback)  ##Inserts users name,rating and feedback in feedback table of MySQL  
    cursor.execute(f_insert)  #Executes the quert f_inser
    con.commit()  #Commits the changes to My SQL databasess
    return ("\n\t\tThank You for you Valuable Feedback!")


ans = "Yes"
# Choice picker
while ans =="Yes" or ans == "yes" or ans == "YES":
    Choice = int(input("\nEnter your choice: "))

    if Choice == 1:
        task = patient_register()
        print(task)
    elif Choice == 2:
        task = doctor_register()
        print(task)
    elif Choice == 3:
        task = worker_register()
        print(task)
    elif Choice == 4:
        task = patient_total()    
        print(task)
    elif Choice == 5:
        task = doctor_total()
        print(task)
    elif Choice == 6:
        task = worker_total()
        print(task)
    elif Choice == 7:
        task = patient_particular()
        print(task)
    elif Choice == 8:
        task = doctor_particular()
        print(task)
    elif Choice == 9:
        task = worker_particular()
        print(task)
    elif Choice == 10:
        task = patient_update()
        print(task)
    elif Choice == 11:
        task = patient_delete()
        print(task)
    elif Choice == 12:
        task = feedback()
        print(task)
    elif Choice == 13:
        print("\n\t\tBye! Stay Happy & Healthy 😀\n")
        exit()  #Exits the system
    else:
        print("Please enter your Choice between (1-13)")
        continue  #Prompts user back to enter the choice of choice not between (1-13)
    ans = input("\nWant to get any other information?......(Yes/No): ")
else:
    print("\n\t\tBye! Stay Happy & Healthy 😀\n")    

cursor = con.close()  #Closes the connection with MySQL


