from datetime import datetime as dt


date_format = "%d/%m/%Y"
x = lambda:dt.now().strftime(date_format)
categories = { "d": "deposit", "w": "withdraw"}

def get_date(prompt = ""):
    
    date_str = input(prompt)
    if not date_str:
        return dt.today().strftime(date_format)
    
    date = check_date_format(date_str)
    return date if date else get_date(prompt)

def get_amount():
        try:
             amount = float(input("Give the amount of the transaction: "))
             if amount > 0:
                return amount
             raise ValueError ()
        except ValueError :
            print("The amount must be greater than 0 and must only contain digits between 0 and 9")
            return get_amount()

def get_category():
        cat = input("What type of transaction? Deposit (d) or Withdraw (W): ").lower()
        
        if cat in categories:
             return categories[cat]
        print("The type of transaction should be: 'd' or 'w' " )
        return get_category()

def get_description(txt = " "):
     txt = input("Give a discription of the transaction or just press Enter: ")
     return txt

def check_date_format(date):
    
    try:
        valide_date = dt.strptime(date, date_format)
        return valide_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in this format: dd/mm/yyyy")
        return ""
    
def get_filter_date():
     prompt = "Give the start date: "
     date = get_date(prompt)
     start_date = date if date else get_date(prompt)
     prompt = "Give the end date: "
     date = get_date(prompt)
     end_date = date if date else get_date(prompt)

     return (start_date, end_date)
     
