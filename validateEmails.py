import pandas as pd
import os
import unicodecsv as csv
from validate_email import validate_email


emails = pd.read_csv('benchmark_nobounce.csv', names=['email_id'], skiprows=1, encoding="ISO-8859-1")

print("Total records in email input file ", emails.count())
print("\n\nFirst few records")
print(emails.head())

emails['domain_'] = emails['email_id'].str.split('@').str[1]

print("\n\nSplitting address and domain")
print(emails.head())


print("\n\nDomain wise count..sample")

domain_count = emails.groupby('domain_')['domain_'].count()
print(domain_count.head())


print("kairee and aryan id count")
print("Kairee Count ",emails[emails['domain_'].str.contains('kairee')].count())
print("Aryan Count ",emails[emails['domain_'].str.contains('aibc')].count())


validated_emails = open('./benchmark_nobounce_validated.csv','wb')    
output_writer = csv.writer(validated_emails, delimiter = "|", encoding='latin2')
print(emails.count())
itr = 0

for email in emails.email_id:
    
    try:

        address = email
        valid_address = validate_email(email)
        valid_domain = validate_email(email,check_mx=True)
        email_exists = validate_email(email,verify=True)
                
        output_writer.writerow([
            address,
            valid_address,
            valid_domain, 
            email_exists])
        print(email,"\t"," :Valid Address ",valid_address,"\tValid Domain : ",valid_domain,"\tEmail Exists : ",email_exists)
        itr = itr+1
        print("\n\nProcessed ",itr," out of ",emails.count())

    except Exception as e:
        print("\nException occured for email id ",email)
        itr = itr+1
        print("\n\nProcessed ",itr," out of ",emails.count())
        
        
print("Processing done.. ")

validated_emails.close()
