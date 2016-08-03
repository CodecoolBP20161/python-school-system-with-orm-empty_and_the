import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:

    fromaddr = "emptyandthe@gmail.com"
    password = "0emptyandthe"

    def __init__(self, toaddr, subject, body):
        self.toaddr = toaddr
        self.subject = subject
        self.body = body

    # Create the body of the email
    def create_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))
        return msg

    # Send the email to the given email address
    def send_email(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fromaddr, self.password)
        msg = self.create_message()
        text = msg.as_string()
        server.sendmail(self.fromaddr, self.toaddr, text)
        server.quit()
