import numpy as np
import pandas as pd
import datetime 

class HomeBudget(object):
    """ This is a class object for developing a personal home budget """
    
    def __init__(self, income):
        """ initialize a HomeBudget """
        self.income = income
        self.calc_days = 30
        #if month_part = True:
            
    
    def __str__(self):
        """ output a message stating the starting income for the budget"""
        return f"HomeBudget() will calculate my category allowances based off of {self.income} dollars of income this month."
    
    def change_to_partial(self):
        """ Run HomeBudget for the remainder of the month """
        x = datetime.datetime.now()
        x1 = datetime.datetime(x.year,x.month+1, 1)
        dd = round((x1-x)/pd.Timedelta(1, 'd'))
        self.calc_days = dd
        
        def __str__(self):
            return f"HomeBudget() will calculate my category allowances based off of {self.calc_days-dd} days left in the month."

           
budget = HomeBudget(income=5000)
print(budget)
budget.change_to_partial()
print(budget)
print(budget.calc_days)

# class Goals(HomeBudget):
#     """ This function let's the user define their 