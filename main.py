from tkinter import *
from functools import partial
import random
from talk import talk, talkG
import speechRecognize as sr
from voiceAssistant import Assistant
import json
from twilio.rest import Client

main_window = Tk()
main_window.geometry('500x200')
main_window.title('PYTHON PROJECT')
main_window.config(bg='#0B5A81')
f = ('Times', 14)
Frame(
    main_window,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
).pack()
Label(main_window, text="Select the login method", font=f).pack()


def otp():
    for widget in main_window.winfo_children():
        widget.destroy()
    Label(main_window, text="You had chosen otp method, Welcome", font=f).grid(row=5, column=0)
    Label(main_window, text="click to send otp", font=f).grid(row=6)

    def send():
        for widget in main_window.winfo_children():
            widget.destroy()
        otp = random.randint(1000, 9999)

        account_sid = 
        auth_token = 
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='Hello! Your OTP is: ' + str(otp) + '\nDo not share with anyone.',
            from_=,
            to=
        )

        print("OTP Sent Successfully")
        Label(main_window, text="Enter OTP", font=f).grid()
        otpno = StringVar()
        Entry(main_window, textvariable=otpno, font=f).grid(row=0, column=1)

        def login_otp():
            for widget in main_window.winfo_children():
                widget.destroy()

            def Run():
                for widget in main_window.winfo_children():
                    widget.destroy()
                Label(main_window, text="working......", font=f).grid()
                while (1):
                    Assistant()

            if int(otpno.get()) == otp:
                for widget in main_window.winfo_children():
                    widget.destroy()
                Label(main_window, text="you are Logged in", font=f).grid()
                Button(main_window, text="RUN", command=Run, font=f).grid(row=1, column=0)
                return
            Label(main_window, text="failed", font=f).grid()

        Button(main_window, text=" login ", command=login_otp, font=f).grid(row=7)

    Button(main_window, text="Send OTP", command=send, font=f).grid(row=7)


def pass_login():
    for widget in main_window.winfo_children():
        widget.destroy()

    def run():
        for widget in main_window.winfo_children():
            widget.destroy()
        Label(main_window, text="ready to run", font=f).grid()
        while (1):
            Assistant()

    def validateLogin(username, password):
        if username.get() == "ni" and password.get() == "90":
            for widget in main_window.winfo_children():
                widget.destroy()
            Label(main_window, text="logged in", font=f).grid()
            Button(main_window, text="RUN", command=run, font=f).grid(row=1, column=0)
            return
        Label(main_window, text="login failed retry", font=f).grid(row=6)

    usernameLabel = Label(main_window, text="User Name", font=f).grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(main_window, textvariable=username, font=f).grid(row=0, column=1)

    # password label and password entry box
    passwordLabel = Label(main_window, text="Password", font=f).grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(main_window, textvariable=password, show='*', font=f).grid(row=1, column=1)

    validateLogin = partial(validateLogin, username, password)

    # login button
    loginButton = Button(main_window, text="Login", command=validateLogin, font=f).grid(row=4, column=0)


Button(main_window, text="otp", command=otp, font=f).pack()
Button(main_window, text="Pass login", command=pass_login, font=f).pack()
main_window.mainloop()
