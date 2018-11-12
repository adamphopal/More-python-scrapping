import csv
import smtplib
from settings import SENDER_EMAIL, SENDER_PASSWORD

ACCEPTED_MSG = """
Hi {},

You are accepted jabroni!!!

Your coach is {}.


"""

REJECTED_MSG = """
HI {},

We are sorry jabrni.

next time....
"""



with open('applications.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    smtp = smtplib.SMTP('smtp.gmail.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
                            
    for row in csv_reader:
        name, email, accepted, coach, language = row

        if accepted == "Yes":
            msg = ACCEPTED_MSG.format(name, coach)
            subject = "Accepted App"
        else:
            msg = REJECTED_MSG.format(name)
            subject = "Rejected"

        smtp.sendmail(SENDER_EMAIL, email, msg)

    smtp.quit()

        


        #print("Send e-mail to: {}".format(email))
        #print("E-main content:")
        #print(msg)
            



