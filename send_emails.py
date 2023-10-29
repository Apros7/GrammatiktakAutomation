import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
recipient_email = "recipient@example.com"
subject = "Daily Report"
message = "This is your daily report."

def send_email():
    # Create an SMTP session
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Log in to your email account
    server.login(sender_email, sender_password)

    # Create the message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Terminate the SMTP session
    server.quit()

# Schedule the email to be sent daily
schedule.every().day.at("08:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
