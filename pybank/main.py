#import modules
import os
import csv

#name file path for reference file
csv_path = os.path.join("Resources", "budget_data.csv")

#create a pandas dataframe from the filepath
with open (csv_path, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    #initiate variables based on zero
    change_list= []
    date_list = []
    sumchange=0
    greatest_increase=[" ",0]
    greatest_decrease=[" ",0]

    #store header
    header= next(csvreader)

    #store 1st row
    firstrow= next(csvreader)

    #initiate variables that are based off of the first row
    months=1
    total_pl= int(firstrow[1])
    prev_month=int(firstrow[1])

    #iterate
    for row in csvreader:
        #determine number of months
        months+=1
        #determine sum all profits and losses
        total_pl +=int(row[1])
        #determine month to month change
        change= (int(row[1])-prev_month)
        #add month to month change to total of the changes
        sumchange+= change
        #set this months value as previous month for next iteration
        prev_month= int(row[1])
        #add the monthly change to the list of monthly changes
        change_list += [change]
        #add the date of current iteration to the list of dates
        date_list += [row[0]]

        #determine greatest increase
        if change > greatest_increase[1]:
            greatest_increase[0]= row[0]
            greatest_increase[1]= change

        #determine greatest decrease
        if change<greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

    #determine average change in profits and losses
    avgchange=sumchange/(months-1)

    #create header info for summary table
    header = "```text \nFinancial Analysis \n ----------------------------"

    #outputs: Total number of months, Sum of Profit/ Loss, Average change in profit/loss
    # Maximum Increase in profits, Maximum decrease/ losses

    summary = (f'{header}\nTotal Months: {months} \nTotal: ${total_pl} \nAverage  Change: ${avgchange} \nGreatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]}) \nGreatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})\n```')
    print(summary)

#specify path for export
output_path = os.path.join("analysis", "PyBankSolution.txt")

# export
with open(output_path, 'w') as txtfile:
     txtfile.write(summary)
     txtfile.close()