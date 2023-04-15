from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import GetParticipantsRequest
import csv
condition = True
my_filter = ChannelParticipantsSearch('')
offset = 0
all_participants = []
phone = input('please Enter your phone:')
user_id = input('please Enter your user_id:')
access_hash = input('please Enter your access_hash:')
with TelegramClient( phone, user_id , access_hash) as client:
    while condition:
        participants = client(GetParticipantsRequest(channel='Channel_Name',  offset= offset, filter = my_filter, limit=200, hash=0))
        
        all_participants.extend(participants.users)
        offset += len(participants.users)
        
        print(len(participants.users))
        
        if len(participants.users) < 1 :
            condition = False

with open("participants.csv", "w", encoding='UTF-8') as p:
    writer = csv.writer(p, delimiter=",", lineterminator="\n")
    writer.writerow(['first_name', 'last_name', 'username'])
    for mem in all_participants:
        writer.writerow([ mem.first_name, mem.last_name, mem.username])

#good luck :)




