start py C:\Path\To\Script\Server\server.py
schtasks /create /sc daily /st 00:00 /tn "Archiving Tool" /tr C:\Path\To\Script\main.py
