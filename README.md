# python-challenge
For PyBank main.py:

I started by creating lists for each column (Date column is months[] and Profits/Loses column is profits_losses[]) and then a list for calculated values for the monthly change in profits/lossts (change_profitlosses[]). The list for change_months[] was created to keep a different list of the dates within the conditional loop in line 20.

I opened the csv using the DictReader so it could take the first row as the header.  Because of that, I had to make a flag variable so when I calculated the monthly change in profits/losses it would skip the first row/header because it is to start subtracting from the third row minus the second row to calculate the monthly change, as seen in the conditional loop.

The for loop in line 14 appends to the months list, converts the Profits/Losses column to an integer and appends it to the profits_losses list.

The conditional loop in line 20 appends to the change_months list, and subtracts the current row minus the previous row in Profits/Losses to calculate the monthly change.  Then it appends the value to the change_profitslosses list.  It ends with setting up for the next row.

The next section in lines 30-36, assigns the calculations needed to variables for more succint print statements later on.  I calculated the total months by getting the len() of the months list.  The total net profit is calculated by taking the sum() of the profits_losses list.  The average change in monthly change of profits/losses is calculated by taking the sum() of the change_profitslosses list and dividing it by len() of change_months list, and then it is rounded to 2 decimal places for currency.  The greatest increase and decrease in monthly changes is found by taking the max() and min(), respectively, of the change_profitslosses list.  Then I indexed those changes to find the months on which they occured.

For the print statements in lines 39-45, I wanted to avoid having to code 6 different print statements.  So I realized I could print a block f' string.

In lines 48-56, I printed the same block f'string and saved it to a new txt file that I created, opened, and closed within the code.


For PyPoll main.py:

I started similary and created empty lists for ballot[] and candidate[].

I opened the csv with Dictreader to read the headers.

In lines 10-13, I used a for loop to append to the ballot[] and candidate[] list and then calculate the total number of votes by getting the len() of the ballot[] list.

In lines 18-19, I used the set() function to create a set of the unique values in the candidate[] list so I could see the complete list of each unique candidate who received votes.  I converted the set() back to a list[] in cased I needed it again.  It turns out I did not.

In line 23, I used the value_counts() to count how many votes per candidate and made it into a Series.

In lines 28 and 29, I used the above series and converted it to a dataframe with reset index, and created new columns with summarized Candidate list "Candidate" and number of votes per candidate "Votes".  I converted the dataframe to lists for CandidateOutput and VoteOutput to quickly pinpoint which candidate got the most votes by using the max() and index() functions in lines 35-36.

I started my print statements in line 39.  Instead of typing ten different print statements, I used three block f'strings for my final output.  I included a for loop to print out the names, final percentages, and final vote count for each candidate.  I had to format the percentage value.  So instead of having to format it in three different print statements, I did the for loop using the range of the len() of the count_df and .loc for indexing.  I probably could have just done the three separate print statements, but I am trying to follow the guide of "if you have to do it three times or more, use a function".

In lines 55-69, I printed the same block f'strings and saved them to a new txt file that I created, opened, and closed within the code.