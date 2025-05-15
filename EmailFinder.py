import pandas as pd

file1 = pd.read_csv('EmailList(1).csv') #sets file1 to the first csv file containing the emails of all profiles
file2 = pd.read_csv('VolunteerList.csv') #sets file2 to the second csv file containing the list of available volunteer information

emails_file1 = set(file1['textBox1'].str.lower().str.strip()) #cleans the file by removing all whitespace and converting all emails to lowercase 
emails_file2 = set(file2['email '].str.lower().str.strip()) #cleans the file by removing all whitespace and changing the email column to lowercase. 

matched_emails = emails_file1.intersection(emails_file2) #finds the intersection/matching emails between file1 and file2 aka the emails of both profile holders and volunteers. 

unmatched_emails = emails_file2 - matched_emails #uses the email column from file2 to find unmatched emails by subtracting the already matched emails from that list.


matched_list = pd.DataFrame({'Email': list(matched_emails), 'Status': 'Matched'}) # creates list of matched emails

unmatched_list = pd.DataFrame({'Email': list(unmatched_emails), 'Status': 'Unmatched'}) # creates list of unmatched emails

matched_df = pd.concat([matched_list, unmatched_list], ignore_index = True)  #concatenates the two dataframes matched & unmatched emails
 

#matched_df = pd.DataFrame(list(matched_emails), columns = ['Matched Emails'])

# used this to create a list of single column of matched emails comment lines 12 - 15 to create a list of matched emails// originally used in task. 

matched_df.to_csv('Matched_emails1.csv', index = False)
#changed the name of the file to Matched_emails1 to avoid overwriting the original file...turns out I had that file open in excel and was unable to save it.

print(f'Found {len(matched_emails)} matching emails. \n Found {len(unmatched_emails)} unmatched emails \n Results saved to Matched_emails.csv')