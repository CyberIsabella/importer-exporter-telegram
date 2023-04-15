from telethon.sync import TelegramClient
from telethon import functions, types
import json
import os

#phone = input('please Enter your phone:')
#user_id = input('please Enter your user_id:')
#access_hash = input('please Enter your access_hash:')
#phone = ''
#user_id = 
#access_hash = ""

results = []

name = open('myusernames.txt', 'r', encoding='utf-8')
usernames = name.readlines()
number_usernames = len(usernames)
i = 0

with open('config.json', 'r', encoding='utf-8') as f:
    configdata = json.loads(f.read())

accounts = configdata['accounts']
for account in accounts:
    api_id = account['api_id']
    api_hash = account['api_hash']
    phone = account['phone']
    print(phone)
    with TelegramClient(phone, api_id , api_hash) as client:
        for x in range(number_usernames):
            result = client(functions.messages.GetPeerDialogsRequest(
                peers=[usernames[x]]
            ))
            tmp =  {
                    'user_id': str(result.users[0].id),
                    'access_hash': str(result.users[0].access_hash),
                    'username': str(result.users[0].username),
            }
            results.append(tmp)
            #.json file is sample and you can add custom number
            with open('data/user/' + phone + "_1111676426" '.json', 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=4, ensure_ascii=False)
            
    #////////////////////////////////////////////////////////////////////////////////////
    config = []
    tmp =  {
                'group_id': '1111676426',
                'access_hash': '-7184572535590939229',
                'title': 'group',
            }
    path_file = 'data/group/' + phone +  '.json'
    if os.path.isfile(path_file):
        with open('data/group/' + phone +  '.json', 'r', encoding='utf-8') as f:
            config = json.loads(f.read())
    config.append(tmp)
    with open('data/group/' + phone +  '.json', 'w', encoding='utf-8') as g:
        json.dump(config, g, indent=4, ensure_ascii=False)


#good luck :)