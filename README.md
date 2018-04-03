# postgresql-tasks
🕗 Automatization to download, check and send an email if postgresql is making backups correctly
## Process
1. Connect FTP for downloading backups
2. Restore whole backups
3. Notify via email

## Requisites
1. Python 3.*
2. Another

## Install & Configuration Process
1. Install the next Python's libraries
2. Configurate file  config.json [1.Account FTP 2.Postresql Local 3.Emails]
3. Execute py main.py
