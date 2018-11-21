import pandas as pd
import os
import unicodecsv as csv


emails = pd.read_csv('mccia.csv', names=['email_id'], skiprows=1,encoding="ISO-8859-1")

print("Total records in email input file ", emails.count())
print("\n\nFirst few records")
print(emails.head())

emails['domain'] = emails['email_id'].str.split('@').str[1]

print("\n\nSplitting address and domain")
print(emails.head())


print("\n\nDomain wise count..sample")

domain_count = emails.groupby('domain')['domain'].count()
print(domain_count.head())


print("kairee and aryan id count")
print("Kairee Count ",emails[emails['domain'].str.contains('kairee')].count())
print("Aryan Count ",emails[emails['domain'].str.contains('aibc')].count())


from validate_email import validate_email


validated_emails = open('./mccia_validated.csv','wb')    
output_writer = csv.writer(validated_emails, delimiter = "|", encoding='latin2')
print(emails.count())
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
        print(email," :Valid Address ",address," Valid Domain :",valid_domain," Email Exists : ",email_exists)

    except Exception as e:
        ()

validated_emails.close()



