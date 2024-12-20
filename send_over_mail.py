import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import re
from datetime import datetime

# Function to send email with attachments
def send_email_with_attachments(smtp_server, port, sender_email, sender_password, recipient_list, subject, body, files):
    """Send an email with attachments."""
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)

        for recipient in recipient_list:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject

            # Email body
            msg.attach(MIMEText(body, 'plain'))

            # Attach files
            for file in files:
                with open(file, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file)}')
                msg.attach(part)

            # Send the email
            server.send_message(msg)
            print(f"Email sent to {recipient}")

        # Close the SMTP server
        server.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

# Function to get files with current date appended
def get_files_with_date(folder, base_files):
    """Get the file names with the current date appended."""
    current_date = datetime.now().strftime("%Y%m%d")
    files_with_date = []
    for base_file in base_files:
        pattern = f"{current_date}_(.+)"
        for file in os.listdir(folder):
            if re.match(pattern, file) and base_file in file:
                files_with_date.append(os.path.join(folder, file))
    return files_with_date

# Configuration
FOLDER_PATH = "reports"
BASE_FILES = ["report1.csv", "report2.csv"]
FILES_TO_SEND = get_files_with_date(FOLDER_PATH, BASE_FILES)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "chaudharyvikash2012@gmail.com"
SENDER_PASSWORD = "dgihpqsinyxurnbw"
RECIPIENT_LIST = ["vikash91120@gmail.com.com", "vikash91120@gmail.com"]
SUBJECT = "Updated Files from Repo"
BODY = "Please find the attached updated files from the repository."

# Check if files are found
if FILES_TO_SEND:
    # Send email with the files
    send_email_with_attachments(
        SMTP_SERVER,
        SMTP_PORT,
        SENDER_EMAIL,
        SENDER_PASSWORD,
        RECIPIENT_LIST,
        SUBJECT,
        BODY,
        FILES_TO_SEND
    )
else:
    print("No files found with the current date.")