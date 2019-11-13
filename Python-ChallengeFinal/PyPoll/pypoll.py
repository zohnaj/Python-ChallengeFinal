#Import modules
import os
import csv

#Path to collect data & write result data
electionpath=os.path.join("Resources", "election_data.csv")
output_election=os.path.join("election_write.txt")


#Define Variables 
totalvotescast=0
candidates={}
percent_votes=0
winner_votes=0
totalvotes_candidates={}
winner=""

#Read files & skip first row
with open(electionpath, "r", newline="") as csvfile: 
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_reader=next(csvreader)
    
    #For loop to iterate through each row to get total number of votes by adding one to each time new row
    for row in csvreader:
        totalvotescast=totalvotescast+1
        candidate=(row[2])
        #Use conditional to determine if candidate is in candidates dictionary and if they are add to votes; if not equal to 1
        if candidate in candidates: 
            candidates[candidate]=candidates[candidate]+1
        else: 
            candidates[candidate]=1

with open(output_election, "w" ) as text_file:
    #Print format & write to text file
    print("Election Results")
    print("______________________")
    print("Total Votes: " + str(totalvotescast))
    print("___________________________")
    text_file.write(" Election Results \n")
    text_file.write("_______________________________ \n")
    text_file.write(" Total Votes: " + str(totalvotescast)+ "\n")

    #Loop through candidates in rows to get total number of votes per candidate & calculate percent of votes won for each    
    for candidate in candidates:
        totalvotes_candidates= candidates[candidate]
        percent_votes=round(totalvotes_candidates/totalvotescast*100,2)
        #Print using horizontal tab character to format print of candidates, percent of votes & total votes per candidate
        #Write to text file
        print(candidate + ':\t' + str(percent_votes) + "% (" + str(totalvotes_candidates) + ")")
        text_file.write(candidate + ':\t' + str(percent_votes) + "% (" + str(totalvotes_candidates) + ")" "\n")
   
    #Use conditional to retrieve winner
    # I had some issues with this getting it to print 
    if candidates[candidate] > totalvotes_candidates:
            totalvotes_candidates=candidates[candidate]
            winner=candidate

    #Print format & write to text file 
    print("Winner: " + winner)
    print("____________________________")
    text_file.write(" Winner: $ " + winner + "\n")
    
