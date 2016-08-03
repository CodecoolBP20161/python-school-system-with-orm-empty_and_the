import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:

    def __init__(toaddr, subject, body, fromaddr="emptyandthe@gmail.com", password="0emptyandthe"):
        self.toaddr = toaddr
        self.subject = subject
        self.body = body

    def create_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = "Details"
        msg.attach(MIMEText(self.body, 'plain'))
        return msg

    def send_email(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fromaddr, self.password)
        msg = self.create_message()
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

email = Email("emptyandthe@gmail.com", "Valami", "Valamimás")
email.send_email
