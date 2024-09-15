import data as data
import input_data as inda

def add():
    data.CSV.create_file()
    date = inda.get_date()
    amount = inda.get_amount()
    category = inda.get_category()
    description = inda.get_description()
    data.CSV.add_entry(date, amount, category, description)

def filter():
    start_date = input("Give the start date: ")
    end_date = input("Give the end date: ")

    data.CSV.filter_transactions(start_date, end_date)

def app():
    while True:
        print("\n1. Add a new transaction")
        print("2. Filter the transaction with a start- and end-date")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice =="2":
            filter()
        elif choice == "3":
            break
        else:
            print("choose between a number from '1' to '3'")

if __name__ == "__main__":
    app()






    

