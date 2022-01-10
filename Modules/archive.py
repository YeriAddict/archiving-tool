"""
    Class Archive
"""

import time
import json
import os
import datetime
import zipfile
import tarfile
import requests

from smb.base import NotConnectedError
from Modules.log import add_to_log, clear_log, delete_log, read_log, read_log_first_line

DATE = datetime.datetime.now().date().strftime("%Y%d%m")
TIME = datetime.datetime.now().strftime("%H:%M:%S")

class Archive:
    """
    Class Archive
    Contains methods allowing user to download zip from URL,
    extracting zip, compressing and sending tgz to SMB server
    """

    def __init__(self, config_file):
        """
        Attributes :
        --> url : Web server's url (localhost)
        --> zip_file : Zip file name
        --> file : File name
        --> tgz_file : Tgz file name
        --> log_file : log file name
        --> expiring_time : Duration (in seconds) for which files are
        considered outdated
        """
        with open(config_file, encoding="utf8") as conf:
            data = json.load(conf)
            archive = data["archive"]
        self.url = archive["url"]
        self.zip_file = archive["zip_file"]
        self.file = archive["file"]
        self.tgz_file = DATE + ".tgz"
        self.log_file = archive["log_file"]
        self.expiring_time = archive["expiring_time"]

    def download_file(self):
        """
        Function allowing user to download file from URL
        """
        filename = (self.url+ self.zip_file).split('/')[-1]
        try:
            with requests.get(self.url + self.zip_file, stream=True) as request:
                request.raise_for_status()
                with open(filename, 'wb') as file:
                    for chunk in request.iter_content(chunk_size=8192):
                        file.write(chunk)
                file.close()
            line_one = ("[" + DATE + " | " + TIME +  "]" + " [DOWNLOAD]: " + filename
            + " downloaded")
            print(line_one)
            add_to_log(self.log_file, line_one)
        except requests.exceptions.ConnectionError:
            line_two = ("[" + DATE + " | " + TIME +  "]"
            + " [DOWNLOAD]: Web connection not established")
            print(line_two)
            add_to_log(self.log_file, line_two)
        except requests.exceptions.RequestException:
            line_three = ("[" + DATE + " | " + TIME +  "]" + " [DOWNLOAD]: "
            + filename + " not downloaded")
            print(line_three)
            add_to_log(self.log_file, line_three)
        return filename

    def extract_zip(self):
        """
        Function allowing user to extract zip
        """
        try:
            with zipfile.ZipFile(self.zip_file, 'r') as zip_ref:
                zip_ref.extractall()
                line_one = ("[" + DATE + " | " + TIME + "]" + " [EXTRACT]: " + self.zip_file
                + " extracted")
                print(line_one)
                add_to_log(self.log_file, line_one)
        except (IOError ,zipfile.BadZipfile):
            line_two = ("[" + DATE + " | " + TIME +  "]" + " [EXTRACT]: " + self.zip_file
            + " does not exist")
            print(line_two)
            add_to_log(self.log_file, line_two)

    def check_file(self):
        """
        Function checking if extracted file is new
        """
        now = time.time()
        try:
            if (now - os.path.getmtime("./" + self.file)) > self.expiring_time:
                line_one = ("[" + DATE + " | " + TIME +  "]" + " [CHECK]: " + self.file
                +" is outdated")
                print(line_one)
                add_to_log(self.log_file, line_one)
            else:
                line_two = ("[" + DATE + " | " + TIME +  "]" + " [CHECK]: " + self.file
                +" is up to date")
                print(line_two)
                add_to_log(self.log_file, line_two)
        except OSError:
            line_two = ("[" + DATE + " | " + TIME +  "]" + " [CHECK]: " + self.file
            + " does not exist")
            print(line_two)
            add_to_log(self.log_file, line_two)

    def create_tgz(self):
        """
        Function allowing user to extract zip
        """
        try:
            with tarfile.open(DATE + ".tgz", "w:gz") as compressed_file:
                compressed_file.add(self.file)
                compressed_file.close()
            compressed_file.close()
            line_one = ("[" + DATE + " | " + TIME +  "]" + " [COMPRESS]: " + self.file
            + " compressed")
            print(line_one)
            add_to_log(self.log_file, line_one)
        except IOError:
            line_two = ("[" + DATE + " | " + TIME +  "]" + " [COMPRESS]: " + self.file
            + " can not be compressed")
            print(line_two)
            add_to_log(self.log_file, line_two)
            os.remove(DATE + ".tgz")

    def send_tgz(self, client):
        """
        Function allowing user to send tgz file to an SMB share server
        --> client : Object from class SmbClient
        """
        file_to_store = DATE + ".tgz"
        try:
            try:
                with open(self.tgz_file, 'rb') as data:
                    client.upload(self.tgz_file, data)
                    line_one = ("[" + DATE + " | " + TIME +  "]" + " [UPLOAD]: " + file_to_store
                    + " sent to SMB")
                    print(line_one)
                    add_to_log(self.log_file, line_one)
                data.close()
            except OSError:
                line_two = ("[" + DATE + " | " + TIME +  "]" + " [UPLOAD]: " + file_to_store
                + " does not exist")
                print(line_two)
                add_to_log(self.log_file, line_two)
        except NotConnectedError:
            line_three = ("[" + DATE + " | " + TIME +  "]"
            + " [UPLOAD]: SMB connection not established")
            print(line_three)
            add_to_log(self.log_file, line_three)

    def clean_zip(self):
        """
        Function deleting the used files
        """
        try:
            os.remove(self.zip_file)
            line_one = ("[" + DATE + " | " + TIME +  "]" + " [CLEAN]: " + self.zip_file
            + " removed")
            print(line_one)
            add_to_log(self.log_file, line_one)
        except OSError:
            line_two = ("[" + DATE + " | " + TIME +  "]" + " [CLEAN]: " + self.zip_file
            + " does not exist")
            print(line_two)
            add_to_log(self.log_file, line_two)

    def clean_file(self):
        """
        Function deleting the used files
        """
        try:
            os.remove(self.file)
            line_one = ("[" + DATE + " | " + TIME +  "]" + " [CLEAN]: " + self.file
            + " removed")
            print(line_one)
            add_to_log(self.log_file, line_one)
        except OSError:
            line_two = ("[" + DATE + " | " + TIME +  "]" + " [CLEAN]: " + self.file
            + " does not exist")
            print(line_two)
            add_to_log(self.log_file, line_two)

    def clean_tgz(self):
        """
        Function deleting the used files
        """
        try:
            os.remove(self.tgz_file)
            line_one = ("[" + DATE + " | " + TIME +  "]" + " [CLEAN]: " + self.tgz_file
            + " removed")
            print(line_one)
            add_to_log(self.log_file, line_one)
        except OSError:
            line_two = ("[" + DATE + " | " + TIME +  "]" + " [CLEAN]: " + self.tgz_file
            + " does not exist")
            print(line_two)
            add_to_log(self.log_file, line_two)

    def clean_server(self, client):
        """
        Function clearing server from files with expired dates
        --> client : Object from class SmbClient
        """
        try:
            client.delete()
            line_one = ("[" + DATE + " | " + TIME +  "]" + " [CLEAN]: Outdated files removed")
            print(line_one)
            add_to_log(self.log_file, line_one)
        except OSError:
            line_two = ("[" + DATE + " | " + TIME +  "]" + " [CLEAN]: Outdated "
            + "files do not exist")
            print(line_two)
            add_to_log(self.log_file, line_two)

    def clear_log_file(self):
        """
        Function erasing log.txt
        """
        clear_log(self.log_file)

    def delete_log_file(self):
        """
        Function deleting log.txt
        """
        delete_log(self.log_file)

    def read_log_file(self):
        """
        Function reading log.txt and returning it as a variable
        """
        data = read_log(self.log_file)
        return data

    def read_log_file_first_line(self):
        """
        Function returning "Successful" or "Unsuccessful" depending on first line
        """
        return read_log_first_line(self.log_file)
