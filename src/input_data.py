from datetime import datetime as dt
import calendar as cl


date_format = "%d/%m/%Y"
x = lambda:dt.now().strftime(date_format)
categories = { "d": "deposit", "w": "withdrawal"}

def get_date(prompt = "", type = ""):
    
    date_str = input(prompt)
    if not date_str:
        return dt.today().strftime(date_format)
    
    date = check_date_format(date_str, type)
    res = date if date else get_date(prompt, type)
    return res

def get_amount():
        try:
             amount = float(input("Give the amount of the transaction: "))
             if amount > 0:
                return amount
             raise ValueError()
        except ValueError :
            print("The amount must be greater than 0 and must only contain digits between 0 and 9")
            return get_amount()

def get_category():
        cat = input("What type of transaction? Deposit (d) or Withdrawal (W): ").lower()
        
        if cat in categories:
             return categories[cat]
        print("The type of transaction should be: 'd' or 'w' " )
        return get_category()

def get_description(txt = " "):
     txt = input("Give a discription of the transaction or just press Enter: ")
     return txt

def check_date_format(date, type):
    
    try:
        if len(date) == 4:
             date = f"01/01/{date}" if type == "start" else f"31/12/{date}"
        if len(date) == 7:
            tmp = date.split("/")
            try:
                 last_day = cl._monthlen(int(tmp[1]), int(tmp[0]))
                 date = f"01/{date}" if type == "start" else f"{last_day}/{date}"
            except IndexError:
                 raise ValueError()
        valide_date = dt.strptime(date, date_format)
        return valide_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in this format: dd/mm/yyyy or mm/yyyy or yyyy")
        return ""
    
def get_filter_date():
     prompt = "Give the start date: "
     date = get_date(prompt, "start")
     start_date = date if date else get_date(prompt)
     prompt = "Give the end date: "
     date = get_date(prompt)
     end_date = date if date else get_date(prompt)

     return (start_date, end_date)
     
