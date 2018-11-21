import win32com.client
import sys
import unicodecsv as csv

inbox_file_details = open('./inbox.csv','wb')    
output_writer_inbox = csv.writer(inbox_file_details, delimiter = "|", encoding='latin2')

sent_file_details = open('./sent.csv','wb')    
output_writer_sent = csv.writer(sent_file_details, delimiter = "|", encoding='latin2')

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. 
messages = inbox.Items

print("\n\nProcessing Inbox\n")
for i, message in enumerate(messages):              # enumerated the items
    try:

        sender = message.SenderName                 
        #sender_address = message.sender.address
        sender_address = message.SenderEmailAddress
        sent_to = message.To
        date = message.LastModificationTime         
        subject = message.subject                   

        output_writer_inbox.writerow([
            date,
            subject,
            sender, 
            sender_address,             
            sent_to]) 

    except Exception as e:
        ()

inbox_file_details.close()


## Sent items
sent_items = outlook.GetDefaultFolder(5) 

messages = sent_items.Items

print("\n\nProcessing Sent Items\n")
for i, message in enumerate(messages):               # enumerated the items
    try:

        sender = message.SenderName                 
        sender_address = message.senderEmailAddress         
        sent_to = message.To                    
        date = message.LastModificationTime         
        subject = message.subject                   

        output_writer_sent.writerow([
            date, 
            sender, 
            sender_address,             
            sent_to,
            subject]) 

    except Exception as e:
        ()

sent_file_details.close()

print("\n\nDone...!!!")
