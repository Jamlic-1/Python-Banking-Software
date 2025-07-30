import sqlite3
#from About_us_page import about_us_page
#from administrative import *
#from CommonFunctions import *
#import bcrypt
#from Maindatabase import *
#from LOGINPAGE import*
#from CREATEACCOUNT import*




# ─────ABOUT US PAGE───────────────────────────────────────────────────────────────────────
def about_us_page():
  print("\nABOUT PAMOJA GROUP BANK\n")

  aboutus = """
  Pamoja Group Bank - A Beacon of Financial Excellence

  Welcome to Pamoja Group Bank, where we transcend traditional banking to focus on your financial well-being and community-centric values. Our dedication to innovation in banking solutions empowers you to navigate your financial journey with confidence and ease.

  Key Highlights:
  - Cutting-edge technology for seamless banking experiences.
  - Strong commitment to trust, transparency, and community development.
  - Diverse range of personalized financial solutions and dynamic 
    investment opportunities.
  Our Motto:
  - "Unity Meets Prosperity" - Our commitment to fostering a sense of 
     unity in every transaction

  Our Mission:
  - We are committed to ensuring our customers have a seamless banking 
    experience.

  Our Journey:
  - We are a leading bank in providing innovative banking solutions in 
    Kenya since 2010.
  - We are dedicated to community development, fostering a sense of unity 
    in every transaction.

  Community and Customer Focus:
  - Actively contributing to societal progress and shared success.
  - Consistently recognized for our community services and customer care.

  Explore our Services:
  - Tailored account management.
  - Investment opportunities tailored to your needs.
  - Dynamic financial solutions for your financial goals.

  Our Team:
  - We are a team of experienced professionals with a passion for banking.
  - Our team members are dedicated to delivering exceptional service and 
    support.

  Our Values:
  - Trust: We believe in the power of trust in the banking industry.
  - Integrity: We strive for honesty and integrity in all our transactions.
  - Community: We embrace a community of like-minded individuals.

  Our Commitment:
  - We are committed to providing you with a seamless banking experience.

  Why Choose Us:
  - We're not just a bank; we're your dedicated financial partner.
  - Award-winning services recognized globally.

  Stay Connected:
  - Follow us on social media for the latest updates and insights.
  - For any inquiries or assistance, please contact us at:
      - Email: plsgq@example.com
      - Phone: +254 706 555 555
  - Visit our website: www.pamojagroupbank.com
  - Address: Pamoja Group Bank, 123 Main Street, Kenya

  Join us on this empowering journey where unity meets prosperity. 
  Experience financial excellence with Pamoja Group Bank.

  We look forward to welcoming you to our community of satisfied customers!

    Feedback and suggestions coming soon!
  """

  print(aboutus)
#====================================================================================================================
#adminisrative
import sqlite3
#from CommonFunctions import*
import random


def connect_db():
    conn = sqlite3.connect('bank_main_database.db')
    cursor = conn.cursor()
    return conn, cursor

def create_user_account():
         conn = sqlite3.connect('bank_main_database.db')
         cursor = conn.cursor()
         try:
             print("Creating a new user account")
             # Gathering user information with input validation
             name = input("Enter the user's full name: ").strip()
             phone = input("Enter the user's phone number: ").strip()
             id_number = input("Enter the user's ID number: ").strip()
             account_number = random.randint(10000000, 99999999)
             initial_balance = 0
             account_opening_date = get_time()
             # Optional: Check if account number already exists
             cursor.execute("SELECT * FROM users WHERE account_number = ?", (account_number,))
             if cursor.fetchone():
                 print(f"Account number {account_number} already exists. Please use a different account number.")
                 return
             # Hash the user's password for security
             hashed_password = hash_password()  # Assuming hash_password is a function that hashes the password
             # Insert the new user data into the database
             cursor.execute('''
                 INSERT INTO users (name, phone, id_number, account_number, balance, hashed_password,account_opening_date, last_login)
                 VALUES (?, ?, ?, ?, ?, ?,?,?)
             ''', (name, phone, id_number, account_number, initial_balance, hashed_password, account_opening_date, None))
             conn.commit()
             print(f"User account for {name} created successfully with account number {account_number}.")
         except sqlite3.Error as e:
             print(f"SQLite error: {e}")
             conn.rollback()
         finally:
             if conn:
                 conn.close()


def view_user_account():
         account_number = input("Enter account number: ")
         conn = sqlite3.connect('bank_main_database.db')
         cursor = conn.cursor()
         try:
             cursor.execute("SELECT * FROM users WHERE account_number = ?", (account_number,))
             user = cursor.fetchone()
             if user:
                 print("User Details:", user)
             else:
                 print("User account not found.")
         except sqlite3.Error as e:
             print(f"SQLite error: {e}")
         finally:
             conn.close()



def modify_user_account():
      account_number = input("Enter account number: ")
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          new_phone = input("Enter new phone number: ")
          new_name = input("Enter new name: ")
          cursor.execute("UPDATE users SET phone = ?, name = ? WHERE account_number = ?", (new_phone, new_name, account_number))
          conn.commit()
          print("User account updated successfully.")
      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          conn.close()

def search_customer_account():
      account_number = input("Enter account number: ")
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          cursor.execute("SELECT * FROM users WHERE account_number = ?", (account_number,))
          user = cursor.fetchone()
          if user:
              print("User Details:", user)
          else:
              print("User account not found.")
      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          conn.close()

def view_transactions_on_account():
      account_number = input("Enter account number: ")
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          cursor.execute("SELECT * FROM transactions WHERE account_number = ?", (account_number,))
          transactions = cursor.fetchall()
          if transactions:
              print("Transactions:")
              for transaction in transactions:
                  print(transaction)
          else:
              print("No transactions found for this account.")

      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          conn.close()



def delete_user_account():
      account_number = input("Enter account number: ")
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          cursor.execute("DELETE FROM users WHERE account_number = ?", (account_number,))
          conn.commit()
          print("User account deleted successfully.")
      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          conn.close()

def freeze_user_account():
      account_number = input("Enter account number: ")
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          cursor.execute("UPDATE users SET frozen = 1 WHERE account_number = ?", (account_number,))
          conn.commit()
          print("User account frozen successfully.")
      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          conn.close()

def unfreeze_user_account():
      account_number = input("Enter account number: ")
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          cursor.execute("UPDATE users SET frozen = 0 WHERE account_number = ?", (account_number,))
          conn.commit()
          print("User account unfrozen successfully.")
      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          conn.close()

def view_freezed_user_account():
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          cursor.execute("SELECT * FROM users WHERE frozen = 1")
          freezed_users = cursor.fetchall()
          if freezed_users:
              print("Freezed Users:")
              for user in freezed_users:
                  print(user)
          else:
              print("No freezed users found.")
      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          conn.close()



def view_top_20_customers():
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          cursor.execute("SELECT * FROM users ORDER BY balance DESC LIMIT 20")
          top_customers = cursor.fetchall()
          for customer in top_customers:
              print(customer)
      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
        conn.close()



#VIEW CUSTOMERS WITH HIGHEST LOAN BALANCES
def view_top_20_loan_customers():
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          cursor.execute("SELECT * FROM users ORDER BY loan_balance DESC LIMIT 20")
          top_loan_customers = cursor.fetchall()
          for customer in top_loan_customers:
              print(customer)
      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          conn.close()



def view_all_loans():
            conn = sqlite3.connect('bank_main_database.db')
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM users WHERE loan_balance > 0")
                loans = cursor.fetchall()
                for loan in loans:
                    print(loan)
            except sqlite3.Error as e:
                print(f"SQLite error: {e}")
            finally:
                conn.close()


def view_all_user_accounts():
             conn = sqlite3.connect('bank_main_database.db')
             cursor = conn.cursor()
             try:
                 cursor.execute("SELECT * FROM users")
                 users = cursor.fetchall()
                 for user in users:
                     print(user)
             except sqlite3.Error as e:
                 print(f"SQLite error: {e}")
             finally:
                 conn.close()


def view_all_loansaccounts():
            conn = sqlite3.connect('bank_main_database.db')
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM users WHERE loan_balance > 0")
                loans = cursor.fetchall()
                for loan in loans:
                    print(loan)
            except sqlite3.Error as e:
                print(f"SQLite error: {e}")
            finally:
                conn.close()


def view_total_amount_in_bank():
       conn = sqlite3.connect('bank_main_database.db')
       cursor = conn.cursor()
       try:
           cursor.execute("SELECT SUM(balance) FROM users")
           total_amount = cursor.fetchone()[0]
           print(f"Total amount in bank: {total_amount}")
       except sqlite3.Error as e:
           print(f"SQLite error: {e}")
       finally:
           conn.close()

def view_total_unpaid_loans():
       conn = sqlite3.connect('bank_main_database.db')
       cursor = conn.cursor()
       try:
           # Calculate the total of unpaid loans
           cursor.execute("SELECT SUM(loan_balance) FROM users WHERE loan_balance > 0")
           total_unpaid_loans = cursor.fetchone()[0]
           if total_unpaid_loans:
               print(f"Total amount of unpaid loans: {total_unpaid_loans}")
           else:
               print("There are no unpaid loans.")
       except sqlite3.Error as e:
           print(f"SQLite error: {e}")
       finally:
           conn.close()
#==============================================================================================================
#common functions
from datetime import datetime
#mport pytz
#import bcrypt
import getpass
import time
#from Validateinput import is_valid_password
#FUNCTION TO HASH USER ACCOUNT PASSWORD USING BCRYPT 

#FUNCTION TO GET EXACT TIME
import time
def get_time():
    # Get current UTC time as a struct_time
    utc_time = time.gmtime()
  
    # Manually adjust for Nairobi's UTC+3 timezone
    nairobi_timestamp = time.mktime(utc_time) + 3 * 3600  # 3 hours * 3600 seconds
    nairobi_time = time.localtime(nairobi_timestamp)

    return time.strftime(" %Y-%m-%d   %H:%M:%S", nairobi_time)

def log_out():
  print("You have successfully logged out at: ",get_time())
  exit()



#import pytz 
import time

def greeting() -> str:
    """
    Determine current time in Nairobi (UTC+3) and choose an appropriate greeting.
    """
    utc_time = time.gmtime()

    # Adjust for Nairobi timezone (UTC+3)
    nairobi_timestamp = time.mktime(utc_time) + 3 * 3600
    nairobi_time = time.localtime(nairobi_timestamp)

    # Extract hour from adjusted time
    hours = nairobi_time.tm_hour

    # Choose greeting based on hour
    if 2 <= hours < 12:
        return "GOOD MORNING!!!"
    elif 12 <= hours < 18:
        return "GOOD AFTERNOON!!!"
    elif 18 <= hours < 22:
        return "GOOD EVENING!!!"
    else:
        return "HELLO!!!"


def proceed_next() -> None:
  _ = input("Press anything if you want to proceed to the next")

import os
import time


def clean_terminal_screen():
    """
    Cleans the terminal screen by performing a system
    clear command. Cls on windows and Clear on UNIX ones.
    """

    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(0.2)

def display_horizontal_line():
    """
    A pretty decorative horizontal line.
    """

    print("───────────────────────────────────────────────────────────────")

#======================================================================================================================================    
# Main database
import sqlite3

conn = sqlite3.connect('bank_main_database.db')
cursor = conn.cursor()

