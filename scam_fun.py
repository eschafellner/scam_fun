#Requirements:
#Pyhton 3.7
#Pip3
#Requests moduel (pip install requests)

#Remove comments to fully activate http requests (import request, request segment)"

#import request
import os
import random
import string
import json
import time

chars = string.digits
random.seed = (os.urandom(1024))

#data directory contains all list files

names = json.loads(open("data/names.json").read())
#firstname list
nachname = json.loads(open("data/nachname.json").read())
#secondname list
vorwahl = json.loads(open("data/vorwahl.json").read())
#starting number list for telephone number
landvw = json.loads(open("data/landvw.json").read())
#country code list
maildom = json.loads(open("data/maildom.json").read())
#mail domain list
name_ext = json.loads(open("data/mail_ext.json").read())
#additinal characters for email adresse


url = ""
#insert target url here
#example "http://etf-buy.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php"

while True:
    for name in names:
        name_extra = random.choice(name_ext)
        firstname = random.choice(names)
        secondname = random.choice(nachname)
        
        username = firstname + " " + secondname
        number = random.choice(landvw) + random.choice(vorwahl) + ''.join(random.choice(chars) for i in range(5))
        email = secondname.lower() + name_extra + "@" + random.choice(maildom)
        
        #requests.post(url, allow_redirects=False, data={
            #"Datafield name": username,
            #"Datafield number": number,
            #"Datafield email": email,
        #})    

        #adapt data field names as needed / as sent by the request and also provide the full request data

    print("sending username %s and number %s and email %s" % (username, number, email))
    time.sleep(1)


