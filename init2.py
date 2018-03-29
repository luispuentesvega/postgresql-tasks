from ftplib import FTP
import logging
import datetime
import json
import datetime
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from random import *

#1
def init_process():
    #Creating folder with the current date
    
    with open('config.json') as json_data_file:
        create_log('Loading variables')
        return json.load(json_data_file)

#2
def create_log(str):
    logging.basicConfig(filename='log' + datetime.datetime.now().strftime("%Y%m%d") + '.log',
                        format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p', level=logging.DEBUG)
    logging.debug(str)

#3.Download the last file found for each folder
def download_backups(config):
    arr_files = []
    ftp = FTP(config['server'])
    response = ftp.login(config['username'], config['password'])
    create_log('Connecting to FTP user('+config['username']+') : '+response)
    for folder in config['folders']:
        filelist = []
        ftp.cwd(folder)
        create_log('Moving to folder: '+folder)
        ftp.retrlines('LIST', filelist.append)
        for latest in filelist:
            if latest.startswith("-") and "latest file pattern if any" in latest:
                create_log('    Downloading file '+latest)
                ftp.retrbinary('RETR '+latest, open(latest, 'wb').write)
        ftp.quit()
    return arr_files

#4.Unzipping folder


config = init_process()
download_backups(config['ftp'])
