# Initial import statements
import csv
import os

#Variable Instatiation
monthCount=0
Total=0
incValue=0
decValue=0
avgTotal=0
prevAmt=0
currAmt=0
initPass=1
#CSV Path to read, home path
csvpath = os.path.join("budget_data.csv")
#Text file to write, home path
output_path = os.path.join("FinancialAnalysis.txt")

#define the read parameters for CSV
with open(csvpath, "r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    
    # Read each row of data after the header
    for row in csvreader:
        if initPass==1:
            initPass=2
            prevAmt=int(row[1])
            monthCount=monthCount + 1
            Total=Total+int(row[1])
            if int(row[1]) > incValue:
                incValue=int(row[1])
                incDate=row[0]
            if int(row[1]) < decValue:
                decValue=int(row[1])
                decDate=row[0]     
        else:
            #Running counter of months and for final average
            monthCount=monthCount + 1
            currAmt=int(row[1])
            avgTotal=avgTotal+currAmt-prevAmt
            prevAmt=currAmt
            #Running total 
            Total=Total+int(row[1])
            #Establish the largest increase value and dates
            if int(row[1]) > incValue:
                incValue=int(row[1])
                incDate=row[0]
            #Establish the largest decrease and dates
            if int(row[1]) < decValue:
                decValue=int(row[1])
                decDate=row[0]

#error checking for divisible by 0
if monthCount==0:
    average=0
else:
    average=avgTotal/(monthCount-1)


#Output to terminal
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(monthCount))
print("Total: " + str(Total))
print("Average Change: " + str("%.2f" % average))
print("Greatest Increase in Profits: " + incDate + " " + str(incValue))
print("Greatest Decrease in Profits: " + decDate + " " + str(decValue))

#Setup output file
file=open(output_path, "w")

#Output to file
file.write("Financial Analysis\n")
file.write("---------------------------\n")
file.write("Total Months: " + "(" + str(monthCount) + ")" + "\n")
file.write("Total: " + "(" + str(Total) + ")" + "\n")
file.write("Average Change: " + "(" + str("%.2f" % average) + ")" + "\n")
file.write("Greatest Increase in Profits: " + incDate + " " + "(" + str(incValue) + ")" + "\n")
file.write("Greatest Decrease in Profits: " + decDate + " " + "(" + str(decValue) + ")"+ "\n")

  



