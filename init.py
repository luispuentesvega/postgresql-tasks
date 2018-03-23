from ftplib import FTP
import sys


#1.Downloading backups conecting FTP
#Location: demo.wftpserver.com
#Username: demo-user
#Password: demo-user
#FTP Port: 21

server = 'ftp.dlptest.com'
username = 'dlpuser@dlptest.com'
password = 'eiTqR7EMZD5zy7M'
port = '21'

#Connection FTP
ftp = FTP(server)
ftp.login(username, password)
#ftp.cwd('download')
ftp.retrlines('LIST')
ftp.retrbinary('RETR db_test.backup', open('db_test.backup', 'wb').write)
ftp.quit()