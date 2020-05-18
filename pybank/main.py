#import os and csv modules
import os
import csv

# #open file path (PyBank/Resources/budget_data.csv).
csvpath = os.path.join('Resources','budget_data.csv')
import csv
with open(csvpath, newline=' ') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #skip header row
    next(csvreader)
    print(csvreader)

    #initiate variables at zero
    sum_profit_loss= 0
    num_months =0
    pl_dict = {}

    print(pl_dict)

    #create for loop to run through the data
    for row in csvreader:
    #     #calculate the net total "Profit/Losses"  over the entire period, by adding the second item of each row in variable sum_profit_loss
    #     sum_profit_loss=sum_profit_loss+ row[1] 
    #     #calculate the total number of months included in the dataset, by adding one for every row counted, as each row is a new month
    #     num_months= num_months+1
    #     print(f'Sum profit and loss is: {sum_profit_loss}')
    #     #determine the change in profit loss for each period
        pl_dict.append(row)
        print(pl_dict)
   
   
    
    # #calculate each change in the "Profit/Losses" data as list change_profit_loss.  Take the average of these changes over the entire period.
    # #calculate the greatest increase in profits (date and amount) over the entire period
    # #print out the total number of months in the period
    # print(f'number of months is:{num_months}')
     