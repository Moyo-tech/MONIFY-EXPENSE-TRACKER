
from tkinter import *
from tkcalendar import Calendar
from datetime import *
from datetime import date 
from pandas import DataFrame as df
import pandas as pd
from csv import writer
import glob
import os.path
import os
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np


def checkIf(month):
    try :
        df = pd.read_csv(f'{month}.csv')
        return df.empty
    except :
        return True
    
    
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


def tracker(date = " ", income =" ", foodDrinks =" ", Transport =" ", lifeEntertainment =" ", miscellaneous =" ", housing= " ", total_expenses = ''):
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
    month,day,year = map(int, datea.split('/'))
    current_month = check_month(month)
    if checkIf(current_month):
        decide = 'w'
        check = True
    database.to_csv(f'{current_month}.csv',mode = decide,header=check,index=False)
    
    
    
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


       
def shopping_list(item, price):
    if os.path.exists('./Shopping List.csv'):
        list = [item,price]
        with open('SHopping List.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list)
            f_object.close()
    else:
        data = {
        'Item Name': item,
        'Price': price
        }
 
        df = pd.DataFrame.from_dict(data, orient='index')
        df = df.transpose()
        df.to_csv('Shopping List.csv', index=False)




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

 
 
   
root = Tk()
root.title('Monify - Expense Tracker Pro')
root.geometry("600x600")

logo_label = Label(root, text = 'MONIFY', font=('Century Gothic', 40))
logo_label.pack()

greet = Label(root, text="Welcome to Monify - The Best Expense Tracker App", font=('Century Gothic', 11))
greet.pack()

version_info = Label(root, text="Version 1.0.1.1\n\n\n\n\n\n\n\n\n\n\n", font=('Century Gothic', 7))
version_info.pack()


options = [
    "Add Income",
    "Add Expenditure",
    "Add Budget",
    "View Budget",
    "Add Shopping List",
    "View Shopping List",
    "Add Debt Record",
    "Pay Debt/Remove Record",
    "View Debt Records",
    "Add Emergency Fund",
    "Emergency Fund Balance",
    "Income-Expense Chart",
    "Spending Chart"
]


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
  
   
   
     
clicked = StringVar()
clicked.set("Select An Operation to Perform")

def selected(event):
    if clicked.get() == "Add Income":
        add_income()
    elif clicked.get() == "Add Expenditure":
        expenditure()
    elif clicked.get() == "Add Budget":
        budget()
    elif clicked.get() == "View Budget":
        view_budget()
    elif clicked.get() == "Add Shopping List":
        if os.path.exists('./Shopping List.csv'):
            os.remove('Shopping List.csv')
        add_shopping_list()
    elif clicked.get() == "View Shopping List":
        view_shopping_list()
    elif clicked.get() == "Add Debt Record":
        add_debt()
    elif clicked.get() == "Pay Debt/Remove Record":
        pass
    elif clicked.get() == "View Debt Records":
        view_debts()
    elif clicked.get() == "Add Emergency Fund":
        add_emergency_fund()
    elif clicked.get() == "Income-Expense Chart":
        income_expense_input()
    elif clicked.get() == "Spending Chart":
        spending_chart_input()

drop = OptionMenu(root, clicked, *options, command = selected)
drop.pack()




# Function to get user input and pass to tracker
def add_income():
    new = Toplevel(root)
    new.geometry("400x400")
    
    # Displays calendar picker with instruction of "enter date"
    l1 = Label(new, text="Pick Income Date Below: ", font=('Century Gothic', 10)).pack()
    cal = Calendar(new, selectmode = 'day', year = 2021, month = 11,day = 15)
    cal.pack(pady = 5)

    # Entry field for income
    l1 = Label(new, text = 'Enter Income: ', font=('Century Gothic', 10)).pack()
    e1 = Entry(new)
    e1.pack(pady =5)
    
    def success():
        l5 = Label(new, text="Successful!").pack()
        
    submit = Button(new, text = "Save", bg = 'black', fg = 'white', width=15, command =lambda: [tracker(cal.get_date(),e1.get()), success(), new.destroy()]).pack()
    



def expenditure():
    expenditure = Toplevel(root)
    expenditure.geometry("400x400")
    
    # Displays calendar picker with instruction of "enter date"
    l1 = Label(expenditure, text="Pick Expense Date Below: ", font=('Century Gothic', 12)).pack()
    cal = Calendar(expenditure, selectmode = 'day', year = 2021, month = 11,day = 15)
    cal.pack(pady = 5)
    
    options = [
        "Food and Drinks",
        "Transport",
        "Life and Entertainment",
        "Miscellaneous",
        "Housing"
    ]
    
    clicked = StringVar()
    clicked.set("Select Category of Expenditure")


    def selected(event):
        if clicked.get() == "Food and Drinks":
            tracker(cal.get_date(),0,e1.get(),0,0,0,0,0)
        elif clicked.get() == "Transport":
            tracker(cal.get_date(),0,0,e1.get(),0,0,0,0)
        elif clicked.get() == "Life and Enetertainment":
            tracker(cal.get_date(),0,0,0,e1.get(),0,0,0)
        elif clicked.get() == "Miscellaneous":
            tracker(cal.get_date(),0,0,0,0,e1.get(),0,0)
        elif clicked.get() == "Housing":
            tracker(cal.get_date(),0,0,0,0,0,e1.get(),0)

    drop = OptionMenu(expenditure, clicked, *options, command = selected)
    drop.pack(pady = 5) 
    
    # Entry field for expenditure
    l1 = Label(expenditure, text = 'Enter Amount Spent: ', font=('Century Gothic', 10)).pack()
    e1 = Entry(expenditure)
    e1.pack(pady=5)
    
    def success():
        l5 = Label(expenditure, text="Successful!").pack()
      
    submit = Button(expenditure, text = "Save", bg = 'black', fg = 'white', width=15, command =lambda: [tracker(cal.get_date(),e1.get()), success(),expenditure.destroy()]).pack()



def budget():
    budget = Toplevel(root)
    budget.geometry("400x400")
    
    l1 = Label(budget, text="Enter Food and Drinks Budget").grid(row = 1, column = 0, sticky = W, pady = 2)
    l2 = Label(budget, text="Enter Transport Budget").grid(row = 4, column = 0, sticky = W, pady = 2)
    l3 = Label(budget, text="Enter Life & Entertainment Budget").grid(row = 2, column = 0, sticky = W, pady = 2)
    l4 = Label(budget, text="Enter Miscellaneous Budget").grid(row = 3, column = 0, sticky = W, pady = 2)
    l5 = Label(budget, text="Enter Housing Budget").grid(row = 5, column = 0, sticky = W, pady = 2)

    e1 = Entry(budget)
    e1.grid(row=1, column=1, sticky=W, pady=2)
    e2 = Entry(budget)
    e2.grid(row=2, column=1, sticky=W, pady=2)
    e3 = Entry(budget)
    e3.grid(row=3, column=1, sticky=W, pady=2)
    e4 = Entry(budget)
    e4.grid(row=4, column=1, sticky=W, pady=2)
    e5 = Entry(budget)
    e5.grid(row=5, column=1, sticky=W, pady=2)
     
    def success():
        l5 = Label(budget, text="Successful!").grid(row = 8, column = 1, sticky = W, pady = 2)
 
    submit = Button(budget, text = "Save", bg = 'black', fg = 'white', width=15, command =lambda: [(budget_data(e1.get(),e2.get(),e3.get(),e4.get(),e5.get())), success(), budget.destroy()]).grid(row=6, column=1, sticky=W, pady=2)
   
   
def view_budget():
    if os.path.exists('./Budget Records.csv'):
        os.startfile('Budget Records.csv', 'open')
    else:
        view_budget = Toplevel(root)
        view_budget.geometry("210x50")
        l1 = Label(view_budget, text="Error! No budget added yet", font=('Century Gothic', 10)).pack()
        
        
def add_shopping_list():
    shop = Tk()
    shop.geometry("300x200")
    
    l1 = Label(shop, text="Enter item name").grid(row = 1, column = 0, sticky = W, pady = 2)
    e1 = Entry(shop)
    e1.grid(row=1, column=1, sticky=W, pady=2)
    
    l2 = Label(shop, text="Enter item price").grid(row = 2, column = 0, sticky = W, pady = 2)
    e2 = Entry(shop)
    e2.grid(row=2, column=1, sticky=W, pady=2)
    
    def success():
        l5 = Label(shop, text="Successful!").grid(row = 8, column = 1, sticky = W, pady = 2)
    
    submit = Button(shop, text = "Save", bg = 'black', fg = 'white', width=15, command =lambda: [(shopping_list(e1.get(),e2.get())), success()]).grid(row=6, column=1, sticky=W, pady=2)
    close = Button(shop, text = "Close List", bg = 'black', fg = 'white', width=15, command =lambda: shop.destroy()).grid(row=7, column=1, sticky=W, pady=2)
    

def view_shopping_list():
    if os.path.exists('./Shopping List.csv'):
        os.startfile('Shopping List.csv', 'open')
    else:
        view_list = Toplevel(root)
        view_list.geometry("210x50")
        l1 = Label(view_list, text="Error! No list added yet", font=('Century Gothic', 10)).pack()  
    



def add_debt():
    new = Toplevel(root)
    new.geometry("600x600")
    
    # Displays calendar picker with instruction of "enter date"
    l1 = Label(new, text="Pick Loan Date Below: ", font=('Century Gothic', 10)).pack()
    cal = Calendar(new, selectmode = 'day', year = 2021, month = 11,day = 15)
    cal.pack(pady = 5)

    # Entry field for income
    l2 = Label(new, text = 'Enter Lender\'s Name: ', font=('Century Gothic', 10)).pack()
    e1 = Entry(new)
    e1.pack(pady =5)
    
    l3 = Label(new, text = 'Enter Loan Amount: ', font=('Century Gothic', 10)).pack()
    e2 = Entry(new)
    e2.pack(pady =5)
    
    l4 = Label(new, text="Pick Repayment Date: ", font=('Century Gothic', 10)).pack()
    cal2 = Calendar(new, selectmode = 'day', year = 2022, month = 12,day = 15)
    cal2.pack(pady = 5)
    
    def success():
        l5 = Label(new, text="Successful!").pack()
        
    submit = Button(new, text = "Save", bg = 'black', fg = 'white', width=15, command =lambda: [debt_data(cal.get_date(),e1.get(),e2.get(),cal2.get_date()), success(), new.destroy()]).pack()

def view_debts():
    if os.path.exists('./Debt Records.csv'):
        os.startfile('Debt Records.csv', 'open')
    else:
        view_list = Toplevel(root)
        view_list.geometry("210x50")
        l1 = Label(view_list, text="Error! No debts added yet", font=('Century Gothic', 10)).pack()  
        
def add_emergency_fund():
    new = Toplevel(root)
    new.geometry("400x400")
    
    # Displays calendar picker with instruction of "enter date"
    l1 = Label(new, text="Pick Date Below: ", font=('Century Gothic', 10)).pack()
    cal = Calendar(new, selectmode = 'day', year = 2021, month = 11,day = 15)
    cal.pack(pady = 5)

    # Entry field for income
    l2 = Label(new, text = 'Enter Amount Saved: ', font=('Century Gothic', 10)).pack()
    e1 = Entry(new)
    e1.pack(pady =5)
    
    submit = Button(new, text = "Save", bg = 'black', fg = 'white', width=15, command =lambda: [emergency_fund_data(cal.get_date(),e1.get()), new.destroy()]).pack()


def income_expense_input():
    new = Toplevel(root)
    new.geometry("250x250")
    
    l2 = Label(new, text = 'Enter Month To Show Chart For: ', font=('Century Gothic', 10)).pack()
    e1 = Entry(new)
    e1.pack(pady =5)
    
    submit = Button(new, text = "Save", bg = 'black', fg = 'white', width=15, command =lambda: [income_expense(e1.get()), new.destroy()]).pack()
    
    
    
def income_expense(user_input):
    list_month= list(map(lambda x : check_month(x), range(1, 13)))  
    month_name = []
    income = []
    expense = []
    total_expense = []
    for month in list_month:
      try:
        get = pd.read_csv(f'{user_input}.csv', index_col= 'Date') #reads each month CSV file 
        income.append(get['Income'].sum())
        expense.append(get['Food & Drinks'].sum())
        expense.append(get['Transport'].sum())
        expense.append(get['Life & Entertainment'].sum())
        expense.append(get['Miscellaneous'].sum())
        expense.append(get['Housing'].sum())
        month_name.append(month)
        total_expense.append(sum(expense))

      except FileNotFoundError or IndexError:
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


def spending_chart_input():
    new = Toplevel(root)
    new.geometry("250x250")
    
    l2 = Label(new, text = 'Enter Month To Show Chart For: ', font=('Century Gothic', 10)).pack()
    e1 = Entry(new)
    e1.pack(pady =5)
    
    submit = Button(new, text = "Save", bg = 'black', fg = 'white', width=15, command =lambda: [income_expense(e1.get()), new.destroy()]).pack()
    

def spending_chart(user_input):
    user_input.title()  
    slices = []
    headers = ["Food & drinks", "Transport", "Life & Entertainment", "Miscellaneous", "Housing"] 

    try:
        if os.path.exists(f'./{user_input}.csv'):
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
        else:
            view_chart = Toplevel(root)
            view_chart.geometry("210x50")
            l1 = Label(view_budget, text="Error! No data added yet", font=('Century Gothic', 10)).pack()
    except FileNotFoundError or IndexError:  
      pass



quit_button = Button(root, text = 'Exit', bg = 'red', fg = 'black', width = 50, command = lambda: root.destroy()).pack()

root.mainloop()