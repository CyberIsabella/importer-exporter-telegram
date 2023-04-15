# importer-exporter-telegram
Telegram importer and exporter tool that offers more and more diverse features than other similar tools

## how to setup

```
+ git clone https://github.com/CyberIsabella/importer-exporter-telegram
+ pip install telethon
+ you need to log in to My.telegram.org to get the api-id and api-hash and fill in the config.json file. In addition, multiple accounts can be placed in the config.json file   

```

![Screenshot 2023-04-15 051748](https://user-images.githubusercontent.com/122454821/232224277-a27b74f1-95c4-445c-af73-51a98282bf6d.png)


## initial
In order to activate our session and log in, we need to type the following command:
`python init_session.py`
After this command, it will log in all the accounts you have entered in config.json

## exporter
First of all, it should be noted that naturally, only users who are in groups and supergroups can be extracted, because channel users can only be seen by the admin and the creator of the channel, and no one else has access to it.

### from group
+ `python   get_data.py`

### from channel
If we were the admin or creator of the channel, we can get the information of the members of that channel. For this, we first enter the name of the channel in the get_channel.py code (in the channel=' ' section)
after that we run it:

+ `python get_channel.py`

![cha](https://user-images.githubusercontent.com/122454821/232224369-d18a62b3-c175-4598-ad4b-949d94e04948.png)


The saved information is stored in the data folder and This information is divided into two parts:

**groups:** Inside the json file that is in the data-->group section, the id and name of all groups and channels are located based on each account (phone number).

**users:** Every json file that is in the data-->user section contains the information of the users of the same group. The files are categorized based on the id of the groups and inside each file there is an id, access_hash, the last date of being online and most importantly, the username of each person.

![ddddd](https://user-images.githubusercontent.com/122454821/232224309-3e7f4fd4-a1a5-49a0-8786-3143d0dd04af.png)

## importer

If we act in the normal way, the user information is located in the data  user section and is specified based on the id of each group. To add, we go to the config.json section and in the group_target section we put the ID of the group or channel in which we want to add users, and in the group_source section we put the ID of the group or channel from which we got the people's information. (this id can be obtained from the data-->group section)

+ `python  add_member.py`

![final](https://user-images.githubusercontent.com/122454821/232224411-5604c3dc-6430-4c40-b655-5f0a16d95b00.png)





