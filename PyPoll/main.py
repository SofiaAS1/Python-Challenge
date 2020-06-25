#Let's get this party started by importing the main guests
import os
import csv
import collections

#Now we bring in the csv
election_data_csv = os.path.join('Resources', 'election_data.csv')

#Let's read the csv
with open(election_data_csv) as election_data_file:
    
    #Read the csv
    election_data_read  = csv.reader(election_data_file, delimiter=',')
    
    #Skip the header
    election_data_header = next(election_data_read)

    election_data = [row for row in election_data_read]

    #Set Up the Variables
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    row_count = len(election_data)
    unique_can = set()

    #set up the loop & if statements...
    for row in election_data:
        unique_can.add(row[2])
        candidate = row[2]
        if candidate == 'Khan':
            khan += 1
        if candidate == 'Correy':
            correy += 1
        if candidate == 'Li':
            li += 1
        if candidate == "O'Tooley":
            otooley += 1

#Get my percent calculations & then round them off to 3 decimal pts
khan_p = (khan / row_count) * 100
khan_prcnt = round(khan_p, 3)
correy_p = (correy / row_count) * 100
correy_prcnt = round(correy_p, 3)
li_p = (li / row_count) * 100
li_prcnt = round(li_p, 3)
otooley_p = (otooley / row_count) * 100
otooley_prcnt = round(otooley_p, 3)

#Calculate the winner...
win = {khan : "Khan", correy : "Correy", li : "Li", otooley : "OTooley"}
winning = max(win)
winner = win.get(winning)
               
#Print out the Results   
print("Election Results")
print("-------------------------------")
print("Total Votes: " + str(row_count))
print("-------------------------------")
print(f"Khan: {khan_prcnt}00% ({khan})")
print(f"Correy: {correy_prcnt}00% ({correy})")
print(f"Li: {li_prcnt}00% ({li})")
print(f"O'Tooley: {otooley_prcnt}00% ({otooley})")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")
#print(list(unique_can))

#Output to txt file
f = open('Analysis/ElectionResults.txt', 'w')
f.write("Election Results\n")
f.write("-------------------------------\n")
f.write("Total Votes: " + str(row_count) + "\n")
f.write("-------------------------------\n")
f.write(f"Khan: {khan_prcnt}00% ({khan})\n")
f.write(f"Correy: {correy_prcnt}00% ({correy})\n")
f.write(f"Li: {li_prcnt}00% ({li})\n")
f.write(f"O'Tooley: {otooley_prcnt}00% ({otooley})\n")
f.write("-------------------------------\n")
f.write(f"Winner: {winner}\n")
f.write("-------------------------------\n")
f.close()