"""
    Script allowing user to handle log file
"""

import datetime
import os

DATE = datetime.datetime.now().date().strftime("%Y%d%m")
TIME = datetime.datetime.now().strftime("%H:%M:%S")

def add_to_log(file, line):
    """
    Function adding text to log.txt
    """
    with open(file, 'a+', encoding="utf8") as filename:
        filename.seek(0)
        data = filename.read(100)
        if len(data) > 0 :
            filename.write("\n")
        filename.write(line)

def clear_log(file):
    """
    Function clearing log.txt
    """
    with open(file, 'w', encoding="utf8") as filename:
        filename.close()

def delete_log(file):
    """
    Function deleting log.txt
    """
    try:
        os.remove(file)
    except OSError:
        line = "[" + DATE + " | " + TIME +  "]" + " [CLEAN]: " + file + " does not exist"
        print(line)

def read_log(file):
    """
    Function returning the content from log.txt
    """
    with open(file, 'r', encoding="utf8") as filename:
        data = filename.read()
    return data

def read_log_first_line(file):
    """
    Function returning "Successful" or "Unsuccessful" depending on first line
    """
    status=""
    with open(file, 'r', encoding="utf8") as filename:
        firstline = filename.readline().rstrip()
        if firstline == ("[" + DATE + " | " + TIME +  "]" + " [DOWNLOAD]: data_zip.zip downloaded"):
            status = "Operation : Success"
        else:
            status = "Operation : Failure"
    return status
