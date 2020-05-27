#import modules
import os
import csv
import numpy as np
import pandas as pd

#name file path for reference file
budget_csv = os.path.join("Resources", "budget_data.csv")

#create a pandas dataframe from the filepath
budget_file=pd.read_csv(budget_csv).astype({"Date":object, "Profit/Losses":float})

#determine the number of months in the report
num_month= budget_file["Date"].count()

#determine the sum of the profits/losses
sum_pl= round(budget_file["Profit/Losses"].sum(),2)

#define a data series for change in profit and loss from the budget_file
delta_ds=budget_file["Profit/Losses"].diff()

#determine average change in profits and losses
avg_delta= round(delta_ds.mean(),2)

#pull the dates column out of the budget file into its own dataseries
dates_ds=(budget_file["Date"])

#make a new dataframe from the delta_ds series and the dates_ds data series
delta_dates_df = pd.concat([dates_ds, delta_ds],axis= 1).astype({"Date":object, "Profit/Losses":float})

#determine max increase in profits and associated date
max_delta= delta_dates_df.max()
max_delta_date = max_delta[0]
max_delta_dollars= max_delta[1]

#determine min decrease in losses
min_delta = delta_dates_df.min()
min_delta_date= min_delta[0]
min_delta_dollars = min_delta[1]

#create header info for summary table
header = "\'\'\'text \nFinancial Analysis \n__________________________________________"

#outputs: Total number of months, Sum of Profit/ Loss, Average change in profit/loss
# Maximum Increase in profits, Maximum decrease/ losses

summary = (f'{header}\nTotal Months: {num_month} \nTotal: ${sum_pl} \nAverage  Change: ${avg_delta} \nGreatest Increase in Profits: {max_delta_date}, (${max_delta_dollars}) \nGreatest Decrease in Profits: {min_delta_date} (${min_delta_dollars})\n\'\'\'')
print(summary)

#specify path for export
output_path = os.path.join("analysis", "PyBankSolution.txt")

#export
with open(output_path, 'w') as txtfile:
    txtfile.write(summary)
    txtfile.close()