import smtplib
from talk import talk, talkG
# import speech_recognition as sr
# import pyttsx3
from email.message import EmailMessage
import speechRecognize as sr


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('hmpsproject.emailbot@gmail.com', 'Python@123')
    email = EmailMessage()
    email['From'] = 'hmpsproject.emailbot@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'rohan': 'haburohan@gmail.com',
    'satyam': 'morankarsatyam@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = sr.listen()
    try:
        receiver = email_list[name]
        print(receiver)
        talk('What is the subject of your email?')
        subject = sr.listen()
        talk('Tell me the text in your email')
        message = sr.listen()
        send_email(receiver, subject, message)
        talk('Your email is sent successfully')
        talk('Do you want to send more email?')
    except:
        talk('I could not find any email in the list given by you.')
    send_more = sr.listen()
    send_more = send_more.lower()
    if 'yes' in send_more:
        get_email_info()
    else:
        talk('Thank you Sir for using my automatic mail service, See you again !!')

# get_email_info()
