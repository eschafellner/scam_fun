#import request
import os
import random
import string
import json
import time

chars = string.digits or ""
random.seed = (os.urandom(1024))

names = json.loads(open('names.json').read())
#firstname list
nachname = json.loads(open('nachname.json').read())
#secondname list
vorwahl = json.loads(open("vorwahl.json").read())
#starting number list for telephone number
landvw = json.loads(open("landvw.json").read())
#country code list
maildom = json.loads(open("maildom.json").read())
#mail domain list
name_ext = json.loads(open("mail_ext.json").read())
#additinal characters for email adresse


url = ""
#insert target url here

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
            #adapt data fields as needed / as sent by the request
        #})    

    print("sending username %s and number %s and email %s" % (username, number, email))
    time.sleep(1)


