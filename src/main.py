import utils
import input_data as inda

def add():
    prompt = "Give the date of the transaction (format: dd/mm/yyyy) or press Enter to use today's date: "

    utils.CSV.create_file()
    date = inda.get_date(prompt)
    amount = inda.get_amount()
    category = inda.get_category()
    description = inda.get_description()
    utils.CSV.add_entry(date, amount, category, description)

def filter():
    dates = inda.get_filter_date()

    return utils.CSV.filter_transactions(dates[0], dates[1])

def app():
    while True:
        print("\n1. Add a new transaction")
        print("2. Filter the transaction with a start- and end-date")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice =="2":
            df = filter()
            res = ""
            while res not in ["1","2","3","4"]:
                print("\nDo you want to see the figure(s) of the Transactions? ")
                print("1. The line chart of the ")
                print("2. The bar chart")
                print("3. Both")
                print("4. None")

                res = input("Enter your choice (1-4): ").lower()
                if res in ["1","2","3"]:
                    utils.CSV.plot_transactions(df,res)
        elif choice == "3":
            break
        else:
            print("choose between a number from '1' to '3'")

if __name__ == "__main__":
    app()
