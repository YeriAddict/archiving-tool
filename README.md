# ArchivingTool - LEANG Denis

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#more-details">More details</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a>
      <ul>
        <li><a href="#how-to-json">A. How to configure the json file</a></li>
        <li><a href="#how-to-smb">B. How to create the SMB share server</a></li>
        <li><a href="#how-to-run">C. How to run the program periodically</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a simple archiving tool built with Python. This tool allows a user to do these successive actions periodically:

1. Download a zip file from a web server (HTTP)
2. Extract that zip file
3. Check whether its content is up to date and valid
4. Compress it after validation into a tgz file
5. Send the tgz file to a server (SMB/CIFS)
6. (Optional) Send an email stating if operation succeeded or not

A logfile stores useful information throughout the whole operations to check if everything works properly or not. It can be attached to the email if the user chooses to do so.

Here is a drawing to better understand the whole process : 

<img src="images/screen_one.png" alt="Logo" width="900" height="400">

### Built With

* [pylint](https://pypi.org/project/pylint/)
* [requests](https://pypi.org/project/requests/)
* [pysmb](https://pysmb.readthedocs.io/en/latest/)

### More details

You can check the folder "Documents" for more details on how the code is written and how to actually use the tool. 
This tool is mainly aimed at Windows workstations. Therefore, it may not work for MacOS or Linux users.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Clone the repository with SSH or HTTPS
   ```sh
   git clone git@github.com:YeriAddict/ArchivingTool.git
   ```
   ```sh
   git clone https://github.com/YeriAddict/ArchivingTool.git
   ```

### Installation

You will need to install these external libraries using pip. 
  ```sh
  py -m pip install pysmb 
  py -m pip install requests
  ```
  
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

You will need to complete these steps in order to successfully launch the tool. At the end, the task will be done periodically.

### A. How to configure the json file

To begin with, you will have to configure the config.json file cautiously. Here is a screenshot of what the file looks like : 

<img src="images/screen_json.png" alt="Logo" width="900" height="400">

The names of the json objects are conveniently named after the classes in the code. But all you must worry about as a user are the following elements. Changing the values in which “NO CHANGE” is specified is not advised:

➢ archive:  
  ▪ “url”: NO CHANGE  
  ▪ “zip_file”: NO CHANGE  
  ▪ “file”: NO CHANGE  
  ▪ “log_file”: Name of the generated log file  
  ▪ “expiring_time”: Duration (in seconds) after which a file is considered outdated  
  
➢ smb_client:  
  ▪ “username”: Current windows session username  
  ▪ “password”: Current windows session password  
  ▪ “machine_name”: Whatever name you want to enter  
  ▪ “server_name”: Name of the current PC  
  ▪ “ip_address”: IP address  
  ▪ “smb_share”: Name of the shared samba server (see after)  
  ▪ “save_duration”: Duration (in seconds) after which a file will be deleted in the smb server depending on its last modification date  
  
➢ archive:  
  ▪ “sender_address”: An E-mail address for the expeditor (Note: Gmail is advised)  
  ▪ “password”: Password for the adress above  
  ▪ “port”: NO CHANGE  
  ▪ “smtp_server”: NO CHANGE  
  ▪ “receiver_address”: An E-mail address for the receiver (Note: Gmail is advised)  
  ▪ “send_mode”: Put on or off depending on if you want to receive mails  
  ▪ “attach_mode”: Put on or off depending on if you want to have logs attached in the mails  

If you struggle finding how to fill "ip_address", follow these steps : 
1. Type **ipconfig** inside a terminal window
2. Get the correct IP address in front of IPv4

Finally, for the "sender_address", you should use a Gmail address. Having a throwaway Gmail address for the sender is advised for security reasons because you will have to enter login credentials inside the config.json to start the script. You must activate this mode: “Allow less secure apps” to on in Gmail. It is essential if you wish to receive the E-mails from the sender address as a receiver. To find this mode, go to :

➢ Settings → Security → Access to less secure apps  

### B. How to create the SMB share server

XXX

### C. How to run the program periodically

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

LEANG Denis - denis.leang@telecom-st-etienne.fr 

Link: [https://github.com/YeriAddict/ArchivingTool](https://github.com/YeriAddict/ArchivingTool)

<p align="right">(<a href="#top">back to top</a>)</p>
