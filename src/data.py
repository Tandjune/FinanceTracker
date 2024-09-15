import pandas as pd
from datetime import datetime as dt
import csv


class CSV:
    csv_file = "../finance_data.csv"
    columns = ["date", "amount", "category", "description"]
    format = "%d/%m/%Y"

    @classmethod
    def create_file(self):
        try:
            pd.read_csv(self.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.csv_file, index=False)

    @classmethod
    def add_entry(self, date, amount, category, description):
        new = {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(self.csv_file, "a", newline="") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=self.columns)
            writer.writerow(new)
        print("New entry added successfully")

    @classmethod
    def filter_transactions(self, start_date, end_date):
        df = pd.read_csv(CSV.csv_file)
        df["date"] = pd.to_datetime(df["date"], format=self.format)
        start_date = dt.strptime(start_date, self.format)
        end_date = dt.strptime(end_date, self.format)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transaction found for the range!")
        else:
            print(f"\nTransaction(s) from the {dt.strftime(start_date, self.format)} to the {dt.strftime(end_date, self.format)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(self.format)}))

        total_income = filtered_df[filtered_df["category"] == "deposit"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"] == "withdraw"]["amount"].sum()
        print("\nSummary:")
        print(f"Total Income: {total_income:.2f}€")
        print(f"Total Expense: {total_expense:.2f}€")
        print(f"Nette saving: {(total_income - total_expense):.2f}€")

        return filtered_df

