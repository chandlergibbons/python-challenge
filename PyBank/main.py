import csv

with open('Bank_Resources_budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for row in csv_reader:

        totalmonths += 1

        print(row[1])
        print(row[2])
        