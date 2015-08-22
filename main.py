__author__ = 'h1py'


import os
import praw

r = praw.Reddit(user_agent='pushq')

submissions = r.get_subreddit('GetMotivated').get_top(limit=1)

for top in submissions:
     one = top.url
     title = top.title

one = one + "\n\n Sends the top post of r/Getmotivated at this time everyday."


#Import smtplib for the actual sending function
import smtplib

#Import the email modules we'll need
from email.mime.text import MIMEText


msg = MIMEText(one)
msg['Subject'] = '%s' % title
msg['From'] = "mymail@gmail.com"
msg['Reply-to'] = "mymail@gmail.com"
msg['To'] = "yourmail@gmail.com"



server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login('mymail@gmail.com','password')
server.sendmail('yourmail@gmail.com','mymail@gmail.com',msg.as_string())
server.close()