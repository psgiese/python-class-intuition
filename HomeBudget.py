import numpy as np
import pandas as pd
import datetime
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

image_format = "svg"  # e.g .png, .svg, etc.


class HomeBudget(object):
    """This is a class object for developing a personal home budget"""

    def __init__(self, income):
        """initialize a HomeBudget"""
        self.income = income
        self.calc_days = 30
        # if month_part = True:

    def __str__(self):
        """output a message stating the starting income for the budget"""
        return f"HomeBudget() will calculate my category allowances based off of {self.income} dollars of income this month."

    def change_to_partial(self):
        """Run HomeBudget for the remainder of the month"""
        x = datetime.datetime.now()
        x1 = datetime.datetime(x.year, x.month + 1, 1)
        dd = round((x1 - x) / pd.Timedelta(1, "d"))
        self.calc_days = dd
        print(
            f"HomeBudget() will calculate my category allowances based off of {self.calc_days} days left in the month."
        )

    def enter_bills(self, d):
        """User enters their bill amounts; store as dictionary; display breakdown in plot"""
        bill_name = list(d.keys())
        bill_amt = [amt / self.income for amt in list(d.values())]  # /self.income
        bills_data = pd.DataFrame.from_dict(
            {"bill_name": bill_name, "bill_amount": bill_amt}
        )
        bills_data.sort_values(by="bill_amount", ascending=False, inplace=True)

        fig, ax = plt.subplots(figsize=(1.618 * 8, 8))
        fig.suptitle("Bills as percent of income", fontsize=20)
        x = bills_data.bill_name.values
        y = bills_data.bill_amount.values
        ax.bar(x, y)
        plt.savefig("budget_bills.svg")
        print("Locate your plot in you working directory as budget_bills.svg")
        return bills_data

    # def responsibe_adult(self):

    # def select_from_categories(self):

    # plt.show()
    #     budget_cateogories=[]
    #     """ All the user to pick from x predefined categories """
    #     presets = ['Entertainment','Clothes','']


budget = HomeBudget(income=5000)
x = budget.enter_bills(
    {
        "Gas Heating": 60,
        "Electric": 84,
        "Water": 90,
        "Trash": 33,
        "Rent": 1750,
        "Car": 400,
        "Gas": 200,
    }
)
print(x)
# budget.change_to_partial()
# print(budget)
# print(budget.calc_days)

# class Goals(HomeBudget):
#     """ This function let's the user define their
