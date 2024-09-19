import pandas as pd
from datetime import datetime as dt
import csv
import matplotlib.pyplot as plt
import numpy as np


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

        df = df.sort_values(by="date", key=lambda col: pd.to_datetime(col, "%Y%m%d"))
        # mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        # filtered_df = df.loc[mask]
        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        if filtered_df.empty:
            print("No transaction found for the range!")
        else:
            print(f"\nTransaction(s) from the {dt.strftime(start_date, self.format)} to the {dt.strftime(end_date, self.format)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(self.format)}))

        total_income = filtered_df[filtered_df["category"] == "deposit"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"] == "withdrawal"]["amount"].sum()
        print("\nSummary:")
        print(f"Total Income: {total_income:.2f}€")
        print(f"Total Expense: {total_expense:.2f}€")
        print(f"Nette saving: {(total_income - total_expense):.2f}€")

        return filtered_df
    
    @classmethod
    def plot_transactions(self, df, choice):
        df.set_index("date", inplace=True)

        if choice in ["1","3"]:
            income_df = (df[df["category"] == "deposit"].resample("D").sum().reindex(df.index, fill_value=0))
            expense_df = (df[df["category"] == "withdrawal"].resample("D").sum().reindex(df.index, fill_value=0)) 

            plt.figure(figsize=(10, 5))
            plt.plot(income_df.index, income_df["amount"], label="Deposit", color="g")
            plt.plot(income_df.index, expense_df["amount"], label="Withdrawal", color="r")
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.title("Deposits and Withdrawal over Time")
            plt.legend()
            plt.grid(True)

        if choice in ["2","3"]:
            df = df.reset_index()
            df2 = df.filter(["date","category", "amount"])
            df2["date"] = df2["date"].apply(lambda x: x.strftime('%m/%Y'))
            df2_income_filter = df2[df2["category"] == "deposit"].filter(["date", "amount"]).reset_index(drop=True)
            df2_expense_filter = df2[df2["category"] == "withdrawal"].filter(["date", "amount"]).reset_index(drop=True)


            df21 = df2_income_filter.groupby(["date"]).sum().reset_index().rename(columns={"amount": "deposit"})
            df22 = df2_expense_filter.groupby(["date"]).sum().reset_index().rename(columns={"amount": "withdrawal"})

            df3 = df21.merge(df22, how="outer", on="date").fillna(0)
            max_ob = df3.max()
            max_value = max(max_ob["deposit"], max_ob["withdrawal"])
            df3.set_index("date", inplace=True)
            df_dict = df3.to_dict()
            keys = df_dict["deposit"].keys()


            x = np.arange(len(keys)) 
            width = 0.25  
            multiplier = 0

            fig, ax = plt.subplots(layout='constrained')

            for category, i in df_dict.items():
                offset = width * multiplier
                rects = ax.bar(x + offset, i.values(), width, label=category)
                ax.bar_label(rects, padding=3)
                multiplier += 1

            ax.set_ylabel('Amount (€)')
            ax.set_xlabel('Date')
            ax.set_title('Transactions')
            ax.set_xticks(x + 0.12, keys)
            ax.legend(loc='upper left', ncols=3)
            ax.set_ylim(0, max_value + 700)

        plt.show()