try:
           cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone TEXT NOT NULL,
                   id_number TEXT NOT NULL,
                   account_number TEXT NOT NULL UNIQUE,
                   balance REAL DEFAULT 0,
                   loan_balance REAL DEFAULT 0,
                   hashed_password TEXT NOT NULL,
                   account_opening_date DATETIME NOT NULL,
                   last_login TEXT,  -- Changed to TEXT
                   address TEXT NULL,
                   frozen INTEGER DEFAULT 0

               );
           ''')

           cursor.execute('''
               CREATE TABLE IF NOT EXISTS transactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   transaction_type TEXT NOT NULL,
                   transaction_amount REAL NOT NULL,
                   transaction_time TIMESTAMP NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users (id)
               );
           ''')

           cursor.execute('''
               CREATE TABLE IF NOT EXISTS logins (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   login_time DATETIME NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users (id)
               );
           ''')

           cursor.execute('''
               CREATE TABLE IF NOT EXISTS user_accounts(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name1 TEXT,
                   name2 TEXT,
                   name3 TEXT,
                   id_number TEXT,
                   phone TEXT,
                   account_number TEXT,
                   balance INTEGER,
                   loan_balance INTEGER,
                   email TEXT,
                   transactions TEXT,
                   logins TEXT,
                   role TEXT  -- Added the comma
               );
           ''')

           cursor.execute('''
               CREATE TABLE IF NOT EXISTS admin_details(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name1 TEXT,
                   name2 TEXT,
                   name3 TEXT,
                   id_number TEXT,
                   phone TEXT,
                   work_id_number TEXT,
                   password TEXT,
                   salt TEXT,
                   timestamp TEXT  -- Changed to TEXT
               );
           ''')

           cursor.execute('''
               CREATE TABLE IF NOT EXISTS admin_login_history(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   admin_id INTEGER,
                   admin_name TEXT,
                   login_time TEXT,
                   logout_time TEXT,
                   session_duration INTEGER,
                   FOREIGN KEY(admin_id) REFERENCES admin_details(id)
               );
           ''')

           cursor.execute('''
               CREATE TABLE IF NOT EXISTS failed_login_attempts(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   id_number TEXT,
                   work_id_number TEXT,
                   reason TEXT,
                   attempt_time DATETIME
               );
           ''')

           cursor.execute('''
               CREATE TABLE IF NOT EXISTS staff (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name1 TEXT,
                   name2 TEXT,
                   name3 TEXT,
                   phone TEXT,
                   id_number INTEGER,
                   work_id_number INTEGER,
                   email TEXT,
                   address TEXT,
                   password TEXT,
                   salt TEXT,
                   is_suspended INTEGER DEFAULT 0,
                   role TEXT
               );
           ''')

           cursor.execute('''
               CREATE TABLE IF NOT EXISTS staff_login_history (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   staff_id INTEGER,
                   login_time TEXT,
                   logout_time TEXT
               );
           ''')

           cursor.execute('''
               CREATE TABLE IF NOT EXISTS staff_login_attempts (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   staff_id INTEGER REFERENCES staff(id) ON DELETE CASCADE,
                   username TEXT,
                   role TEXT,
                   reason TEXT,
                   time_attempted TEXT
               );
           ''')

           # Commit the changes
           conn.commit()

except sqlite3.Error as e:
           print(f"SQLite error: {e}")

#finally:
           # Close the connection
          #if conn:
              # conn.close()

#=================================================================================================================
#LOGIN PAGE
import sqlite3
#import bcrypt
#from Validateinput import *
import getpass
#from CommonFunctions import *

conn = sqlite3.connect('bank_main_database.db')
cursor = conn.cursor()

#############################################################################################################################################
#############################################################################################################################################
##                                              USER
#############################################################################################################################################
##################3
def log_in_to_user_account():
      print("\nLOG INTO YOUR ACCOUNT")
      account_number = input("ENTER YOUR ACCOUNT NUMBER: ")
      password = input("ENTER YOUR PASSWORD: ")
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      try:
          # Retrieve user information from the database
          cursor.execute('''
              SELECT u.id, u.name, u.account_number, u.hashed_password, u.salt, u.frozen
              FROM users u
              WHERE u.account_number = ?;
          ''', (account_number,))
          user = cursor.fetchone()
          if user is not None:
              user_id, user_name, _, stored_hashed_password, salt, frozen_status = user
              # Check if the user account is frozen
              if frozen_status == 1:
                  print("YOUR ACCOUNT IS FROZEN. PLEASE CONTACT CUSTOMER SUPPORT.")
                  return
              # Hash the entered password using the stored salt and compare with the stored hashed password
              hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8')).decode('utf-8')
              if stored_hashed_password == hashed_password:
                  # Passwords match
                  print(f"\nSUCCESSFUL LOG IN AT: {get_time()}\nWELCOME TO PAMOJA GROUP BANK")
                  # Update last login time
                  cursor.execute('''
                      UPDATE users
                      SET last_login = ?
                      WHERE account_number = ?;
                  ''', (get_time(), account_number))
                  conn.commit()
                  # Call your main menu or any other relevant function here
                  main_menu(user_id, user_name)  # Pass the user_id and user_name
              else:
                  print("INVALID ACCOUNT NUMBER OR PASSWORD. PLEASE TRY AGAIN.")
          else:
              print("INVALID ACCOUNT NUMBER OR PASSWORD. PLEASE TRY AGAIN.")
      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          # Close the connection
          if conn:
              conn.close()



#############################################################################################################################################
#############################################################################################################################################
##                                         ADMIN
#############################################################################################################################################
##################3
def admin_login():
     print("FOR ADMIN LOGINS ONLY")
     id_number = input("ENTER YOUR 8-DIGIT ID NUMBER: ")
     work_id_number = input("ENTER YOUR 10-DIGIT WORK ID NUMBER: ")
     try:
         cursor.execute(
             '''
             SELECT id, name1, name2, name3, password, salt FROM admin_details WHERE id_number = ? AND work_id_number = ?
             ''', (id_number, work_id_number))
         admin_data = cursor.fetchone()
         if admin_data:
             admin_id, name1, name2, name3, stored_hashed_password, salt = admin_data
             # Get the password and hash it using the stored salt
             password = getpass.getpass("ENTER YOUR PASSWORD: ")
             is_valid_password(password)
             hashed_password = password
             if stored_hashed_password == hashed_password:
                 print(
                     f"Admin '{name1} {name2} {name3}' logged in successfully at {get_time()}"
                 )
                 # Record the admin login
                 record_admin_login(admin_id)
                 return admin_id
             else:
                 print("INVALID PASSWORD. LOGIN FAILED.")
                 record_admin_failed_login_attempt(id_number, work_id_number, 'Invalid password')
         else:
             print("ACCOUNT NOT FOUND OR INVALID ID/WORK ID\n PLEASE TRY AGAIN!.")
             record_admin_failed_login_attempt(id_number, work_id_number, 'Invalid login credentials!')
     except Exception as e:
         print(f"An error occurred during login: {e}")
         record_admin_failed_login_attempt(id_number, work_id_number, 'Login error')


# ─────RECORD ADMIN LOGIN───────────────────────────────────────
def record_admin_login( admin_id):
    current_time = get_time()
    try:
      cursor.execute(
          '''
                   INSERT INTO admin_login_history (admin_id, login_time) VALUES (?, ?)
               ''', (admin_id, current_time))
      conn.commit()
    except sqlite3.Error as e:
      print(f"An error occurred while recording the admin login: {e}")


# ─────ADMIN LOG OUT TIME───────────────────────────────
def record_admin_logout( admin_id):
    current_time = get_time(
    )  # Ensure this returns the current time in the correct format
    try:
      # Find the ID of the most recent login record for this admin
      cursor.execute(
          '''
               SELECT id FROM admin_login_history
               WHERE admin_id = ? AND logout_time IS NULL
               ORDER BY login_time DESC
               LIMIT 1
               ''', (admin_id, ))
      login_record_id = cursor.fetchone()
      if login_record_id:
        # Update the logout time for the found record
        cursor.execute(
            '''
                   UPDATE admin_login_history
                   SET logout_time = ?
                   WHERE id = ?
                   ''', (current_time, login_record_id[0]))
        conn.commit()
      else:
        print("No active login session found for the admin.")
    except sqlite3.Error as e:
      print(f"An error occurred while recording the admin logout: {e}")


# ───── ADMIN LOGIN HISTORY───────────────────────────────────────
def record_admin_failed_login_attempt( id_number, work_id_number, reason):
    try:
      current_time = get_time()
      cursor.execute(
          '''
                    INSERT INTO failed_login_attempts (id_number, work_id_number, reason, attempt_time)
                    VALUES (?, ?, ?, ?)
                ''', (id_number, work_id_number, reason, current_time))
      conn.commit()
      print("Failed login attempt recorded.")
    except Exception as e:
      print(f"An error occurred while recording the failed login attempt: {e}")



#############################################################################################################################################
#############################################################################################################################################
##STAFF
#############################################################################################################################################
##################3
def staff_login(cursor):
      username = input("Enter your username: ")
      id_number = int(input("Enter your ID number: "))
      password = input("Enter your password: ")

      cursor.execute(
          '''
          SELECT id, password, salt, is_suspended FROM staff WHERE id_number = ? 
          ''', (id_number,))
      staff_data = cursor.fetchone()

      if staff_data:
          staff_id, stored_hashed_password, salt, is_suspended = staff_data

          if is_suspended:
              print("ACCOUNT IS SUSPENDED. PLEASE CONTACT ADMIN.")
              return

          # Get the password and hash it using the stored salt
          hashed_password = password

          if stored_hashed_password == hashed_password:
              print(f"Staff '{username}' logged in successfully at {get_time()}")
              record_staff_login(staff_id)
              staff_tasks_on_user_accounts(staff_id)
          else:
              print("INVALID PASSWORD. LOGIN FAILED.")
              record_staff_failed_login_attempt(
                  staff_id=staff_id, username=username, role='staff', reason='Invalid password')
      else:
          print("STAFF ACCOUNT NOT FOUND.\nPLEASE TRY AGAIN.")
          record_staff_failed_login_attempt(
              staff_id=None, username=username, role='staff', reason='Account not found')


def record_staff_failed_login_attempt(staff_id, username, role, reason):
  current_time = get_time()
  try:
      cursor.execute(
          '''
          INSERT INTO staff_login_attempts (staff_id, username, role, reason, time_attempted) VALUES (?, ?, ?, ?, ?)
          ''', (staff_id, username, role, reason, current_time))
      conn.commit()
      print(f"Staff login attempt recorded at {current_time}")
  except sqlite3.Error as e:
      print(f"An error occurred while recording staff login attempt: {e}")


def record_staff_login(staff_id):
  current_time = get_time()
  try:
      cursor.execute(
          '''
          INSERT INTO staff_login_history (staff_id, login_time) VALUES (?, ?)
          ''', (staff_id, current_time))
      conn.commit()
  except sqlite3.Error as e:
      print(f"Error recording staff login: {e}")


def record_staff_logout(staff_id):
      current_time = get_time()
      try:
          # Find the ID of the most recent login record for this staff member
          cursor.execute(
              '''
              SELECT id FROM staff_login_history
              WHERE staff_id = ? AND logout_time IS NULL
              ORDER BY login_time DESC
              LIMIT 1
              ''', (staff_id,))
          login_record_id = cursor.fetchone()

          if login_record_id:
              # Update the logout time for the found record
              cursor.execute(
                  '''
                  UPDATE staff_login_history
                  SET logout_time = ?
                  WHERE id = ?
                  ''', (current_time, login_record_id[0]))
              conn.commit()
              print("Staff logged out successfully.")
          else:
              print("No active login session found for the staff.")
      except sqlite3.Error as e:
          print(f"Error recording staff logout: {e}")

#====================================================================================================================
#CREATE ACCOUNTS
#import bcrypt
#from Validateinput import *
import sqlite3
import random
import getpass
  
def create_staff_account():
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      name1, name2, name3, id_number, phone_number, email, address, date_of_birth = collect_create_details()
      phone = phone_number
      work_id_number = collect_work_id_number()
      # Generate a unique salt for each password
      salt = bcrypt.gensalt()
      # Get the password and hash it
      hashed_password = hash_password(salt)
      try:
          cursor.execute(
              '''
              INSERT INTO staff (name1, name2, name3, phone, id_number, work_id_number, email, address, password, role)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              ''', (name1, name2, name3, phone, id_number, work_id_number, email, address, hashed_password, 'staff'))
          conn.commit()
          print("\nStaff account created successfully!")

      except sqlite3.Error as e:
          print(f"Error creating staff account: {e}")

def create_admin_account():
       print("CREATE AN ADMIN ACCOUNT")
       conn = sqlite3.connect('bank_main_database.db')
       cursor = conn.cursor()
       name1, name2, name3, id_number, phone, email, address, date_of_birth = collect_create_details()
       work_id_number = collect_work_id_number()

       # Generate a unique salt for each password
       #salt = bcrypt.gensalt()

       # Get the password and hash it
       hashed_password = 1234
       salt=1234

       cursor.execute(
           '''
           INSERT INTO admin_details (name1, name2, name3, id_number, phone, work_id_number, password, salt, timestamp)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
           ''', (name1, name2, name3, id_number, phone, work_id_number,
                 hashed_password, salt.decode('utf-8'), get_time()))
       conn.commit()
       print("\nAdmin account created successfully!")

       # Fetch admin ID
       cursor.execute(
           '''
           SELECT id, name1, name2, name3, password, salt FROM admin_details WHERE id_number = ? AND work_id_number = ?
           ''', (id_number, work_id_number))
       admin_id = cursor.fetchone()
       return admin_id

def create_user_account():
      print("\nCREATE A USER ACCOUNT")
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()

      try:
          name1, name2, name3, id_number, phone_number, email, address, date_of_birth = collect_create_details()
          phone = phone_number
          name = f"{name1} {name2} {name3}"

          # Generate a unique salt for each password
          salt = bcrypt.gensalt()

          # Get the password and hash it
          hashed_password = hash_password(salt)

          account_number = random.randint(10000000, 99999999)
          account_opening_date = get_time()

          cursor.execute(
              '''
              INSERT INTO users (
                  name, phone, id_number, account_number, balance, loan_balance, hashed_password, account_opening_date, last_login
              ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
              ''', (name, phone, id_number, account_number, 0, 0, hashed_password,
                    account_opening_date, None))

          # Commit the changes to the database
          conn.commit()
          print("\nUser account created successfully at:", get_time())
          print(f"User account for {name} created successfully with account number {account_number} at: {get_time()} ")

      except sqlite3.Error as e:
          print(f"SQLite error: {e}")
      finally:
          if conn:
              conn.close()

         
def collect_create_details():
    name1 = input("ENTER YOUR FIRST NAME: ")
    is_valid_name(name=name1)
    name2 = input("ENTER YOUR MIDDLE NAME: ")
    is_valid_name(name=name2)
    name3 = input("ENTER YOUR LAST NAME: ")
    is_valid_name(name=name3)
    id_number = input("ENTER YOUR 8-DIGIT ID NUMBER: ")
    is_valid_id_number(id_number)
    phone_number= input("ENTER YOUR 10-DIGIT PHONE NUMBER: ")
    is_valid_phone_number(phone_number)
   # Optional details
    email = input("ENTER EMAIL : ")
    is_valid_email(email)
    address = input("ENTER ADDRESS : ").strip()
    date_of_birth = get_date_of_birth()
    is_valid_date_of_birth(date_of_birth)    
    gender = input("ENTER GENDER (M/F/O): ").strip()
    is_valid_gender(gender)
    return name1, name2, name3, id_number, phone_number,  email, address, date_of_birth

def collect_work_id_number():
    work_id_number = input("ENTER 10 digit WORK ID NUMBER: ")
    if not work_id_number.isdigit() or len(work_id_number) != 10:
      print("INVALID WORK ID NUMBER. PLEASE ENTER A 10-DIGIT NUMERIC VALUE.")
      return
    return work_id_number

def hash_password(salt):
    for attempt in range(3):
        password = getpass.getpass("ENTER YOUR PASSWORD: ")
        password_confirmation = getpass.getpass("CONFIRM YOUR PASSWORD: ")

        if password == password_confirmation:
            is_valid_password(password)
            # Hashing the password with the provided salt
            hashed_password = password
            print("YOUR PASSWORD IS:", password)
            return hashed_password
        else:
            print(f"PASSWORDS DO NOT MATCH. YOU HAVE {2 - attempt} ATTEMPTS LEFT.")
            print()

    print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF ATTEMPTS. PLEASE TRY AGAIN LATER.")
    wait_time = 60  # 5 minutes in seconds
    print(f"PLEASE WAIT FOR {wait_time // 60} MINUTES AND {wait_time % 60} SECONDS BEFORE TRYING AGAIN.")
    time.sleep(wait_time/4)
    print()
    print()
    print("RESTARTING THE PROGRAM...")
    print()
    print()
    time.sleep(wait_time/4)
    print()
    print()
    print("LOADING...")
    time.sleep(wait_time/4)
    print()
    print()
    print("LOADING...")
    print()  
    print() 
    time.sleep(wait_time/4)
    print()
    print()
    print("YOU CAN NOW TRY AGAIN\nBE CAREFUL THIS TIME!.")
    print()
    return hash_password(salt)


#================================================================================================================================================
#VALIDATE INPUT
import string
#from validate_email_address import validate_email

def is_valid_name(name) -> bool:
       # Check length constraints
       max_len = 15
       if len(name) > max_len or len(name) == 0:
           print(f"Name should be between 1 and {max_len} characters long.")
           return False
       # Check for invalid characters
       for character in name:
           if character in string.punctuation or character.isnumeric() or character.isspace():
               print("Name should not contain special characters or numbers.")
               return False

       return True




def is_valid_email(email) -> bool:
    try:
        # Use the validate_email function to check if the email is valid
        # It's assumed that validate_email is a function from the validate_email_address module
       # is_valid = validate_email(email, verify=True)
        is_valid =True
        return is_valid

    except ValueError:
        # ValueError is raised for invalid email format
        return False
  



      

def is_valid_password(password: str) -> bool:
          error_message = None

          if len(password) < 8 or len(password) > 50:
              error_message = "Password should be between 8 and 50 characters in length."

          have_number, have_lowercase, have_uppercase, have_special_character = False, False, False, False

          for char in password:
              if char.isspace():
                  error_message = "Password should not contain spaces."
              elif char.isnumeric():
                  have_number = True
              elif char.islower():
                  have_lowercase = True
              elif char.isupper():
                  have_uppercase = True
              elif char in string.punctuation:
                  have_special_character = True

          if not (have_number and have_lowercase and have_uppercase and have_special_character):
              error_message = "Password should contain at least one digit, one lowercase letter, one uppercase letter, and one special character."

          return error_message is None

def is_valid_account_number(account_number: str) -> bool:
   if not account_number.isnumeric() or len(account_number) != 8:
       print("Account number should be 8 digits long and contain only numbers.")
       return False

   return True

def is_valid_phone_number(phone_number: str) -> bool:
      if len(phone_number) != 10 or not (phone_number.startswith('01') or phone_number.startswith('07')):
          print("Phone number should start with '01' or '07' and be 10 digits in length.")
          return False

      return phone_number.isnumeric()


def is_valid_id_number(id_number: str) -> bool:
      if id_number.isnumeric() and (len(id_number) == 7 or len(id_number) == 8):
          return True
      else:
          print("ID number should be 7 or 8 digits long.")
          return False

def is_valid_gender(gender: str) -> bool:
       valid_genders = ['M', 'F', 'O']

       if gender.upper() in valid_genders:
           return True
       else:
           print("Invalid gender. Please enter 'M' for Male, 'F' for Female, or 'O' for Other.")
           return False



#VALIDATE DATE OF BIRTH
from datetime import datetime

def get_current_year() -> int:
        current_date = datetime.now()
        return current_date.year

def get_date_of_birth() -> str:
        while True:
            try:
                date_str = input("Enter your date of birth (YYYY-MM-DD): ")
                birth_date = datetime.strptime(date_str, "%Y-%m-%d")

                current_year = get_current_year()

                if not (1900 <= birth_date.year <= current_year and birth_date <= datetime.now()):
                    raise ValueError("Invalid date of birth. Please enter a valid date.")

                return date_str

            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid date in the format YYYY-MM-DD.")

def is_valid_date_of_birth(date_of_birth: str) -> bool:
        current_date = datetime.now()
        birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")

        if birth_date.month < 1 or birth_date.month > 12:
            print("Invalid month in date of birth.")
            return False

        max_day_in_month = 0
        if birth_date.month in {1, 3, 5, 7, 8, 10, 12}:
            max_day_in_month = 31
        elif birth_date.month in {4, 6, 9, 11}:
            max_day_in_month = 30
        elif birth_date.year % 4 == 0 and (birth_date.year % 100 != 0 or birth_date.year % 400 == 0):
            max_day_in_month = 29
        else:
            max_day_in_month = 28

        if birth_date.day < 1 or birth_date.day > max_day_in_month:
            print("Invalid day in that month of date of birth.")
            return False

        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

        if age < 18:
            print("You need to be 18 years old or older to create a new account.")
            return False

        return True





def is_it_admin_or_staff():
  while True:
    print()
    print()
    print("P A M O J A G R O U P  B A N K\nYour online banking partner")
    print("CHOOSE YOUR ROLE IN THE BANK")
    print("┌───────────────────────────────────┐  ")
    print("│ ▶︎ 1 • ADMIN                       │  ")
    print("├───────────────────────────────────┤")
    print("│ ▶︎ 2 • STAFF                       │ ")
    print("├───────────────────────────────────┤")
    print("│ ▶︎ 3 • EXIT                        │ ")
    print("└───────────────────────────────────┘")
    print('=====================================')
    print()
    admin_option = input("Enter your choice: ")

    if admin_option == '1':
      admin_signup_menu()
    elif admin_option == '2':
      staff_signup_menu()
    elif admin_option == '3':
      exit()
    else:
      print("INVALID OPTION. ENTER A VALID OPTION")
      exit()

# ─────ACCESS ADMIN ACCOUNT MENU────────────────────────────────

def admin_signup_menu():
    while True:
      print()
      print()
      print("P A M O J A G R O U P  B A N K\nYour online banking partner")
      print("ADMIN MAIN MENU OPTIONS SELECTION")
      print("┌───────────────────────────────────┐  ")
      print("│ ▶︎ 1 • CREATE ADMIN ACCOUNT        │  ")
      print("├───────────────────────────────────┤")
      print("│ ▶︎ 2 • ADMIN LOG IN                │ ")
      print("├───────────────────────────────────┤")
      print("│ ▶︎ 3 • LOG OUT                     │ ")
      print("└───────────────────────────────────┘")
      print('=====================================')
      print()
      admin_option = input("Enter your choice: ")

      if admin_option == '1':
        create_admin_account()
        record_admin_login(admin_id=None)
        admin_tasks( admin_id)
      elif admin_option == '2':
        admin_login()
      elif admin_option == '3':
        exit()
      else:
        print("INVALID OPTION. ENTER A VALID OPTION")
        exit()

# ─────ADMIN MENU─────────────────────────────────────
def admin_tasks(admin_id):
  print()
  print()
  print("  P A M O J A G R O U P  B A N K\n   Your online banking partner")
  print("                                          ")
  print("  ADMIN ONLY     ")
  print("ADMINISTRATIVE TASKS ON USER")
  print("  MAIN MENU OPTIONS SELECTION      ┌─────────────────┐")
  print("┌─────────────────────────────────┐| ┌──────────╮    |")
  print("│ ▶︎ 1 • VIEW ALL ADMIN ACCOUNTS   │| | P G B  * |    │")
  print("├─────────────────────────────────┤| | BANK ****|    |")
  print("│ ▶︎ 2 • UPDATE ADMIN ACCOUNT      │| | .........|    |")
  print("├─────────────────────────────────┤| ╰──────────╯    |")
  print("│ ▶︎ 3 • CREATE STAFF ACCOUNT      │|  your banking   |")
  print("├─────────────────────────────────┤|    partner      | ")
  print("│ ▶︎ 4 • VIEW ALL STAFF ACCOUNTS   │|                 | ")
  print("├─────────────────────────────────┤|                 | ")
  print("│ ▶︎ 5 • SUSPEND A STAFF ACCOUNT   │|                 | ")
  print("├─────────────────────────────────┤|                 | ")
  print("│ ▶︎ 6 • VIEW SUSPENDED STAFF      │|  ADMINISTERING  | ")
  print("├─────────────────────────────────┤|     USER        | ")
  print("│ ▶︎ 7 • REINSTATE SUSPENDED STAFF │|   ACCOUNTS      | ")
  print("├─────────────────────────────────┤|                 | ")
  print("│ ▶︎ 8 • DELETE A STAFF ACCOUNT    │| CONTACT         | ")
  print("├─────────────────────────────────┤| DEVELOPER       | ")
  print("│ ▶︎ 9 •UPDATE A STAFF ACCOUNT     │| @Karish         | ")
  print("├─────────────────────────────────┤|Tel:0706816154   | ")
  print("│ ▶︎ 10 • VIEW BANK LOGINS         │|                 | ")
  print("├─────────────────────────────────┤|                 | ")
  print("│ ▶︎ 11 • VIEW DATABASE            │|                 | ")
  print("├─────────────────────────────────┤|  STRICTLY       | ")
  print("│ ▶︎ 12 • LOG OUT                  │| ADMINS ONLY     | ")
  print("└─────────────────────────────────┘└─────────────────┘")
  print('====================================================')
  admin_main_menu_option = int(input("Enter your choice: "))
  print()
  print()
  if admin_main_menu_option == 1:
    view_all_admin_accounts()
    admin_tasks( admin_id)
  elif admin_main_menu_option == 2:
    update_admin_details()
    admin_tasks( admin_id)
  elif admin_main_menu_option == 3:
    create_staff_account()
    admin_tasks( admin_id)
  elif admin_main_menu_option == 4:
    view_staff()
    admin_tasks(admin_id)
  elif admin_main_menu_option == 5:
    suspend_staff()
    admin_tasks(admin_id)
  elif admin_main_menu_option == 6:
    view_suspended_staff()
    admin_tasks(admin_id)
  elif admin_main_menu_option == 7:
    reinstate_suspended_staff()
    admin_tasks(admin_id)
  elif admin_main_menu_option == 8:
    delete_staff()
    admin_tasks(admin_id)
  elif admin_main_menu_option == 9:
    update_staff_account()
    admin_tasks(admin_id)  
  elif admin_main_menu_option == 10:
      view_admin_staff_logins(admin_id)
      admin_tasks(admin_id)
  elif admin_main_menu_option == 11:
    draw_tables_user_database(database_name='bank_main_database.db')
    admin_tasks(admin_id)
  elif admin_main_menu_option == 12:  
    record_admin_logout(admin_id)
    time = get_time()
    print("logged out successfully at ", time)
    exit()

  else:
    print("INVALID OPTION.\nYOU HAVE BEEN LOGGED OUT")
    is_it_admin_or_staff()


def view_admin_staff_logins(admin_id):
    print()
    print()
    print("  P A M O J A G R O U P  B A N K\n   Your online banking partner")
    print("                                          ")
    print("  ADMIN ONLY     ")
    print("┌───────────────────────────────────┐ ")
    print("│ ▶︎ 1 • VIEW ADMIN LOG INS          │ ")
    print("├───────────────────────────────────┤")
    print("│ ▶︎ 2 • ADMIN FAILED LOG IN ATTEMPTS│ ")
    print("├───────────────────────────────────┤")
    print("│ ▶︎ 3 • VIEW STAFF LOG INS          │")
    print("├───────────────────────────────────┤")
    print("│ ▶︎ 4 •  VIEW STAFF FAILED LOG INS  │ ")
    print("├───────────────────────────────────┤")
    print("│ ▶︎ 5 •  DELETE ADMIN LOG IN HISTORY│ ")
    print("├───────────────────────────────────┤")
    print("│ ▶︎ 6 • GO BACK                     │ ")
    print("└───────────────────────────────────┘")
    print('=====================================')
    print()

    # ─────ADMIN MENU───────────────────────────────────────
    admin_option = int(input("Enter your choice: "))
    print()
    print()
    if admin_option == 1:
      view_admin_login_history()  
      view_admin_staff_logins( admin_id)
    elif admin_option == 2:
      check_admin_failed_login_attempts()
      view_admin_staff_logins( admin_id)
    elif admin_option == 3:
      view_staff_login_history()
      view_admin_staff_logins( admin_id)
    elif admin_option == 4:
      view_failed_staff_logins()
      view_admin_staff_logins( admin_id)
    elif admin_option == 5:
      print("OPTION DEACTIVATED FOR SECURITY PURPOSES")
      #delete_admin_login_history()
      view_admin_staff_logins( admin_id)
    elif admin_option == 6:
      admin_tasks(admin_id)  
    else:
      print("INVALID OPTION.\nYOU HAVE BEEN LOGGED OUT")
      is_it_admin_or_staff()

 # ─────CREATE ADMIN ACCOUNT─────────────────────────────────────────
def create_admin_account():
        print("CREATE AN ADMIN ACCOUNT")
        name1 = input("ENTER YOUR FIRST NAME: ")
        name2 = input("ENTER YOUR MIDDLE NAME: ")
        name3 = input("ENTER YOUR LAST NAME: ")
        id_number = input("ENTER YOUR 8-DIGIT ID NUMBER: ")
        if len(id_number) != 8 or not id_number.isdigit():
            print("INVALID ID NUMBER.\n PLEASE ENTER 8-DIGIT ID NUMBER\n")
            create_admin_account()
        phone = input("ENTER YOUR 10-DIGIT PHONE NUMBER: ")
        if len(phone) != 10 or not phone.isdigit():
            print("INVALID PHONE NUMBER.\n PLEASE ENTER 10-DIGIT PHONE NUMBER\n")
            create_admin_account()
        work_id_number = input("ENTER YOUR 10-DIGIT WORK ID NUMBER: ")
        if len(work_id_number) != 10 or not work_id_number.isdigit():
            print("INVALID WORK ID NUMBER.\n PLEASE ENTER 10-DIGIT WORK ID NUMBER\n")
            create_admin_account()
        password = input("ENTER YOUR PASSWORD: ")
        hashed_password =password
        salt=1234
        cursor.execute(
            '''
                  INSERT INTO admin_details (name1, name2, name3, id_number, phone, work_id_number, password, salt, timestamp)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
              ''', (name1, name2, name3, id_number, phone, work_id_number,
                    hashed_password, salt, get_time()))
        conn.commit()
        print("\nAdmin account created successfully!")
        # FETCH ADMIN ID
        cursor.execute(
            '''
                SELECT id, name1, name2, name3, password, salt FROM admin_details WHERE id_number = ? AND work_id_number = ?
            ''', (id_number, work_id_number))
        admin_id = cursor.fetchone()
        record_admin_login(admin_id=None)
        admin_tasks( admin_id)

    # ───── ADMIN LOG IN─────────────────────────────────────────
def admin_login():
        print("FOR ADMIN LOGINS ONLY")
        id_number = input("ENTER YOUR 8-DIGIT ID NUMBER: ")
        work_id_number = input("ENTER YOUR 10-DIGIT WORK ID NUMBER: ")
        password = input("ENTER YOUR PASSWORD: ")
        try:
            cursor.execute(
                '''
                      SELECT id, name1, name2, name3, password, salt FROM admin_details WHERE id_number = ? AND work_id_number = ?
                  ''', (id_number, work_id_number))
            admin_data = cursor.fetchone()
            if admin_data:
                admin_id, name1, name2, name3, stored_hashed_password, salt = admin_data
                hashed_password = password
                if stored_hashed_password == hashed_password:
                    print(
                        f"Admin '{name1} {name2} {name3}' logged in successfully at {get_time()}"
                    )
                    # Record the admin login
                    record_admin_login(admin_id)
                    admin_tasks( admin_id)
                else:
                    print("INVALID PASSWORD. LOGIN FAILED.")
                    record_admin_failed_login_attempt(id_number, work_id_number,
                                                     'Invalid password')
            else:
                print("ACCOUNT NOT FOUND OR INVALID ID/WORK ID\n PLEASE TRY AGAIN!.")
                record_admin_failed_login_attempt(id_number, work_id_number,
                                                 'Invalid login credentials!')
        except Exception as e:
            print(f"An error occurred during login: {e}")
            record_admin_failed_login_attempt( id_number, work_id_number, 
                                             'Login error')


# ─────RECORD ADMIN LOGIN───────────────────────────────────────

def record_admin_login( admin_id):
    current_time = get_time()
    try:
      cursor.execute(
          '''
                   INSERT INTO admin_login_history (admin_id, login_time) VALUES (?, ?)
               ''', (admin_id, current_time))
      conn.commit()
    except sqlite3.Error as e:
      print(f"An error occurred while recording the admin login: {e}")
# ─────ADMIN LOG OUT TIME───────────────────────────────

def record_admin_logout( admin_id):
    current_time = get_time(
    )  # Ensure this returns the current time in the correct format
    try:
      # Find the ID of the most recent login record for this admin
      cursor.execute(
          '''
               SELECT id FROM admin_login_history
               WHERE admin_id = ? AND logout_time IS NULL
               ORDER BY login_time DESC
               LIMIT 1
               ''', (admin_id, ))
      login_record_id = cursor.fetchone()
      if login_record_id:
        # Update the logout time for the found record
        cursor.execute(
            '''
                   UPDATE admin_login_history
                   SET logout_time = ?
                   WHERE id = ?
                   ''', (current_time, login_record_id[0]))
        conn.commit()
      else:
        print("No active login session found for the admin.")
    except sqlite3.Error as e:
      print(f"An error occurred while recording the admin logout: {e}")

# ─────VIEW ADMIN LOGIN───────────────────────────────────────

def view_admin_login_history():
    print("PAMOJA GROUP BANK ADMIN LOGIN HISTORY ON ADMIN ACCOUNTS")
    try:
      cursor.execute('''
            SELECT ad.name1, ad.name2, ad.name3, alh.login_time, alh.logout_time 
            FROM admin_login_history alh
            JOIN admin_details ad ON alh.admin_id = ad.id
            ORDER BY alh.login_time ASC  -- Changed from DESC to ASC
        ''')
      rows =cursor.fetchall()

      if rows:
        print(f"{'Admin Name':<30}{'Login Time':<25}{'Logout Time':<25}")
        for row in rows:
          admin_name = ' '.join(filter(
              None, row[:3]))  # Concatenating non-empty name parts
          login_time = row[3] if row[3] else '---'
          logout_time = row[4] if row[4] else '---'
          print(f"{admin_name:<30}{login_time:<25}{logout_time:<25}")
      else:
        print("No admin login history found.")
    except sqlite3.Error as e:
      print(f"An error occurred while fetching the admin login history: {e}")

# ─────VIEW ADMIN LOGIN HISTORY───────────────────────────────────────

def record_admin_failed_login_attempt( id_number, work_id_number, reason):
    try:
      current_time = get_time()
      cursor.execute(
          '''
                    INSERT INTO failed_login_attempts (id_number, work_id_number, reason, attempt_time)
                    VALUES (?, ?, ?, ?)
                ''', (id_number, work_id_number, reason, current_time))
      conn.commit()
      print("Failed login attempt recorded.")
    except Exception as e:
      print(f"An error occurred while recording the failed login attempt: {e}")

# ─────VIEW FAILED LOGIN ATTEMPTS───────────────────────────────────────

def check_admin_failed_login_attempts():
    print(
        "SUSPICIOUS ACTIVITY! FAILED LOGIN ATTEMPTS ON PAMOJA GROUP BANK ADMIN ACCOUNTS"
    )
    try:
      cursor.execute('SELECT * FROM failed_login_attempts')
      attempts = cursor.fetchall()
      if attempts:
        print(
            f"{'ID Number':<15}{'Work ID Number':<15}{'Reason':<30}{'Attempt Time':<20}"
        )
        for attempt in attempts:
          print(
              f"{attempt[1]:<15}{attempt[2]:<15}{attempt[3]:<30}{attempt[4]:<20}"
          )
      else:
        print("No failed login attempts found.")
    except Exception as e:
      print(f"An error occurred while fetching failed login attempts: {e}")

# ─────UPDATE ADMIN DETAILS─────────────────────────────────────

def update_admin_details():
       print("UPDATE ADMIN DETAILS")
       admin_id = input("Enter your admin ID: ")  # Admin identification, e.g., work ID
       cursor.execute('SELECT * FROM admin_details WHERE id = ?', (admin_id,))
       admin_data = cursor.fetchone()

       if admin_data:
           # Asking for the current password for verification
           current_password = input("Enter your current password: ")
           # Verify the current password
           hashed_current_password = bcrypt.hashpw(current_password.encode('utf-8'), admin_data[8].encode('utf-8')).decode('utf-8')  # Assuming salt is at index 8

           if hashed_current_password == admin_data[7]:  # Assuming hashed password is at index 7
               print("Current Admin Details:")
               # Displaying current admin details (excluding password for security reasons)

               field_to_update = input("Enter the number of the field you want to update: ")
               new_value = input("Enter the new value: ")

               update_mapping = {
                   '1': 'name1',
                   '2': 'name2',
                   '3': 'name3',
                   '4': 'id_number',
                   '5': 'phone',
                   '6': 'work_id_number',
                   '7': 'password',  # Including password here as it will be handled separately
               }

               if field_to_update in update_mapping:
                   update_field = update_mapping[field_to_update]

                   if field_to_update == '7':  # If the password field is chosen for update
                       new_hashed_password, new_salt = hash_password(new_value)
                       cursor.execute(
                           'UPDATE admin_details SET password = ?, salt = ? WHERE id = ?',
                           (new_hashed_password, new_salt, admin_id))
                   else:
                       cursor.execute(
                           f'UPDATE admin_details SET {update_field} = ? WHERE id = ?',
                           (new_value, admin_id))

                   conn.commit()
                   print("Admin details updated successfully.")
               else:
                   print("Invalid field number. No changes made.")
           else:
               print("Incorrect admin password. Access denied.")
       else:
           print("Admin account not found.")

# ─────VIEW ALL ADMINS─────────────────────────────────────

def view_all_admin_accounts():
    print("VIEW ALL ADMIN ACCOUNTS")
    cursor.execute('SELECT * FROM admin_details')
    admin_accounts = cursor.fetchall()
    if admin_accounts:
      print(
          f"{'ID':<5}{'Name':<30}{'ID Number':<15}{'Phone Number':<15}{'Work ID Number':<15}{'Timestamp':<25}"
      )
      for admin in admin_accounts:
        admin_id = admin[0]
        admin_name = f"{admin[1]} {admin[2]} {admin[3]}"
        id_number = admin[4]
        phone_number = admin[5]
        work_id_number = admin[6]
        timestamp = admin[9]
        print(
            f"{admin_id:<5}{admin_name:<30}{id_number:<15}{phone_number:<15}{work_id_number:<15}{timestamp:<25}"
        )
    else:
      print("No admin accounts found.")



def delete_admin_login_history():
    date_threshold = input(
        "Enter the date (YYYY-MM-DD) to delete login history: ")
    try:
      # Delete records older than the specified date
      cursor.execute(
          '''
                DELETE FROM admin_login_history
                WHERE login_time = ?
                ''', (date_threshold, ))
      conn.commit()
      print(
          f"Login history for date {date_threshold} has been successfully deleted."
      )
    except sqlite3.Error as e:
      # Rollback in case of error
      conn.rollback()
      print(f"An error occurred while deleting the login history: {e}")



def create_staff_account():
         print("CREATE A STAFF ACCOUNT")
         name1 = input("ENTER FIRST NAME: ")
         name2 = input("ENTER MIDDLE NAME: ")
         name3 = input("ENTER LAST NAME: ")
         phone = input("ENTER PHONE NUMBER: ")
         id_number = input("ENTER ID NUMBER: ")
         work_id_number = input("ENTER WORK ID NUMBER: ")

         # Optional details
         email = input("ENTER EMAIL (optional, press Enter to skip): ").strip()
         address = input("ENTER ADDRESS (optional, press Enter to skip): ").strip()

         # Validate phone number and ID
         if not (phone.isdigit() and len(phone) == 10):
             print("INVALID PHONE NUMBER. PLEASE ENTER A 10-DIGIT NUMBER.")
             return

         if not id_number.isdigit():
             print("INVALID ID NUMBER. PLEASE ENTER A DIGIT VALUE.")
             return

         if not work_id_number.isdigit():
             print("INVALID WORK ID NUMBER. PLEASE ENTER A DIGIT VALUE.")
             return

         password = input("ENTER PASSWORD: ")

         # Hash the password and get the salt
         hashed_password, salt = hash_password(password)

         try:
             cursor.execute(
                 '''
                 INSERT INTO staff (name1, name2, name3, phone, id_number, work_id_number, email, address, password, salt, role)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                 ''', (name1, name2, name3, phone, id_number, work_id_number, email, address, hashed_password, salt, 'staff'))
             conn.commit()
             print("\nStaff account created successfully!")

         except sqlite3.Error as e:
             print(f"Error creating staff account: {e}")


def update_staff_account():
      print("UPDATE STAFF ACCOUNT")
      id_number = input("Enter the staff ID number to update: ")

      # Check if the staff with the provided ID number exists
      cursor.execute('SELECT * FROM staff WHERE id_number = ?', (id_number,))
      staff_data = cursor.fetchone()

      if staff_data:
          print("Current Staff Details:")
          staff_id, name1, name2, name3, phone, id_number, work_id_number, email, address, hashed_password, salt, is_suspended, role = staff_data
          status = 'Suspended' if is_suspended else 'Active'

          # Displaying current staff details (excluding password for security reasons)
          print(f"{'ID':<5}{'Name':<30}{'Phone Number':<15}{'Work ID Number':<15}{'Email':<30}{'Address':<30}{'Status':<10}")
          print(f"{staff_id:<5}{f'{name1} {name2} {name3}':<30}{phone:<15}{work_id_number:<15}{email:<30}{address:<30}{status:<10}")

          # Asking for the current password for verification
          current_password = input("Enter your current password: ")

          # Verify the current password
          hashed_current_password = bcrypt.hashpw(
              current_password.encode('utf-8'), hashed_password.encode('utf-8')).decode('utf-8')

          if hashed_current_password == hashed_password:
              field_to_update = input("Enter the number of the field you want to update:\n"
                                      "1. Name\n"
                                      "2. Phone Number\n"
                                      "3. Work ID Number\n"
                                      "4. Email\n"
                                      "5. Address\n"
                                      "6. Password\n"
                                      "7. Status (Suspended/Active)\n"
                                      "Enter your choice: ")

              if field_to_update == '1':
                  name1 = input("Enter the new first name: ")
                  name2 = input("Enter the new middle name: ")
                  name3 = input("Enter the new last name: ")
              elif field_to_update == '2':
                  phone = input("Enter the new phone number: ")
              elif field_to_update == '3':
                  work_id_number = input("Enter the new work ID number: ")
              elif field_to_update == '4':
                  email = input("Enter the new email: ").strip()
              elif field_to_update == '5':
                  address = input("Enter the new address: ").strip()
              elif field_to_update == '6':
                  new_password = input("Enter the new password: ")
                  hashed_password, salt = hash_password(new_password)
              elif field_to_update == '7':
                  new_status = input("Enter the new status (Suspended/Active): ").lower()
                  is_suspended = 1 if new_status == 'suspended' else 0

              # Update the staff account
              cursor.execute('''
                  UPDATE staff
                  SET name1=?, name2=?, name3=?, phone=?, work_id_number=?, email=?, address=?, password=?, salt=?, is_suspended=?
                  WHERE id_number=?
                  ''', (name1, name2, name3, phone, work_id_number, email, address, hashed_password, salt, is_suspended, id_number))
              conn.commit()

              print("Staff account updated successfully.")
          else:
              print("Incorrect staff password. Access denied.")
      else:
          print("Staff account not found.")



def view_staff():
  print("\nVIEW STAFF")
  cursor.execute('SELECT * FROM staff')
  staff_members = cursor.fetchall()
  if staff_members:
      print(f"{'ID':<5}{'Name':<30}{'Phone Number':<15}{'Work ID Number':<15}{'Email':<30}{'Address':<30}{'Status':<10}")
      for staff_member in staff_members:
          staff_id, name1, name2, name3, phone, id_number, work_id_number, email, address, hashed_password, salt, is_suspended, role = staff_member
          status = 'Suspended' if is_suspended else 'Active'
          print(f"{staff_id:<5}{f'{name1} {name2} {name3}':<30}{phone:<15}{work_id_number:<15}{email:<30}{address:<30}{status:<10}")
  else:
      print("No staff members found.")

def view_staff_login_history():
  print("\nVIEW STAFF LOGINS")
  cursor.execute('SELECT * FROM staff_login_history')
  logins = cursor.fetchall()

  if logins:
      print(
          f"{'ID':<5}{'Staff ID':<10}{'Login Time':<25}{'Logout Time':<25}")
      for login in logins:
          login_id, staff_id, login_time, logout_time = login
          print(
              f"{login_id:<5}{staff_id:<10}{login_time:<25}{logout_time:<25}")
  else:
      print("No staff logins found.")



  def view_failed_staff_logins():
       try:
           cursor.execute('''
               SELECT id, staff_id, username, role, reason, attempt_time, status
               FROM failed_login_attempts
               WHERE role = "staff"
           ''')
           attempts = cursor.fetchall()

           if attempts:
               print("\nFAILED STAFF LOGIN ATTEMPTS")
               print(f"{'ID':<5}{'Staff ID':<10}{'Username':<20}{'Reason':<30}{'Attempt Time':<20}{'Status':<10}")

               for attempt in attempts:
                   attempt_id, staff_id, username, role, reason, attempt_time, status = attempt
                   print(f"{attempt_id:<5}{staff_id:<10}{username:<20}{reason:<30}{attempt_time:<20}{status:<10}")
           else:
               print("No failed staff login attempts found.")
       except sqlite3.Error as e:
           print(f"An error occurred while fetching failed staff logins: {e}")




def delete_staff():
  id_number = input("Enter the staff ID number: ")
  cursor.execute(
      '''
      DELETE FROM staff WHERE id_number = ?
      ''', (id_number,))
  conn.commit()
  print(f"\nStaff member with ID NUMBER {id_number} deleted successfully!")

def suspend_staff():
  id_number = input("Enter the staff ID number : ")
  cursor.execute(
      '''
      UPDATE staff SET is_suspended = 1 WHERE id_number = ?
      ''', (id_number,))
  conn.commit()
  print(f"\nStaff member with ID {id_number} suspended successfully!")

def view_suspended_staff():
     try:
         cursor.execute('''
             SELECT id, name1, name2, name3, phone, id_number, work_id_number, email, address, status
             FROM staff
             WHERE is_suspended = 1
         ''')
         suspended_staff = cursor.fetchall()

         if suspended_staff:
             print("\nSUSPENDED STAFF MEMBERS")
             print(f"{'ID':<5}{'Name':<30}{'ID Number':<15}{'Phone Number':<15}{'Work ID Number':<15}{'Email':<30}{'Address':<30}{'Status':<10}")

             for staff in suspended_staff:
                 staff_id, name1, name2, name3, phone, id_number, work_id_number, email, address, status = staff
                 print(f"{staff_id:<5}{f'{name1} {name2} {name3}':<30}{id_number:<15}{phone:<15}{work_id_number:<15}{email:<30}{address:<30}{status:<10}")
         else:
             print("No suspended staff members found.")
     except sqlite3.Error as e:
         print(f"An error occurred while fetching suspended staff: {e}")


def reinstate_suspended_staff():
  id_number = input("Enter the staff ID number : ")
  cursor.execute(
      '''
      UPDATE staff SET is_suspended = 0 WHERE id_number = ?
      ''', (id_number,))
  conn.commit()
  print(f"\nSuspended staff member with ID {id_number} reinstated successfully!")


      # ─────ACCESS staff ACCOUNT MENU────────────────────────────────
def staff_signup_menu():
          while True:
            print()
            print()
            print("P A M O J A G R O U P  B A N K\nYour online banking partner")
            print("ADMIN MAIN MENU OPTIONS SELECTION")
            print("┌───────────────────────────────────┐  ")
            print("│ ▶︎ 1 • STAFF LOG IN                │  ")
            print("├───────────────────────────────────┤  ")
            print("│ ▶︎ 2 • EXIT                        │ ")
            print("└───────────────────────────────────┘")
            print('=====================================')
            print()
            admin_option = input("Enter your choice: ")

            if admin_option == '1':
              staff_login()
            elif admin_option == '2':
              exit()
            else:
              print("INVALID OPTION. ENTER A VALID OPTION")
              exit()
def staff_tasks_on_user_accounts(staff_id):
  #proceed_next()
  print()
  print()
  print("ADMINISTRATIVE TASKS ON USER")
  print("  MAIN MENU OPTIONS SELECTION ┌─────────────────┐")
  print("┌────────────────────────────┐| ┌──────────╮    |")
  print("│ ▶︎ 1 • CREATE USER ACCOUNT  │| | P G B  * |    │")
  print("├────────────────────────────┤| | BANK ****|    |")
  print("│ ▶︎ 2 • VIEW USER ACCOUNT    │| | .........|    |")
  print("├────────────────────────────┤| ╰──────────╯    |")
  print("│ ▶︎ 3 •MODIFY USER ACCOUNTS  │|  your banking   |")
  print("├────────────────────────────┤|    partner      | ")
  print("│ ▶︎ 4 •VIEW ALL USER ACCOUNTS│|                 | ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 5 • DELETE USER ACCOUNTS │|                 | ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 6 • VIEW TOP CUSTOMERS   │|  ADMINISTERING  | ")
  print("├────────────────────────────┤|     USER        | ")
  print("│ ▶︎ 7 •  ALL BANK BALANCE    │|   ACCOUNTS      | ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 8 • ALL BANK LOANS       │| CONTACT         | ")
  print("├────────────────────────────┤| DEVELOPER       | ")
  print("│ ▶︎ 9 • HIGH VALUE UNPAIDLOAN│| @Karish         | ")
  print("├────────────────────────────┤|Tel:0706816154   | ")
  print("│ ▶︎ 10 • ABOUT US            │|                 | ")
  print("├────────────────────────────┤|  STRICTLY       | ")
  print("│ ▶︎ 11 • LOG OUT             │| ADMINS ONLY     | ")
  print("└────────────────────────────┘└─────────────────┘")
  print('====================================================')
  print()
  main_menu_option = int(input("KEY IN YOUR MENU OPTION, 1-10: "))
  print()
  print()
  if main_menu_option == 1:
    create_user_account()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 2:
    view_user_account()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 3:
    modify_user_account()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 4:
    view_all_user_accounts()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 5:
    delete_user_account()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 6:
    view_top_20_customers()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 7:
    view_all_bank_balances()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 8:
    view_all_loans()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 9:
    view_top_20_loan_customers()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 10:
    about_us_page()
    staff_tasks_on_user_accounts(staff_id)
  elif main_menu_option == 11:
    record_staff_logout(staff_id)
    print(f"You have successfully logged out at {get_time}")

  else:
    print("INVALID CHOICE. PLEASE REENTER YOUR OPTION!")
    staff_tasks_on_user_accounts(staff_id)




def draw_tables_user_database(database_name='bank_main_database.db'):
      conn = sqlite3.connect(database_name)
      cursor = conn.cursor()

      try:
          # Fetch table names
          cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
          tables = cursor.fetchall()

          for table in tables:
              table_name = table[0]
              print(f"\nTable: {table_name}")
              print("-" * 70)  # Increased width for lines

              # Fetch column names and types
              cursor.execute(f"PRAGMA table_info({table_name});")
              columns = cursor.fetchall()

              # Print column headers
              header = "| "
              for column in columns:
                  header += f"{column[1]} ({column[2]}), ".ljust(20)  # Adjusted width
              print(header[:-2] + " |")

              # Print line for columns
              print("|" + "-" * 68 + "|")  # Adjusted width

              # Fetch and print data
              cursor.execute(f"SELECT * FROM {table_name};")
              rows = cursor.fetchall()
              for row in rows:
                  row_data = "| "
                  for value in row:
                      row_data += f"{str(value)}, ".ljust(20)  # Adjusted width
                  print(row_data[:-2] + " |")

                  # Print line for rows
                  print("|" + "-" * 68 + "|")  # Adjusted width

      except sqlite3.Error as e:
          print(f"SQLite error: {e}")

      finally:
          # Close the connection
          if conn:
              conn.close()


def staff_login():
  username = input("Enter your username: ")
  id_number = int(input("Enter your ID number: "))
  password = input("Enter your password: ")

  cursor.execute(
      '''
      SELECT id, password, is_suspended FROM staff WHERE id_number = ? 
      ''', (id_number,))
  staff_data = cursor.fetchone()

  if staff_data:
      staff_id, stored_hashed_password, is_suspended = staff_data

      if is_suspended:
          print("ACCOUNT IS SUSPENDED. PLEASE CONTACT ADMIN.")
          return

      hashed_password = password

      if stored_hashed_password == hashed_password:
          print(f"Staff '{username}' logged in successfully at {get_time()}")
          record_staff_login(staff_id)
          staff_tasks_on_user_accounts(staff_id)
      else:
          print("INVALID PASSWORD. LOGIN FAILED.")
          record_staff_failed_login_attempt(
              staff_id=staff_id, username=username, role='staff', reason='Invalid password')
  else:
      print("STAFF ACCOUNT NOT FOUND.\nPLEASE TRY AGAIN.")
      record_staff_failed_login_attempt(
          staff_id=None, username=username, role='staff', reason='Account not found')


def record_staff_failed_login_attempt(staff_id, username, role, reason):
  current_time = get_time()
  try:
      cursor.execute(
          '''
          INSERT INTO staff_login_attempts (staff_id, username, role, reason, time_attempted) VALUES (?, ?, ?, ?, ?)
          ''', (staff_id, username, role, reason, current_time))
      conn.commit()
      print(f"Staff login attempt recorded at {current_time}")
  except sqlite3.Error as e:
      print(f"An error occurred while recording staff login attempt: {e}")


def record_staff_login(staff_id):
  current_time = get_time()
  try:
      cursor.execute(
          '''
          INSERT INTO staff_login_history (staff_id, login_time) VALUES (?, ?)
          ''', (staff_id, current_time))
      conn.commit()
  except sqlite3.Error as e:
      print(f"Error recording staff login: {e}")


def record_staff_logout(staff_id):
      current_time = get_time()
      try:
          # Find the ID of the most recent login record for this staff member
          cursor.execute(
              '''
              SELECT id FROM staff_login_history
              WHERE staff_id = ? AND logout_time IS NULL
              ORDER BY login_time DESC
              LIMIT 1
              ''', (staff_id,))
          login_record_id = cursor.fetchone()

          if login_record_id:
              # Update the logout time for the found record
              cursor.execute(
                  '''
                  UPDATE staff_login_history
                  SET logout_time = ?
                  WHERE id = ?
                  ''', (current_time, login_record_id[0]))
              conn.commit()
              print("Staff logged out successfully.")
          else:
              print("No active login session found for the staff.")
      except sqlite3.Error as e:
          print(f"Error recording staff logout: {e}")

#====================================================================================================================
#Main page

import sqlite3
#import Maindatabase
#from About_us_page import about_us_page
#from admin_module import*
#from CommonFunctions import *
import random
#import pyfiglet
# datetime import date, datetime
# CommonFunctions import hash_password
#import pytz



def connect_to_database():
  try:
      conn = sqlite3.connect('bank_main_database.db')
      cursor = conn.cursor()
      return conn, cursor
  except sqlite3.Error as e:
      print(f"Error connecting to the database: {e}")
      return None

#START OF PROJECT
def admin_user_selection():
  print()
  print()
  print("P A M O J A G R O U P  B A N K\nYour online banking partner")
  print("WHICH ACCOUNT DO YOU WISH TO ACCESS?")
  print("┌───────────────────────────────────┐  ")
  print("│ ▶︎ 1 • USER                        │  ")
  print("├───────────────────────────────────┤")
  print("│ ▶︎ 2 • ADMIN                       │ ")
  print("├───────────────────────────────────┤")
  print("│ ▶︎ 3 • LOG OUT                     │ ")
  print("└───────────────────────────────────┘")
  print('=====================================')
  print()
  selection = input("Enter your choice: ")
  if selection == '1':
    signup_login()
  elif selection == '2':
    is_it_admin_or_staff()
  elif selection == '3':
    log_out()
  else:
    print("INVALID OPTION. ENTER A VALID OPTION")
    signup_login()

# ───────LOG IN/ CREATE ACCOUNT OPTION─────────────────────────────────
def signup_login():
  print("   \nWELCOME CUSTOMER TO OUR BANKING SERVICES")
  print("   \n  PRESS A KEY TO SELECT AN OPTION")
  print("  ╭────────────────────────────────────╮")
  print("  │ ▶ 1 • LOG IN TO YOUR ACCOUNT       │")
  print("  ├────────────────────────────────────┤")
  print("  │ ▶ 2 • OPEN AN ACCOUNT WITH US      │")
  print("  ├────────────────────────────────────┤")
  print("  │ ▶ 3  • FORGOT PASSWORD             │")
  print("  ├────────────────────────────────────┤")
  print("  │ ▶ 4  • VIEW ABOUT US               │")
  print("  ├────────────────────────────────────┤")
  print("  │ ▶ 5  • EXIT AND CLOSE PROGRAM      │")
  print("  ╰────────────────────────────────────╯")
  print('=========================================')
  signup_or_login_option = int(input("ENTER YOUR OPTION!\n"))
  if signup_or_login_option == 1:
    log_in_to_account()
  if signup_or_login_option == 2:
    create_user_account()
  if signup_or_login_option == 3:
    forgot_password()
  if signup_or_login_option == 4:
    about_us_page()
    signup_login()
  if signup_or_login_option == 5:
    print("THANK YOU FOR USING OUR BANKING SERVICES")
    exit()
  else:
    print("YOU HAVE PRESSED AN INVALID OPTION\n\n")
    signup_login()



def log_in_to_account():
    print("\nLOG INTO YOUR ACCOUNT")
    account_number = input("ENTER YOUR ACCOUNT NUMBER: ")
    password = input("ENTER YOUR PASSWORD: ")

    conn = sqlite3.connect('bank_main_database.db')
    cursor = conn.cursor()

    try:
        # Retrieve user information from the database
        cursor.execute('''
            SELECT u.id, u.name, u.account_number, u.hashed_password, u.frozen
            FROM users u
            WHERE u.account_number = ?;
        ''', (account_number,))
        user = cursor.fetchone()

        if user is not None:
            user_id, user_name, _, hashed_password, frozen_status = user

            # Check if the user account is frozen
            if frozen_status == 1:
                print("YOUR ACCOUNT IS FROZEN. PLEASE CONTACT CUSTOMER SUPPORT.")
                return

            # Hash the entered password and compare with the stored hashed password
            #if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            if password== hashed_password:
                # Passwords match
                print(f"\nSUCCESSFUL LOG IN AT: {get_time()}\nWELCOME TO PAMOJA GROUP BANK")

                # Update last login time
                cursor.execute('''
                    UPDATE users
                    SET last_login = ?
                    WHERE account_number = ?;
                ''', (datetime.now(), account_number))
                conn.commit()

                # Call your main menu or any other relevant function here
                main_menu(user_id, user_name)  # Pass the user_id and user_name
            else:
                print("INVALID ACCOUNT NUMBER OR PASSWORD. PLEASE TRY AGAIN.")
        else:
            print("INVALID ACCOUNT NUMBER OR PASSWORD. PLEASE TRY AGAIN.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        # Close the connection
        if conn:
            conn.close()

# ───FORGOT  PASSWORD────────────────────────────────────────────────────────────────────────────────
def forgot_password():
  changepasscode = int(
      input("PRESS 1 TO CHANGE PASSWORD, PRESS 2 TO GO BACK "))
  if changepasscode == 1:
    account_number = input("ENTER YOUR ACCOUNT NUMBER: ")
    user_id = input("Enter your id number")
    change_password(account_number, user_id)
  elif changepasscode == 2:
    signup_login()
  else:
    print("YOU HAVE PRESSED AN INVALID OPTION\n\n")
    forgot_password()


# ─────CHANGE PASSWORD──────────────────────────────────────────────────────────────────────────
def change_password(account_number, user_id):
  # Retrieve user id information from the database
  cursor.execute('SELECT * FROM users WHERE account_number = ?',
                              (account_number, ))
  user = cursor.fetchone()
  hashed_password = hash_password()
  cursor.execute(
      'UPDATE users SET hashed_password = ? WHERE account_number = ?',
      (hashed_password, account_number))
  conn.commit()
  print(f"PASSWORD CHANGED SUCCESSFULLY AT: {get_time()}")
  main_menu(account_number, user[3])  # Pass the id_number as user_id


# ─────OPEN ACCOUNT───────────────────────────────────────────────────────────────────────────────
def create_user_account():
  print("\nCREATE AN ACCOUNT")
  conn = sqlite3.connect('bank_main_database.db')
  cursor = conn.cursor()
  try:
    name = input("Enter your full name: ")
    phone = input("Enter your phone number: ")
    id_number = input("Enter your ID number: ")
    # Hash the password
    hashed_password =1234
    hashedpassword=hashed_password
    account_number = random.randint(10000000, 99999999)
    account_opening_date = get_time()
    cursor.execute(
        '''
          INSERT INTO users (
              name, phone, id_number, account_number, balance, loan_balance, hashed_password, account_opening_date, last_login
          ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
      ''', (name, phone, id_number, account_number, 0, 0, hashedpassword,
            account_opening_date, None))
    # Commit the changes to the database
    conn.commit()
    print("\nUser account created successfully at: {get_time()}!")
    print(f"Your account number is: {account_number}")
    print("Please remember your account number and password.")
    main_menu(account_number, id_number)
  except sqlite3.Error as e:
    print(f"SQLite error: {e}")
  finally:
    if conn:
      #conn.close()
      pass


# ─────MAIN MENU OPTIONS DISPLAY─────────────────────────────────────────────
def main_menu(account_number, user_id):
  print()
  print()
  print(
      "        P A M O J A G R O U P  B A N K\n        Your online banking partner"
  )
  print("  MAIN MENU OPTIONS SELECTION ┌─────────────────┐")
  print("┌────────────────────────────┐| ┌──────────╮    |")
  print("│ ▶︎ 1 • CHECK BALANCE        │| | P G B  * |    │")
  print("├────────────────────────────┤| | BANK ****|    |")
  print("│ ▶︎ 2 • MAKE DEPOSIT         │| | .........|    |")
  print("├────────────────────────────┤| ╰──────────╯    |")
  print("│ ▶︎ 3 • WITHDRAW CASH        │|  your banking   |")
  print("├────────────────────────────┤|    partner      | ")
  print("│ ▶︎ 4 • TRANSFER CASH        │|                 | ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 5 • TAKE LOAN            │|                 | ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 6 • PAY LOAN             │| ASK FOR HELP    | ")
  print("├────────────────────────────┤|CONTACT ADMIN    | ")
  print("│ ▶︎ 7 • CHECK LOAN BALANCE   │|Tel:+254706816154| ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 8 • ACCOUNT STATEMENT    │|                 | ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 9 • VIEW ACCOUNT DETAILS │|                 | ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 10 • DELETE USER ACCOUNT │|                 | ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 11 • CHANGE PASSWORD     │|                 | ")
  print("├────────────────────────────┤|                 | ")
  print("│ ▶︎ 12 • LOG OUT             │|                 | ")
  print("└────────────────────────────┘└─────────────────┘")
  print('====================================================')
  main_menu_option = int(input("KEY IN YOUR MENU OPTION, 1-10: "))
  print()
  print()
  if main_menu_option == 1:
    check_balance(account_number, user_id)
    main_menu(account_number, user_id)
  elif main_menu_option == 2:
    make_deposit(account_number, user_id)
    main_menu(account_number, user_id)
  elif main_menu_option == 3:
    make_withdraw(account_number, user_id)
  elif main_menu_option == 4:
    transfer_money(account_number, user_id)
    main_menu(account_number, user_id)
  elif main_menu_option == 5:
    apply_for_loan(account_number, user_id)
    main_menu(account_number, user_id)
  elif main_menu_option == 6:
    repay_loan(account_number, user_id)
    main_menu(account_number, user_id)
  elif main_menu_option == 7:
    check_loan_balance(account_number)
    main_menu(account_number, user_id)
  elif main_menu_option == 8:
    view_transactions(user_id, account_number)
    main_menu(account_number, user_id)
  elif main_menu_option == 9:
     view_account_details(user_id, account_number)
     main_menu(account_number, user_id)
  elif main_menu_option == 10:
    delete_account(account_number, user_id)
    main_menu(account_number, user_id)
  elif main_menu_option == 11:
    change_password(account_number, user_id)
  elif main_menu_option == 12:
    log_out()
  else:
    print("INVALID CHOICE. PLEASE REENTER YOUR OPTION!")
    main_menu(account_number, user_id)


# ─────CHECK BALANCE──────────────────────────────────────────────────────────
def check_balance(account_number, user_id):
  try:
    with sqlite3.connect('bank_main_database.db') as conn:
      cursor = conn.cursor()
      cursor.execute('SELECT balance FROM users WHERE account_number = ?',
                     (account_number, ))
      balance_result = cursor.fetchone()
      if balance_result is not None:
        balance = balance_result[0]
        # Improved formatting for the balance output
        formatted_balance = "{:,.2f}".format(balance)
        print(
            f"YOUR ACCOUNT BALANCE IS: Ksh{formatted_balance} AS AT {get_time()}")
        if balance == 0:
          print("YOU HAVE NO BALANCE. PLEASE MAKE A DEPOSIT.")
        return balance
      else:
        print("ACCOUNT NOT FOUND.")
        return None
  except sqlite3.Error as e:
    print(f"Error accessing database: {e}")
    return None


# ─────MAKE DEPOSITS───────────────────────────────────────────────────────
def make_deposit(account_number, user_id):
            amount = float(input("ENTER THE DEPOSIT AMOUNT: ksh"))
            conn = sqlite3.connect('bank_main_database.db')
            cursor = conn.cursor()
            try:
              # Check if the account exists
              cursor.execute('SELECT id, balance FROM users WHERE account_number = ?',
                             (account_number, ))
              user_data = cursor.fetchone()
              if user_data is not None:
                user_id, current_balance = user_data
                new_balance = current_balance + amount
                # Update the user's balance
                cursor.execute('UPDATE users SET balance = ? WHERE id = ?',
                               (new_balance, user_id))
                # Record the deposit transaction
                time = get_time()
                transaction_type = 'DEPOSIT'
                cursor.execute(
                    'INSERT INTO transactions (user_id, transaction_type, transaction_amount, transaction_time) VALUES (?, ?, ?, ?)',
                    (user_id, transaction_type, amount, time))
                conn.commit()
                print(f"Deposited Ksh{amount}. New balance: Ksh{new_balance}")
              else:
                print("Account not found.")
            except sqlite3.Error as e:
              print(f"SQLite error: {e}")
            finally:
              conn.close()

# ──────WITHDRAW FUNDS────────────────────────────────────────────────────────────────────────────
def make_withdraw(account_number, user_id):
         try:
             with sqlite3.connect('bank_main_database.db') as conn:
                 cursor = conn.cursor()
                 cursor.execute('SELECT balance FROM users WHERE account_number = ?', (account_number,))
                 balance_result = cursor.fetchone()
                 if balance_result is not None:
                     current_balance = balance_result[0]
                     amount = float(input("ENTER THE WITHDRAWAL AMOUNT: ksh"))
                     if amount <= current_balance:
                         new_balance = current_balance - amount
                         cursor.execute('UPDATE users SET balance = ? WHERE account_number = ?', (new_balance, account_number))
                         transaction_time = get_time()
                         cursor.execute('''
                             INSERT INTO transactions (user_id, transaction_type, transaction_amount, transaction_time)
                             VALUES (?, ?, ?, ?)
                         ''', (user_id, 'WITHDRAWAL', amount, transaction_time))
                         conn.commit()
                         print(f"WITHDRAWAL SUCCESSFUL. WITHDREW ksh{amount}. NEW BALANCE: ksh{new_balance}")
                     else:
                         print("INSUFFICIENT BALANCE. WITHDRAWAL FAILED.")
                 else:
                     print("ACCOUNT NOT FOUND.")
         except sqlite3.Error as e:
             print(f"SQLite error: {e}")
         finally:
           pass
         main_menu(account_number, user_id)


# ─────TAKE LOAN───────────────────────────────────────────
def apply_for_loan(account_number, user_id):
           conn = sqlite3.connect('bank_main_database.db')
           cursor = conn.cursor()
           try:
               # Fetch the user's current balance and existing loan balance
               cursor.execute('SELECT balance, loan_balance FROM users WHERE account_number = ?', (account_number,))
               user_data = cursor.fetchone()
               if user_data is not None:
                   current_balance, existing_loan_balance = user_data
                   print(f"\nCURRENT BALANCE: Ksh{current_balance}")
                   print(f"EXISTING LOAN BALANCE: Ksh{existing_loan_balance}")
                   if existing_loan_balance == 0:
                       max_loan_amount = current_balance * 3  # Assuming the max loan amount is 3 times the current balance
                       request_amount = float(input(f"Enter the loan amount you want to apply for (up to Ksh{max_loan_amount}): "))
                       time = int(input("Enter the repayment period in years:/n Loan compounded at interest of 10% annually"))
                       if 0 < request_amount <= max_loan_amount:
                           # Calculate the new loan balance and the updated account balance            
                           principal = request_amount
                           rate = 0.10
                           totaltopay=  principal * (1 + rate)**time
                           interest = totaltopay - principal
                           new_loan_balance = existing_loan_balance + totaltopay
                           updated_balance = current_balance + request_amount
                           # Update the user's loan balance and account balance in the database
                           cursor.execute('UPDATE users SET loan_balance = ?, balance = ? WHERE account_number = ?', (new_loan_balance, updated_balance, account_number))
                           # Record the loan transaction
                           timestamp = get_time()
                           cursor.execute('INSERT INTO transactions (user_id, transaction_type, transaction_amount, transaction_time) VALUES (?, "LOAN", ?, ?)', (user_id, request_amount, timestamp))
                           conn.commit()
                           print(f"\nLoan application successful! You have been granted a loan of Ksh{request_amount}.")
                           print(f"Your new loan balance is Ksh{new_loan_balance}.")
                           print(f"Your updated account balance is Ksh{updated_balance}.")
                       else:
                           print("Loan application unsuccessful. Requested amount exceeds the maximum allowable limit.")
                   else:
                       print("You have an existing loan. Please clear your previous loan before applying for a new one.")
               else:
                   print("Account not found.")
           except sqlite3.Error as e:
               print(f"SQLite error: {e}")
               conn.rollback()
           finally:
               if conn:
                   conn.close()

# ─────REPAY LOAN───────────────────────────────────────────
def repay_loan(account_number, user_id):
         conn = sqlite3.connect('bank_main_database.db')
         cursor = conn.cursor()
         try:
             # Check the user's existing loan balance and current account balance
             cursor.execute('SELECT loan_balance, balance FROM users WHERE account_number = ?', (account_number,))
             loan_balance_result = cursor.fetchone()
             if loan_balance_result is not None:
                 existing_loan_balance, current_balance = loan_balance_result
                 # User inputs the repayment amount
                 repayment_amount = float(input("Enter the repayment amount: Ksh"))
                 if repayment_amount <= 0:
                     print("Invalid repayment amount. Please enter a valid amount.")
                     return
                 # Determine if the repayment amount exceeds the loan balance
                 if repayment_amount > existing_loan_balance:
                     # Calculate excess amount and update loan balance to zero
                     excess_amount = repayment_amount - existing_loan_balance
                     new_balance = current_balance + excess_amount
                     repayment_amount = existing_loan_balance  # Set repayment to just clear the loan
                 else:
                     # No excess amount; update loan balance accordingly
                     new_loan_balance = existing_loan_balance - repayment_amount
                     new_balance = current_balance
                 # Update the user's loan balance and account balance in the database
                 cursor.execute('UPDATE users SET loan_balance = ?, balance = ? WHERE account_number = ?', (max(new_loan_balance, 0), new_balance, account_number))
                 # Record the loan repayment transaction
                 timestamp = get_time()
                 cursor.execute('INSERT INTO transactions (user_id, transaction_type, transaction_amount, transaction_time) VALUES (?, "LOAN REPAYMENT", ?, ?)', (user_id, repayment_amount, timestamp))
                 conn.commit()
                 print(f"Loan repayment successful!") 
                 check_loan_balance(account_number)
             else:
                 print("Account not found.")
         except sqlite3.Error as e:
             print(f"SQLite error: {e}")
             conn.rollback()
         finally:
             if conn:
                 conn.close()


# ─────VIEW LOAN BALANCE────────────────────────────────────────
def check_loan_balance(account_number):
            conn = sqlite3.connect('bank_main_database.db')
            cursor = conn.cursor()
            try:
                # Retrieve the user's loan balance and account balance
                cursor.execute('SELECT loan_balance, balance FROM users WHERE account_number = ?', (account_number,))
                result = cursor.fetchone()
                if result is not None:
                    loan_balance, account_balance = result
                    print(f"\nAccount Number: {account_number}")
                    print(f"Current Loan Balance: Ksh{loan_balance}")
                    print(f"Current Account Balance: Ksh{account_balance}")
                    if loan_balance > 0:
                        print("You have an outstanding loan. Consider making repayments to avoid additional interest.")
                    else:
                        print("You currently have no outstanding loan. Keep up the good financial management!")

                else:
                    print("Account not found. Please check the account number and try again.")
            except sqlite3.Error as e:
                print(f"SQLite error: {e}")
            finally:
                if conn:
                    conn.close()

# ─────DELETE ACCOUNT───────────────────────────────────────────
def delete_account(account_number, user_id):
        conn = sqlite3.connect('bank_main_database.db')
        cursor = conn.cursor()
        try:
            # Verify the account exists and check balances
            cursor.execute('SELECT balance, loan_balance FROM users WHERE account_number = ?', (account_number,))
            account_data = cursor.fetchone()
            if account_data is None:
                print(f"Account {account_number} not found.")
                return
            account_balance, loan_balance = account_data
            if loan_balance > 0 or account_balance > 0:
                print("Account cannot be deleted. Ensure both loan and bank balances are zero.")
                return
            # Confirmation from the user before deletion
            confirmation = input(f"Are you sure you want to delete account {account_number}? This action cannot be undone (yes/no): ").lower()
            if confirmation == 'yes':
                # Proceed with account deletion
                cursor.execute('DELETE FROM users WHERE account_number = ?', (account_number,))
                conn.commit()
                print(f"Account {account_number} has been successfully deleted.")
            else:
                print("Account deletion cancelled.")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            conn.rollback()
        finally:
            if conn:
                conn.close()

def view_account_details(account_number, user_id):
  conn = sqlite3.connect('bank_main_database.db')
  cursor = conn.cursor()
  try:
    # Retrieve the user's account details
    cursor.execute('SELECT name, account_number, balance, loan_balance FROM users WHERE account_number = ?', (account_number,))
    result = cursor.fetchone()
    if result is not None:
      name, account_number, balance, loan_balance = result
      print(f"\nAccount Number: {account_number}")
      print(f"Name: {name}")
      print(f"Balance: Ksh{balance}")
      print(f"Loan Balance: Ksh{loan_balance}")
    else:
      print("Account not found. Please check the account number and try again.")
  except sqlite3.Error as e:
    print(f"SQLite error: {e}")
  finally:
    if conn:
      conn.close()

def view_transactions(account_number, user_id):
    conn=sqlite3.connect('bank_main_database.db')
    cursor=conn.cursor()
    try:
        # Retrieve the user's transactions
        cursor.execute('SELECT transaction_type, transaction_amount, transaction_time FROM transactions WHERE user_id = ?', (user_id,))
        transactions = cursor.fetchall()
        if transactions:
            print("\nTransaction History:")
            for transaction in transactions:
                transaction_type, transaction_amount, transaction_time = transaction
                print(f"Transaction Type: {transaction_type}")
                print(f"Transaction Amount: Ksh{transaction_amount}")
                print(f"Transaction Time: {transaction_time}")
                print("--------------------")
        else:
            print("No transactions found for this user.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
      
"""  
# ─────VIEW TRANSACTION HISTORY───────────────────────────────────────────
def view_transactions(user_id, account_number):
  conn = sqlite3.connect('bank_main_database.db')
  cursor = conn.cursor()
  try:
      # Fetch user's transactions from the database, ordered from oldest to newest
      cursor.execute(
          '''
          SELECT t.transaction_type, t.transaction_amount, t.transaction_time
          FROM transactions t
          JOIN users u ON t.user_id = u.id
          WHERE u.id = ? AND u.account_number = ?
          ORDER BY t.transaction_time ASC  -- Changed from DESC to ASC
          ''', (user_id, account_number))
      transactions = cursor.fetchall()
      if transactions:
          print("\nTransaction History (Oldest to Newest):")
          print(f"{'Type':<20}{'Amount':<15}{'Timestamp':<25}")
          for transaction in transactions:
              print(f"{transaction[0]:<20}{transaction[1]:<15}{transaction[2]:<25}")
      else:
          print("No transactions found for this user and account number combination.")
  except sqlite3.Error as e:
      print(f"SQLite error: {e}")
  finally:
      if conn:
          conn.close()
"""

# ─────TRANSFER MONEY───────────────────────────────────────────
def transfer_money(account_number, user_id):
         conn = sqlite3.connect('bank_main_database.db')
         cursor = conn.cursor()
         try:
             # Input details for the transfer
             recipient_account_number = input("Enter the recipient's account number: ")
             transfer_amount = float(input("Enter the amount to transfer: "))
             # Check if both the sender and recipient accounts exist
             cursor.execute('SELECT id, balance FROM users WHERE account_number = ?', (account_number,))
             sender_data = cursor.fetchone()
             cursor.execute('SELECT id, balance FROM users WHERE account_number = ?', (recipient_account_number,))
             recipient_data = cursor.fetchone()
             if sender_data is None or recipient_data is None:
                 print("Either sender or recipient account not found.")
                 return
             sender_id, sender_balance = sender_data
             recipient_id, _ = recipient_data
             # Check if the sender has sufficient balance
             if sender_balance < transfer_amount:
                 print("Insufficient balance in sender's account.")
                 return
             # Perform the transfer
             # Deduct from sender
             new_sender_balance = sender_balance - transfer_amount
             cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (new_sender_balance, sender_id))
             # Add to recipient
             cursor.execute('UPDATE users SET balance = balance + ? WHERE id = ?', (transfer_amount, recipient_id))
             # Record the transaction for both sender and recipient
             timestamp = get_time()
             cursor.execute('INSERT INTO transactions (user_id, transaction_type, transaction_amount, transaction_time) VALUES (?, "MONEY TRANSFER", ?, ?)', (sender_id, transfer_amount, timestamp))
             cursor.execute('INSERT INTO transactions (user_id, transaction_type, transaction_amount, transaction_time) VALUES (?, "MONEY RECEIVED", ?, ?)', (recipient_id, transfer_amount, timestamp))
             conn.commit()
             print(f"Transfer of Ksh{transfer_amount} to account {recipient_account_number} completed successfully.")
         except sqlite3.Error as e:
             print(f"SQLite error: {e}")
             conn.rollback()
         except ValueError:
             print("Invalid input. Please enter a valid amount.")
         finally:
             if conn:
                 conn.close()





admin_user_selection()


