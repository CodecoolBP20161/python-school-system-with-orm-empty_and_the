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
    def send_email(self, server):
        msg = self.create_message()
        text = msg.as_string()
        server.sendmail(self.fromaddr, self.toaddr, text)

    # Connect gmail server
    @classmethod
    def connect_server(cls):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(cls.fromaddr, cls.password)
        return server

    # Simpler method, older ones haven't changed because of older user strories
    def connect_and_send_email(self):
        server = Email.connect_server()
        self.send_email(server)
        Email.disconnect_server(server)

    # Disconnect gmail server
    @staticmethod
    def disconnect_server(server):
        server.quit()
