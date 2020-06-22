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

    total_amt = 0

    for row in budget_data_read:

        row_count += 1
        total_amt +=int(row[1])
   
print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(total_amt))



    

    






#row_count2 = len(budget_data_csv)
#print(row_count2)    



