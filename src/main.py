import data as data
import input_data as inda


done = True
choice = {"y":True, "n":False}


def app():
    data.CSV.create_file()
    date = inda.get_date()
    amount = inda.get_amount()
    category = inda.get_category()
    description = inda.get_description()
    data.CSV.add_entry(date, amount, category, description)


def add_another():
    tmp = input("Do you want to add another transaction? Yes 'y' or No 'n': ").lower()
    if tmp in choice:
        return choice[tmp]
    raise ValueError()


while done:
    app()
    try:
       done = add_another()
    except ValueError:
        print("Choise between 'y' or ''n ")
        done = add_another()



    

