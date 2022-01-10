"""
    Class SmbClient
"""

import json
import time
import os
import shutil

from smb.SMBConnection import SMBConnection

class SmbClient:
    """
    Class SmbClient
    Contains methods handling SMB server connection and upload
    """

    def __init__(self, config_file):
        """
        Attributes :
        --> username : Current session username
        --> password : Current session password
        --> machine_name : Arbitrary string
        --> server_name : Name of the computer
        --> ip : IP
        --> smb_share : Name of the samba folder share
        --> save_duration : Duration (in seconds) for which files are stored
        """
        with open(config_file, encoding="utf8") as conf:
            data = json.load(conf)
            smb_client = data["smb_client"]
        self.username = smb_client["username"]
        self.password = smb_client["password"]
        self.machine_name = smb_client["machine_name"]
        self.server_name = smb_client["server_name"]
        self.ip_adress = smb_client["ip_adress"]
        self.smb_share = smb_client["smb_share"]
        self.save_duration = smb_client["save_duration"]

    def upload(self, file_to_store, data):
        """
        Function allowing user to send a file to an SMB server
        --> file_to_store : File to store in SMB server
        --> data : data when using open
        """
        con = SMBConnection(self.username, self.password, self.machine_name,
        self.server_name, use_ntlm_v2 = True)
        con.connect(self.ip_adress, 139)
        file = "/" + file_to_store
        con.storeFile(self.smb_share, file, data)

    def delete(self):
        """
        Function allowing user to delete a files in SMB server
        """
        now = time.time()
        folder = "./" + self.smb_share + "/"
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if (now - os.path.getmtime(folder + filename)) > self.save_duration:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
