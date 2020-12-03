import csv

#stores the csv data file location 
fileone = '/Users/Chibbbins/desktop/python-challenge/PyBank/Resources/Bank_Resources_budget_data.csv'

# opens the file
with open(fileone) as f:
    #separates data and assigns the data set to a variable
    csvreader = csv.reader(f, delimiter=',')
    #all calc skips header
    csv_header = next(csvreader)
    
    #varlaible asignments for calculations
    month_count = 0
    net_total = 0
    profit_losses = []
    changes = []
    Date = []
    
    #counts total months and creates lists contaning each colomn
    for row in csvreader:
        month_count += 1
        profit_losses.append(int(row[1]))
        Date.append((row[0]))
    
    #Calculates net total amount of Profit/Losses over the entire period    
    for a in profit_losses:
        
        net_total += a
    
    #Iterates through the dataframe calculating the change in profit/loss monthly
    for b in range(month_count-1):
        val1 = profit_losses[b]
        val2 = profit_losses[b + 1]
        
        changes.append(val2 - val1)
    
    #Calulates average change from the changes list and rounds to 2 decimals    
    average_change = str(round((sum(changes) / len(changes)), 2))         
    
    #Finds the highest profit and asigns it to a variable
    maximum = max(profit_losses)
    #Finds and returns the month asociated with the max profit and returns it to a varable 
    maxdate = profit_losses.index(maximum)
    maxdate = Date[(maxdate)]
    
    #Finds the lowest loss and asigns it to a variable
    minimum = min(profit_losses)
    #Finds and returns the month asociated with the lowest loss and returns it to a varable
    mindate = profit_losses.index(minimum)
    mindate = Date[(mindate)]
   
#Returns a formated analysis to the terminal
print("Fnancal Analysis\n--------------------------\nTotal Months: " + str(month_count) + 
      "\nTotal: $" + str(net_total) + "\nAverage Change: $" + str(average_change) + "\nGreatest Increase in Profits: " + 
      str(maxdate) + " ($" + str(maximum) + ")" + "\nGreatest Decrease in Profits: " + str(mindate) + " ($" + str(minimum) + ")")

#Exports a text file with the results
output_path = '/Users/Chibbbins/Desktop/python-challenge/PyBank/Analysis/analysis.txt'


with open("/Users/Chibbbins/Desktop/python-challenge/PyBank/Analysis/analysis.txt", "a") as f:

    print("Fnancal Analysis\n--------------------------\nTotal Months: " + str(month_count) + 
      "\nTotal: $" + str(net_total) + "\nAverage Change: $" + str(average_change) + "\nGreatest Increase in Profits: " + 
      str(maxdate) + " ($" + str(maximum) + ")" + "\nGreatest Decrease in Profits: " + str(mindate) + " ($" + str(minimum) + ")", file = f)