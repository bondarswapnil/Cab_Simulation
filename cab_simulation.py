'''
Author - Swapnil Bondar
Description - Console Based application for ride booking.
              Integrated with Bill generation with auto E-mail sending.
              
Date - 29-12-2022
'''
from fpdf import FPDF
from texttable import Texttable
from datetime import datetime
from datetime import date 
import random

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    pdf = FPDF()
    pdf.add_page()

    subject = "Bill For Uber Application"
    body = "************* -----Uber----- ****************"
    sender_email = "bondarswapnil@gmail.com"
    password = "#"

    print("\n****** Welcome To Uber Services ******")
    print("------------------------------------")
    print("|  Promo Code : 20% off on NEWBIE  |")
    print("------------------------------------")
    print("\n*********** Vehicle Available ***********")

    
    dte = date.today()
    nowt = datetime.now()
    tme = nowt.strftime("%H:%M:%S")
    rde = random.randint(111111,999999)

    #code for tabular format
    t = Texttable()
    t.add_rows([['Sr No','Car type','capacity','Rate'],
                ['1','Mini','4','Rs.20/km'],['2','Big','7','Rs.25/km'],['3','Sedan','5','Rs.50/km']])
    print (t.draw())

    print("------------------------------------")
    print("|  Promo Code : 20% off on NEWBIE  |")
    print("------------------------------------")

    print("\n********* Avaialble Routes *********")

    y = Texttable()
    y.add_rows([['Sr. No','Available Routes'],['1','Swargate - Kothrud'],['2','Kothrud - Swargate'],
                ['3','Kothrud - Baner'],['4','Baner - Kothrud'],['5','Kothrud - Warje'],
                ['6','Warje- Kothrud'],['7','Katraj - Deccan'],['8','Deccan - Katraj'],
                ['9','Warje - Katraj'],['10','Katraj - Warje']])
    print(y.draw())

    routes = {'KOTHRUD-SWARGATE' : 20 , 'SWARGATE-KOTHRUD' : 20,
                'KOTHRUD-BANER': 15,'BANER-KOTHRUD':15,
                'KOTHRUD-WARJE': 7,'WARJE-KOTHRUD':7,
                'KATRAJ-DECCAN':10,'DECCAN-KATRAJ':10,
                'WARJE-KATRAJ':16,'KATRAJ-WARJE':16}

    vehicles = {'1': 'Mini' , '2': 'Big' , '3' : 'Sedan' }

    fare = {'1':20,'2':25,'3':50}

    source = input("Enter Source : ")
    source_upper = source.upper()
    destination  = input("Enter Destination : ")
    destination_upper = destination.upper()
    ctype = input("1} Mini\n2} Big\n3} Sedan\nEnter Vehicle Type in 1,2,3 : ")

    route_to_find = source_upper + "-" + destination_upper
    base_fare = fare[ctype]*routes[route_to_find]

    if route_to_find in routes.keys() and ctype in fare.keys():
        print(f"Distance Between {source} and {destination} is {routes[route_to_find]} and chosen vehicle {vehicles[ctype]}")
        print(f"Base Fare : Rs.{base_fare}")
        yn = input("Enter Yes to Book Ride : ")
        yn_lower = yn.lower()
        if yn_lower=='yes':
            name = input("Enter your Name :")
            gemail = input("Enter your E-mail ID : ")
            mob = input("Enter Your Mobile Number : ")
            print(f"Thanks For booking Ride With us {name}")
            print("Driver Will come to Pick you up soon !")
            promo_code = input("Do you want to enter Promo Code (Yes/No) : ")
            promo_code_lower = promo_code.lower()
            if promo_code == 'yes':
                pdf.set_font('helvetica', size=25)
                pdf.cell(w=0,h=5,txt = "************************ Uber Ride Receipt ***********************",align="C",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.set_font('helvetica', size=20)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* Ride No : {rde}",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* Date : {dte}          Time : {tme}",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* Passenger Name : {name}",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* Passenger Email-ID : {gemail}",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* Passender Mobile Number : {mob}",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* Base Fare : Rs.{base_fare}",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* Total Fare {base_fare} without promo",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* Total Fare : Rs.{(base_fare+((base_fare*0.09)+(base_fare*0.09)))-(base_fare*0.20)}",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* `Includes 9% CGST and 9%SGST (T&C)`",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt=f"* Thanks For Riding with Us")
                pdf.cell(txt="  ",ln=1)
                pdf.output(f"RideBill.pdf")
                
            else:
                pdf.set_font('helvetica', size=25)
                pdf.cell(w=0,h=5,txt = "************************ Uber Ride Receipt ***********************",align="C",ln=1)
                pdf.cell(txt="  ",ln=1)
                pdf.set_font('helvetica', size=20)
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt = f"* Ride No : {rde}")
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt = f"* Date : {dte}          Time : {tme}")
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt = f"* Passenger Name : {name}")
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt = f"* Passenger Email-ID : {gemail}")
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt = f"* Passender Mobile Number : {mob}")
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt = f"* Base Fare : Rs.{base_fare}")
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt = f"* Total Fare : Rs.{(base_fare+((base_fare*0.09)+(base_fare*0.09)))}")
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt = f"* `Includes 9% CGST and 9%SGST (T&C)`")
                pdf.cell(txt="  ",ln=1)
                pdf.cell(txt = f"* Thanks For Riding with Us")
                pdf.cell(txt="  ",ln=1)
                pdf.output(f"RideBill.pdf")
        else:
            print("Ride Cancelled !")
    else:
        print(f"Route {source} and {destination} not avialable !")
    
    
    receiver_email = gemail
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    filename = f"RideBill.pdf" 

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
  
    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",)

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text) 

    print("Email sent Successfully")
    
except BaseException as ex:
    print(ex)
    