# Import libraries/modules needed to run the program and its functions
import datetime
from datetime import date 
from pandas import DataFrame as df #Allows creation of CSV file for file handling
import pandas as pd
from csv import writer
import glob
import os.path  
import os       #Allows file handling
from matplotlib import style    #Visual representation of statistics 
import matplotlib.pyplot as plt

# Checks if the csv for the current month has been created
def checkIf(month):
    try :
        df = pd.read_csv(f'{month}.csv')
        return df.empty
    except :
        return True
    
# Gives the month per date    
def check_month(month):
    switch = {
        1 : 'January',
        2 : 'February',
        3 :'March',
        4 :'April',
        5 :'May',
        6 :'June',
        7 :'July',
        8 :'August',
        9 :'September',
        10 :'October',
        11 :'November',
        12 :'December',
    }
    return switch.get(month,1)

# Tracker function takes input from user, stores in a dictionary, then passes the dictionary to a datarame.
# Dataframe is saved as csv if it doesn't exist, otherwise it appends as 'a' mode. The dataframe stores the user expenses, income and total income per month
def tracker(date = 0, income =" ", foodDrinks =" ", Transport =" ", lifeEntertainment =" ", miscellaneous =" ", housing= " ", total_expenses = ''):
    data = {
    'Date':date,
    'Income':income,
    'Food & Drinks':foodDrinks,
    'Transport': Transport,
    'Life & Entertainment': lifeEntertainment,
    'Miscellaneous': miscellaneous,
    'Housing': housing, 
    'Total Expenses': total_expenses
    }
    
    database = df.from_dict(data,orient='index')
    database = database.transpose()
    decide = 'a'
    check = False
    datea = str(date)
    year,month,day = map(int, datea.split('-'))
    current_month = check_month(month)
    if checkIf(current_month):
        decide = 'w'
        check = True
    database.to_csv(f'{current_month}.csv',mode = decide,header=check,index=False)
 
 

