"""
This function is for writing the text format email into a certain directory
Thus we could upload it to the Zong Diao platform

* Subject: The original email subject
* Body: The body of the email
"""

import re
import os
from datetime import datetime

now = datetime.now()
year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute

# Current dir
current_path = os.getcwd()

# Form output dir (We want all of this result to be print to output)
output_dir = os.path.join(current_path, 'Output')

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Get into the output dir
os.chdir(output_dir)


def write_textMail(Body, Subject):

    # Sanitize filename to remove invalid characters for Windows
    def sanitize_filename(filename):
        # Remove invalid characters such as \ / : * ? " < > | and \t (tab)
        filename = re.sub(r'[\/:*?"<>|\t]', '', filename)
        # Replace multiple spaces with a single space
        filename = re.sub(r'\s+', ' ', filename)
        return filename.strip()

    # Create dir
    # If dir not exist, create the dir
    dir_name = f"Email_Dir_{year}-{month}-{day}"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    # Sanitize the filename to avoid invalid characters
    filename = sanitize_filename(Subject)
    file_path = os.path.join(dir_name, filename)

    # Every single email will write one single email to the directory
    with open(file_path, 'w', encoding='utf-8') as file:
        # file.write(f"Subject: {subject}\n")
        # file.write(f"Sender: {sender}\n")
        # file.write("\n--- Email Body ---\n\n")
        file.write(Body)

    print(f"Email saved to {filename}")

###
# TESTING
###
if __name__ == "__main__":

    # Current dir
    current_path = os.getcwd()

    # Upper dir
    parent_dir = os.path.dirname(current_path)

    # Form output dir (We want all of this result to be print to output)
    output_dir = os.path.join(parent_dir, 'Output')

    # Get into the output dir
    os.chdir(output_dir)

    textMail = write_textMail("a", "b")