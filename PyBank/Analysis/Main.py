#Let's get this party started by importing the main guests
import os
import csv

#Now we bring in the csv
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Let's read the csv
with open(budget_data_csv) as budget_data_file:

    budget_data_read  = csv.reader(budget_data_file, delimiter=',')

    budget_data_header = next(budget_data_read)

    row_count = 0

    for row in budget_data_read:

        row_count += 1

print(row_count)

#row_count2 = len(budget_data_csv)
#print(row_count2)    



