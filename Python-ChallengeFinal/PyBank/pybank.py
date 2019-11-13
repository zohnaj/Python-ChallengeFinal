#Import Modules
import os
import csv

#Path to collect data & write data
budgetpath=os.path.join("Resources", "budget_data.csv")
output_budget=os.path.join("budget_write.txt")

#Define/set initial variable values
net_total=0
dates_change=[]
months_total=0
greatest_profit=0
greatest_loss=0
greatestprofit_date=""
greatestloss_date=""
average_change=0
change=0
previous_pl=0
first_pl=0
last_pl=0

#Read files & skip first row
with open(budgetpath, "r", newline='') as csvfile: 
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_reader= next(csvreader)
    

    #For loop to iterate each row & lineNum to check for the row number 
    for row in csvreader:
        lineNum=csvreader.line_num
        #If lineNum=2 then save first_pl variable value in row 1 else save last_pl variable as value in row 1 
        if lineNum==2:
                first_pl=int(row[1])
        else:
                last_pl=int(row[1])
        #Caclcuate number of months, net total, current_pl & change 
        dates_change.append(row[0])
        months_total=months_total+1
        net_total=net_total+int(row[1])
        current_pl=int(row[1])
        change=current_pl-previous_pl

        #Updating previous_pl to be equal to current_pl so it will hold the spot
        previous_pl=current_pl
        
        #Conditionals 
        if (change > greatest_profit):
                greatest_profit=change
                greatestprofit_date=str(row[0])

        if (change < greatest_loss):
                greatest_loss = change
                greatestloss_date=str(row[0])

#Calculate average change 
average_change=(last_pl-first_pl)/(months_total-1)
average_change=round(average_change, 2)
     

#Open output file to write
with open(output_budget, "w" ) as text_file: 

#Print Summary Table 
        print(" Financial Analysis")
        print("________________________________________")
        print(" Total Months: " + str(months_total))
        print(" Total: $ " + str(net_total))
        print(" Average Change: $ " + str(average_change))
        print(" Greatest Increase in Profits: $ " + str(greatestprofit_date) + " ($"  + str(greatest_profit) + ")")
        print(" Greatest Decrease in Profits: $ " + str(greatestloss_date) + " ($" + str(greatest_loss) + ")")

#Summary table to text format to output file
        text_file.write(" Financial Analysis \n")
        text_file.write("_______________________________ \n")
        text_file.write(" Total Months: " + str(months_total)+ "\n")
        text_file.write(" Total: $ " + str(net_total)+ "\n")
        text_file.write(" Average Change: $ " + str(average_change) + "\n")
        text_file.write(" Greatest Increase in Profits: " + str(greatestprofit_date) + " ($" + str(greatest_profit) + ")" "\n")
        text_file.write(" Greatest Decrease in Profits: " + str(greatestloss_date) + "($" + str(greatest_loss) + ")" "\n")