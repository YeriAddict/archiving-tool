"""
    Class Mail
"""

import datetime
import json
import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Modules.log import add_to_log

DATE = datetime.datetime.now().date().strftime("%Y%d%m")
TIME = datetime.datetime.now().strftime("%H:%M:%S")

class Mail:
    """
        Class Mail
    """

    def __init__(self, config_file):
        """
        Attributes :
        --> username : Current session username
        --> password : Current session password
        --> machine_name : Arbitrary string
        --> server_name : Name of the computer
        --> ip : IP
        --> log_file : log file name
        """
        with open(config_file, encoding="utf8") as conf:
            data = json.load(conf)
            mail = data["mail"]
            archive = data["archive"]
        self.sender_adress = mail["sender_adress"]
        self.password = mail["password"]
        self.port = mail["port"]
        self.smtp_server = mail["smtp_server"]
        self.receiver_adress = mail["receiver_adress"]
        self.log_file = archive["log_file"]

    def send_email_ssl(self, body, subject):
        """
        Function sending emails using SSL
        --> body: body of the Email
        --> subject: subject of the Email
        """
        context = ssl.create_default_context()
        try:
            complete_message = MIMEMultipart()
            complete_message["From"] = self.sender_adress
            complete_message["To"] = self.receiver_adress
            complete_message["Subject"] = subject
            complete_message.attach(MIMEText(body, "plain"))
            text = complete_message.as_string()

            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
                server.login(self.sender_adress, self.password)
                server.sendmail(self.sender_adress, self.receiver_adress, text)
            line = ("[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Mail sent to "
            + self.receiver_adress)
            print(line)
            add_to_log(self.log_file, line)
        except smtplib.SMTPSenderRefused:
            line_one = "[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Sender adress refused"
            print(line_one)
            add_to_log(self.log_file, line_one)
        except smtplib.SMTPRecipientsRefused:
            line_two = "[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Receiver adress refused"
            print(line_two)
            add_to_log(self.log_file, line_two)
        except smtplib.SMTPConnectError:
            line_three = ("[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Connection with " +
            "server failed")
            print(line_three)
            add_to_log(self.log_file, line_three)
        except smtplib.SMTPAuthenticationError:
            line_four = ("[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Wrong username or " +
            "password")
            print(line_four)
            add_to_log(self.log_file, line_four)

    def send_email_ssl_with_log(self, body, subject):
        """
        Function sending emails using SSL with log.txt attached
        --> body: body of the Email
        --> subject: subject of the Email
        """
        context = ssl.create_default_context()
        try:
            complete_message = MIMEMultipart()
            complete_message["From"] = self.sender_adress
            complete_message["To"] = self.receiver_adress
            complete_message["Subject"] = subject
            complete_message.attach(MIMEText(body, "plain"))

            with open(self.log_file, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
            "Content-Disposition",
            f"attachment; filename= {self.log_file}",
            )
            complete_message.attach(part)
            text = complete_message.as_string()

            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
                server.login(self.sender_adress, self.password)
                server.sendmail(self.sender_adress, self.receiver_adress, text)
            line = ("[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Mail sent to "
            + self.receiver_adress)
            print(line)
            add_to_log(self.log_file, line)
        except smtplib.SMTPSenderRefused:
            line_one = "[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Sender adress refused"
            print(line_one)
            add_to_log(self.log_file, line_one)
        except smtplib.SMTPRecipientsRefused:
            line_two = "[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Receiver adress refused"
            print(line_two)
            add_to_log(self.log_file, line_two)
        except smtplib.SMTPConnectError:
            line_three = ("[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Connection with " +
            "server failed")
            print(line_three)
            add_to_log(self.log_file, line_three)
        except smtplib.SMTPAuthenticationError:
            line_four = ("[" + DATE + " | " + TIME +  "]" + " [EMAIL]: Wrong username or " +
            "password")
            print(line_four)
            add_to_log(self.log_file, line_four)
