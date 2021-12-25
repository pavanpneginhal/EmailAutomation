from email.message import EmailMessage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from email.mime.base import MIMEBase
from email import encoders

root = Tk()
root.title("Email Automation Tool")
root.geometry('960x640')

global toaddress

def SendMail(ImgFileName, toad):
    from_add = "pyprojmin@gmail.com"
    to = toad
    data = MIMEMultipart() 
    data['From'] = from_add
    data['To'] = toad
    data['Subject'] = "Thank you for the subscription!"
    body = "Hello Sir/Madam,thank you for your valuable subscription. Here is the picture of the day"
    data.attach(MIMEText(body, 'plain'))
    filename = "1.png"
    attachment = open(ImgFileName, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    data.attach(p)  
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_add, "1234554321AB!")
    text = data.as_string()
    s.sendmail(from_add, data["To"].split(","), text)
    messagebox.showinfo("showinfo", "Email Sent Successfully") 
    

def send():
  to_address = toaddress.get()
  if to_address == "":
    messagebox.showerror("Error", "Please fill To_Addresses") 
  else:
    SendMail('C:/Users/Pavan/Desktop/Email/kakashi1.jpg','C:/Users/Pavan/Desktop/Email/sasuke.jpg','C:/Users/Pavan/Desktop/Email/goku', to_address)

frame = Frame(root)
frame2 = Frame(frame)
font1 = font.Font(family='Verdana', size=40, weight='bold')
font2 = font.Font(family='Verdana', size=15)
font3 = font.Font(family='Verdana', size=15, weight='bold')
font4 = font.Font(family='Verdana', size=13)
photo = PhotoImage(file="C:\\Users\\Pavan\\Desktop\\Email\\1.png")
Label(frame, image=photo).pack(pady=15)
Label(frame, font=font1, text="Email Automation Tool").pack()
Label(frame, font=font2, text="Welcome to Email Automation Tool").pack(pady=20)
Label(frame, font=font2, text="Make sure you have stable Internet connection").pack(pady=10)
Label(frame, font=font3, text="To(Recipients)(Seperated by commas)", pady=15).pack(pady=10)
toaddress = StringVar()
Entry(frame2, width=60, font=font4, bg='#CFD4D2', textvariable=toaddress).grid(row=0, column=0, sticky='nsew')
Button(frame2, text='Send', font=font4, height=2, width=20, bg='#4EF8B4', command=send).grid(row=0, column=1, sticky='nsew', padx=15)
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)
frame2.pack(fill='x')
frame.pack()
root.mainloop()