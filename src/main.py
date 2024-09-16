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
            while res not in ["y", "n"]:
                res = input("Do you want to see a plot? (y/n): ").lower()
                if res == "y":
                    utils.CSV.plot_transactions(df)
        elif choice == "3":
            break
        else:
            print("choose between a number from '1' to '3'")

if __name__ == "__main__":
    app()
