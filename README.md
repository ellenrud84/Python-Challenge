# Python Demo:
This demo is actually two mini demos of the use of Python scripts.  In some of these demos the datasets are quite large. This showcases one of the limits of Excel-based analysis. While our first instinct, is often to head straight into Excel, creating scripts in Python can provide us with more robust options for handling "big data".  The two demos are outlined in further detail below.

## Bank Analysis:
![Revenue](Images/revenue-per-lead.png)

A Python script for analyzing the financial records of a theoretical company to calculate the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period
  
In addition, the script both prints the analysis to the terminal and exports a text file with the results.

### Bank Data: 
A simple set of ficitonal financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

### Bank Results:
TODO: Add screenshot of results.

## Poll Analysis

![Vote Counting](Images/Vote_counting.png)

This demo is aimed at helping a small, rural town modernize its vote counting process.
The Python script analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.
  
The script both prints the analysis to the terminal and exportd a text file with the results.

### Poll Data:
A fictional set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

### Poll Results:
TODO: Add screenshot of results.

  






