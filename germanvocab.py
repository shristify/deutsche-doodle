#code for German vocab below
import time
import os
import random
from twilio.rest import Client 
import csv
import schedule
from messenger import *

import re
str= open('german.txt','r').read().replace('\n','  ')
one=re.findall(r'\([^\(\)]*\)', str)

def german():    
    message = client.messages.create( 
                     from_=twi,  
                        to=me,
                          body=(one[random.randint(0,len(one)-1)])
                          )
    print(message.sid)

schedule.every(1).minute.do(german)

while True:
    schedule.run_pending()
    time.sleep(1)

#with open('german.txt') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter='@')
#    for row in csv_reader:
#         one.append(row)
