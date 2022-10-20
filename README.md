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
        <li><a href="#how-to-run">How to run</a></li>
        <li><a href="#how-to-use">How to use</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a simple archiving tool built with Python. This tool allows a user to do these successive actions:

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
<p align="right">(<a href="#top">back to top</a>)</p>

### Installation

You will need to install these external libraries using pip. 
  ```sh
  py -m pip install pysmb 
  py -m pip install requests
  ```

<!-- USAGE EXAMPLES -->
## Usage

### How to run

XXX

### How to use

XXX

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

LEANG Denis - denis.leang@telecom-st-etienne.fr 

Link: [https://github.com/YeriAddict/ArchivingTool](https://github.com/YeriAddict/ArchivingTool)

<p align="right">(<a href="#top">back to top</a>)</p>