# Function to accept arguments and create a dataframe for user defined budget.   
# CREATION OF CSV FILE FOR BUDGET RECORDS
def budget_data(food=' ', transport=" ", life_entertainment=" ", miscelleneous=" ", Housing=" "):
    data = {
        'Food & Drinks Budget': food,
        'Transport Budget': transport,
        'Life & Entertainment Budget': life_entertainment,
        'Miscelleneous Budget': miscelleneous,
        'HOusing Budget': Housing
    }

    if os.path.exists('./Budget Records.csv'):
        list = [food, transport, life_entertainment, miscelleneous, Housing]
        with open('Budget Records.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list)
            f_object.close()
    else:
        df = pd.DataFrame.from_dict(data, orient='index')
        df = df.transpose()
        df.to_csv('Budget Records.csv', index=False)
        


# CREATION OF EMERGENCY FUNDS RECORDS IN CSV FORMAT
def emergency_fund_data(date=0, amount_saved=' '):
    data = {
        'Date': date,
        'Amount_Saved': amount_saved,
    }
    if os.path.exists('./Emergency Funds.csv'):
        list = [date, amount_saved]
        with open('Emergency Funds.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list)
            f_object.close()
    else:
        df = pd.DataFrame.from_dict(data, orient='index')
        df = df.transpose()
        df.to_csv('Emergency Funds.csv', index=False)




# Defines the main class Monify with all its associated attributes/methods. 
class Monify:
  # Gets user input for income and passes to the tracker function as arguments
  def add_income():
    date = str(input('Enter Date (YYYY-MM-DD)\n: --> '))
    year,month,day=map (int,date.split('-'))
    date = datetime.date(year,month,day)
    income = int(input("Enter your income for the month \n: --> "))
    tracker(date,income,0,0,0,0,0,0)
    
    
  # Passes user input to tracker function under expenditure category.
  # Adds exception handling to avoid wrong input terminating the program.
  def add_expenditure():
    print("\t\t\t\nEXPENSE CATEGORIES: \n1. Food & Drinks\n2. Transport\n3. Life & Entertainment\n4. Miscellaneous\n5. Housing\n")
    
    while True:
        try:
            response = int(input("\nPlease select a category number: "))
            print("\n")
        except ValueError:
            print("Not a valid option!\n")
            continue
        else:
            break
        
    if response == 1:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-')) #converts string to datetime 
                date = datetime.date(year,month,day)
                
                fd = str(input("\nHow much did you spend on \"Food and Drinks?\" --> "))
            
                
            except ValueError:
                print("Please enter valid input!\n")
                continue
              
            else: 
                tracker(date,0,fd,0,0,0,0,0) 
                print("\nExpense recorded successfully!\n")
                user_response  = input("Add another expenditure (yes/no)? ")
                user_response.lower()
                if user_response == "yes":
                  Monify.add_expenditure()
                if user_response == 'no':
                  menu()
                
            
    elif response == 2:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-'))
                date = datetime.date(year,month,day)
                
                ht = str(input("\nHow much did you spend on \"Transport?\" --> "))

            except ValueError:
                print("Please enter valid input!\n")
                continue
              
            else:
                tracker(date,0,0,ht,0,0,0,0)
                print("\nExpense recorded successfully!\n")
                user_response  = input("Add another expenditure (yes/no)? ")
                user_response.lower()
                if user_response == "yes":
                  Monify.add_expenditure()
                if user_response == 'no':
                  menu()
               


    elif response == 3:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-'))
                date = datetime.date(year,month,day)
                
                le = str(input("\nHow much did you spend on \"Life & Entertainment?\" --> "))

            except ValueError:
                print("Please enter valid input!\n")
                continue
              
            else:
                tracker(date,0,0,0,le,0,0,0)
                print("\nExpense recorded successfully!\n")
                user_response  = input("Add another expenditure (yes/no)? ")
                user_response.lower()
                if user_response == "yes":
                  Monify.add_expenditure()
                if user_response == 'no':
                  menu()
               


    elif response == 4:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-'))
                date = datetime.date(year,month,day)
                
                misc = str(input("\nHow much did you spend on \"Miscellaneous?\" --> "))
                
            except ValueError:
                print("Please enter valid input!\n")
                continue
            else:
                tracker(date,0,0,0,0,misc,0,0)
                print("\nExpense recorded successfully!\n")
                user_response  = input("Add another expenditure (yes/no)? ")
                user_response.lower()
                if user_response == "yes":
                  Monify.add_expenditure()
                if user_response == 'no':
                  menu()
                


    elif response == 5:
        while True:
            try:
                date = str(input('Enter expenditure date (YYYY-MM-DD) (optional) \n: --> '))
                year,month,day=map(int,date.split('-'))
                date = datetime.date(year,month,day)
                
                house = str(input("\nHow much did you spend on \"Housing?\" --> "))
        
            except ValueError:
                print("Please enter valid input!\n")
                continue
              
            else:
                tracker(date,0,0,0,0,0,house,0)
                print("\nExpense recorded successfully!\n")
                user_response  = input("Add another expenditure (yes/no)?: ")
                user_response.lower()
                if user_response == "yes":
                  Monify.add_expenditure()
               
   
    
  # Method allows user to create a budget of how they want to spend their income
  # Budget is saved to dataframe and a csv file is created for it.          
  def add_budget():
        print("\nYou are about to enter your budget for the CURRENT MONTH")

        while True:
            try:
                user_option = str(
                    input("\nWould you like to proceed (yes/no): "))
                user_option = user_option.lower()
                if user_option == 'yes':
                    user_input1 = input(
                        str("Enter your budget for Food & drinks: "))
                    user_input2 = input(
                        str("Enter your budget for Transport: "))
                    user_input3 = input(
                        str("Enter your budget for Life & Entertainment: "))
                    user_input4 = input(
                        str("Enter your budget for Miscellaneous: "))
                    user_input5 = input(str("Enter your budget for Housing: "))
                    budget_data(user_input1, user_input2,
                                user_input3, user_input4, user_input5)
                    print("SUCCESSFULLY RECORDED")
                    menu()
            except ValueError:
                print("Enter a valid response")
                continue
            else:
                break
  
  
  
  # This function on call, displays the data the user has in budget records. 
  def view_budget():
    try:
      if os.path.exists('./Budget Records.csv'):
          get = pd.read_csv('Budget Records.csv', header=0)
          print(get)
      else:
          print("\nYou have not created a budget record!")
    except FileNotFoundError:
      print("\nYou have not created a budget record!")
      pass
      


  # Function asks user for input for emergency funds
  # User input is passed to secondary function "emergency_fund_data" which creates the dataframe and csv
  def add_emergency_fund():
    try:
      emergency_fund_amount = int(input("How much do you want to add to your Emergency fund account: "))
      date_saved = input ("Enter the date: ")
      year, month, day = map(int, date_saved.split('-'))
      date = datetime.date(year, month, day)
      emergency_fund_data(date, emergency_fund_amount)
      print(f"\n {emergency_fund_amount} has been added to your Emergency Funds Savings")
    
    except ValueError:
      print("Please input the right value!")
      Monify.add_emergency_fund()
  
    
  # This function on call, displays the amount the user has in emergency funds.  
  def view_emergency_fund():
    try:
      if os.path.exists('./Emergency Funds.csv'):
          get = pd.read_csv('Emergency Funds.csv', header=0)
          emergeny_fund_balance = get['Amount_Saved'].sum()
          print(f"You have ${emergeny_fund_balance} in your emergency fund Account. Keep up the saving habit! ")
      else:
          print("\nYou have not created your Emergency Fund account !")
    except FileNotFoundError:
      print("\nYou have not created your Emergency Fund account!")
      pass
    
  
  # Allows user to view their shopping list
  # Shopping list is retrieved from the system if existent then converted to a dataframe which is printed, otherwise prints a message. 
  def view_shopping_list():
    if os.path.exists('./Shopping List.csv'):
      list = pd.read_csv('Shopping List.csv', header=0)
      print("\nThis is your most recent shopping list: --> \n")
      print(list)
    else:
      print("\nYou have not added any shopping list yet!")
      Monify.add_shopping_list()
    
    
    
  # Allows a user create a shopping list, save to a dictionary, and then passes it to a dataframe
  # Dataframe is saved as csv file and if csv for shopping list is already existent, it removes and writes the current.
  def add_shopping_list():
    shopping_list = {}
    ans = True
    while ans:
      print("\nEnter the items in your shopping list and their prices -->")
      item = str(input("\nEnter the item name: --> "))
      value = int(input("\nEnter the price: --> "))
      shopping_list[item] = value
      
      print("Recorded!\n")
      resp = str(input("Add another item? (yes/no) --> "))
      resp = resp.upper()
      if resp == "YES":
        continue
      else:
        ans = False
        df = pd.DataFrame.from_dict(shopping_list, orient = 'index')
        df = df.transpose()
        
        if os.path.exists('./Shopping List.csv'):
          os.remove('Shopping List.csv')
          
        df.to_csv('Shopping List.csv')

    # User is asked if they would like to view the shopping list which they just added.
    user_response = input(str("Would you like to view your shopping list (yes/no)"))
    user_response.lower
    if user_response == "yes":
      Monify.view_shopping_list()

   
   

# Function allows a user to pass arguments to it.
# Arguments are saved to dataframe as input and a csv file is created for debt record as in the previous tracker function.
def debt_data(date = 0, lender = " ", amount = " ", due = " ",):
  data = {
  'Date':date,
  'Lender':lender,
  'Amount Borrowed':amount,
  'Repayment Date': due
  }

  if os.path.exists('./Debt Records.csv'):  
    list = [date,lender,amount,due]
    with open('Debt Records.csv', 'a') as f_object:   
      writer_object = writer(f_object)
      writer_object.writerow(list)
      f_object.close()     
  else:
    df = pd.DataFrame.from_dict(data, orient = 'index')  
    df = df.transpose()                                 
    df.to_csv('Debt Records.csv', index = False)



# This class and it's methods are repsonsible for keeping track of user's debt and repaying them on request.
# Pay debt has the functionality of removing the debt record file (overwriting it) and updating it with recent records.
class Debt_account(Monify):
  
  # Collects user input of debt information and passes it as arguments into the debt_data function
  def add_debt_record():
    amount = input("\nHow much did you borrow? --> ")
    date = input("\nWhen did borrow this money? -->  ")
    lender = input("\nEnter the name of the lender who you owe: --> ")
    due = input("\nWhat date do you need to pay back?: --> ")
    
    debt_data(date, lender, amount, due)

  def pay_debt():
    data = pd.read_csv('Debt Records.csv', header=0)  
    print(data)                                       
    
    response = int(input("\nWhich loan have you payed back? (Enter row number) --> "))
    data = data.drop(index = response)
  
    if os.path.exists('./Debt Records.csv'):   
      os.remove('Debt Records.csv')    
      data.to_csv('Debt Records.csv')
    


    
# Defines the class Statistics with all its associated attributes/methods.
# Statistics inherits from parent class Monify
class Statistics(Monify):

  # This allows a user choose a month to show a graph of.
  # User input is converted to match records using title() method. Handles "filenotfound" error 
  def spending_chart():
    user_input = input("What month would you like to view the statistics for: ")
    user_input.title()  
    slices = []
    headers = ["Food & drinks", "Transport", "Life & Entertainment", "Miscellaneous", "Housing"]  

    try:
      get =  pd.read_csv (f'{user_input}.csv')   #reads the csv file to get what month statistics the user would like to see
      slices.append(get['Food & Drinks'].sum())
      slices.append(get['Transport'].sum())
      slices.append(get['Life & Entertainment'].sum())
      slices.append(get['Miscellaneous'].sum())
      slices.append(get['Housing'].sum())
      print(slices)
    
      colors = ['r', 'y', 'g', 'b', 'm' ]  #colors of the pie slices
      myexplode = (0, 0, 0, 0, 0)

      #plotting the pie chart 
      fig, ax = plt.subplots(figsize =(10, 7))
      wedges, texts, autotexts = ax.pie(slices,
                                  autopct = '%1.1f%%',
                                  explode = myexplode,
                                  labels = headers,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90)
      #legend to indicate what each color represent with respect to categories
      ax.legend(title = "Expense Categories", loc ="upper left" , bbox_to_anchor =(1, 0, 0.5, 1))
      plt.setp(autotexts, size = 8, weight ="bold")
      ax.set_title('Spending by Categories')
      plt.show()
      
    except FileNotFoundError:  
      print("\nYou haven't inputed any data for that month")



  # Function to plot a graph of income against expense.
  # Handles "filenotfound" errors.
  def income_expense():
    list_month= list(map(lambda x : check_month(x), range(1, 13)))  
    month_name = []
    income = []
    expense = []
    total_expense = []
    for month in list_month:
      try:
        get = pd.read_csv(f'{month}.csv', index_col= 'Date') #reads each month CSV file 
        income.append(get['Income'].sum())
        expense.append(get['Food & Drinks'].sum())
        expense.append(get['Transport'].sum())
        expense.append(get['Life & Entertainment'].sum())
        expense.append(get['Miscellaneous'].sum())
        expense.append(get['Housing'].sum())
        month_name.append(month)
        total_expense.append(sum(expense))

      except FileNotFoundError :
        pass
    
    #plotting the bar chart 
    graph_detail = df({
        'Income':income,
        'Expense':total_expense} ,index = month_name)
    style.use('fivethirtyeight')
    columns = ['Income', 'Expenses']
    graph_detail.plot.bar(rot = 0)
    plt.title(f"Cash Flow Trend")
    plt.show()




# Menu function to show user the functionalities of the app and what they can do on the CLI
def menu():
  print("\n\t\t########################### WELCOME TO MONIFY ###########################")
  print("\n\t\tWhat do you want to do?\n\t\t1. Add Income\n\t\t2. Add Expenditure\n\t\t3. Debt Accounting\n\t\t4. Shopping List\n\t\t5. Emergency Funds\n\t\t6. Add Budget\n\t\t7. View Statistics\n")
  
  while True:
    try:
      ans = int(input("Please enter an option: --> "))
    except ValueError:
      print("\nPlease enter an integer!")
      continue
    else:
      break

  if ans == 1:
    Monify.add_income()
    
  elif ans == 2:
    Monify.add_expenditure()
    
  elif ans == 3:
    while True:
      try:
        print("\n\t\t1. Add Debt Record\n\t\t2. Pay Debt\n")
        debt = int(input("What do you want to do? --> "))
      except ValueError:
        print("\nPlease enter an integer!\n")
        continue
      else:
        break
    if debt == 1:
      Debt_account.add_debt_record()
    elif debt == 2:
      Debt_account.pay_debt()

  elif ans == 4:
    while True:
      try:
        print("\n\t\t1. Add items to Shopping List\n\t\t2. View Shopping List\n")
        user_shop_resp = int(input("What do you want to do? --> "))
      except ValueError:
        print("\nPlease enter an integer!\n")
        continue
      else:
        break
    if user_shop_resp == 1:
      Monify.add_shopping_list()
    elif user_shop_resp == 2:
      Monify.view_shopping_list()
  
  elif ans == 5:
    while True:
      try:
        print("\n\t\t1. Add Emergency Funds\n\t\t2. View Emergency Funds Savings\n")
        user_shop_resp = int(input("What do you want to do? --> "))
      except ValueError:
        print("\nPlease enter an integer!\n")
        continue
      else:
        break
    if user_shop_resp == 1:
      Monify.add_emergency_fund()
    elif user_shop_resp == 2:
      Monify.view_emergency_fund()
    
  
  elif ans == 6:
    while True:
      try:
        print("\n\t\t1. Add Budget\n\t\t2. View Budget\n")
        user_shop_resp = int(input("What do you want to do? --> "))
      except ValueError:
        print("\nPlease enter an integer!\n")
        continue
      else:
        break
    if user_shop_resp == 1:
      Monify.add_budget()
    elif user_shop_resp == 2:
      Monify.view
    
  
  elif ans == 7:
    while True:
      try:
        print("\n\t\t1. View Income-Expense Chart\n\t\t2. View Spending Chart\n")
        user_stats_resp = int(input("What do you want to do? --> "))
      except ValueError:
        print("\nPlease enter an integer!\n")
        continue
      else:
        break
    if user_stats_resp == 1:
      Statistics.income_expense()
    elif user_stats_resp == 2:
      Statistics.spending_chart()
 
 
 
# Program is initiated with a while loop.
# The loop prints the menu as long as user input for opration is true.   
run = True
while run:
  menu()
  resp = str(input("\nDo you want to perform another operation? (yes/no) --> "))
  resp = resp.upper()
  if resp == "YES":
    continue
  elif resp == "NO":
    run = False
    
