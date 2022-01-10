"""
    Main
"""

import json

from Modules.smb_client import SmbClient
from Modules.archive import Archive
from Modules.mail import Mail

CONFIG = "config.json"

client = SmbClient(CONFIG)
archive = Archive(CONFIG)
mail = Mail(CONFIG)

with open(CONFIG, encoding="utf8") as conf:
    data = json.load(conf)
    mail_json = data["mail"]

def main():
    """
    Main script of this project
    """
    body = ""
    subject=""

    archive.clear_log_file()
    archive.download_file()
    archive.extract_zip()
    archive.check_file()
    archive.create_tgz()
    archive.clean_zip()
    archive.clean_file()
    archive.send_tgz(client)
    archive.clean_tgz()
    archive.clean_server(client)
    body = archive.read_log_file()
    subject = archive.read_log_file_first_line()

    if mail_json["send_mode"] == "on":
        if mail_json["attach_mode"] == "on":
            mail.send_email_ssl_with_log(body, subject)
        else:
            mail.send_email_ssl(body, subject)

    archive.delete_log_file()

if __name__ == "__main__":
    main()
