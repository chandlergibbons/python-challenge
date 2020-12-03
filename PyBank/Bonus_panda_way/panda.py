import csv
import pandas as pd

#Imports the csv data file and converts it into a dataframe
fileone = '/Users/Chibbbins/desktop/python-challenge/PyBank/Resources/Bank_Resources_budget_data.csv'
file_one_df = pd.read_csv(fileone)

#Calculates the total number of months included in the dataset
index = file_one_df.index
total_months = len(index)

#Calculates net total amount of Profit/Losses over the entire period
total = file_one_df["Profit/Losses"].sum()

#Iterates through the dataframe calculating the change in profit/loss monthly
changes = []
for x in range(total_months - 1):
    val1 = (file_one_df.iloc[x][1])
    val2 = (file_one_df.iloc[x + 1][1])
    val3 = int(val1)
    val4 = int(val2)
    
    changes.append(val4 - val3)

#Calulates average change from the changes list and rounds to 2 decimals
average_change = str(round((sum(changes) / len(changes)), 2)) 

#Finds the highest profit and asigns it to a variable
maximum = int(file_one_df["Profit/Losses"].max())
#Finds and returns the month asociated with the max profit and returns it to a varable 
maxdate = file_one_df['Date'].where(file_one_df['Profit/Losses'] == maximum).dropna().values[0]

#Finds the lowest loss and asigns it to a variable
minimum = file_one_df["Profit/Losses"].min()
#Finds and returns the month asociated with the lowest loss and returns it to a varable
mindate = file_one_df['Date'].where(file_one_df['Profit/Losses'] == minimum).dropna().values[0]

#Returns a formated analysis to the terminal
print("Fnancal Analysis\n--------------------------\nTotal Months: " + str(total_months) + 
      "\nTotal: $" + str(total) + "\nAverage Change: $" + str(average_change) + "\nGreatest Increase in Profits: " + 
      str(maxdate) + " ($" + str(maximum) + ")" + "\nGreatest Decrease in Profits: " + str(mindate) + " ($" + str(minimum) + ")")


#Exports a text file with the results
output_path = '/Users/Chibbbins/Desktop/python-challenge/PyBank/Analysis/analysis.txt'


with open("/Users/Chibbbins/Desktop/python-challenge/PyBank/Analysis/analysis.txt", "a") as f:

    print("Fnancal Analysis\n--------------------------\nTotal Months: " + str(total_months) + 
      "\nTotal: $" + str(total) + "\nAverage Change: $" + str(average_change) + "\nGreatest Increase in Profits: " + 
      str(maxdate) + " ($" + str(maximum) + ")" + "\nGreatest Decrease in Profits: " + str(mindate) + " ($" + str(minimum) + ")", file = f)
