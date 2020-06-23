#Let's get this party started by importing the main guests
import os
import csv

#Now we bring in the csv
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Now we create a list for our net change
net_change_list=[]

#Let's read the csv
with open(budget_data_csv) as budget_data_file:
    
    #Read the csv
    budget_data_read  = csv.reader(budget_data_file, delimiter=',')
    
    #Skip the header
    budget_data_header = next(budget_data_read)

    #Set our 1st 2 variables to 0
    row_count = 0
    total_amt = 0

    #Set up variables for net change (to calc avg)
    first_row = next(budget_data_read)
    prev_net = int(first_row[1])

    #set up the loop...
    for row in budget_data_read:
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change) 
        prev_net = int(row[1])
        row_count += 1
        total_amt +=float(row[1])
       
#Formulate the net change average
average = sum(net_change_list) / row_count

#Print out the Results   
print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(total_amt))
print("Average Change: $" + str(round(average, 2)))


