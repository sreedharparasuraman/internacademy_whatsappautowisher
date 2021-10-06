import pywhatkit

import webbrowser

import mysql.connector
import datetime
import os

now=str(datetime.date.today())

today = now[8:10]+now[5:7]
print(today)
con=mysql.connector.connect(host="localhost",user="root",password="password@4021",database="birthdays")
cur=con.cursor()
cur.execute(f"select*from data where bday={today}")
list1=cur.fetchall()
input("Press enter to start wish. Make sure to connect internet.")
for i in list1:
        a='+91'+i[2]
        b='Happy birthday to you'+i[0]
        pywhatkit.sendwhatmsg(a,b,00,00)
