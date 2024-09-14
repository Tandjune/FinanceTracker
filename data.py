import pandas as pd
import csv


class CSV:
    csv_file = "finance_data.csv"
    columns = ["date", "amount", "category", "description"]

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


CSV.create_file()