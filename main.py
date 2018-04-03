from ftplib import FTP
import os
import datetime
import json
from random import *
from utils.connection_bd import *
from utils.util import *
"""
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from pydba import PostgresDB
"""
class main():
    #1
    def init_process(self):
        util.create_log('Starting process...')
        path = os.getcwd() + "\\backups\\" + datetime.datetime.now().strftime("%Y%m%d")
        if os.path.isdir(path):
            util.create_log('Deleting files existing folder %s'%path)
            util.delete_files_from_directory(path)
        else:
            os.makedirs(path, exist_ok=True)
            util.create_log('Creating Folder on %s'%path)
        #Creating folder with the current date
        with open('config.json') as json_data_file:
            util.create_log('Loading variables from config.json')
            return json.load(json_data_file)

    #2.Download the last file found for each folder
    def download_backups(self, config):
        arr_files = []
        ftp = FTP(config['server'])
        response = ftp.login(config['username'], config['password'])
        util.create_log('Connecting to FTP user('+config['username']+') : '+response)
        for folder in config['folders']:
            if folder in ftp.nlst():
                util.log('Exist folder %s on the FTP'%folder)
                filelist = []
                #To know if the directory exists
                ftp.cwd(folder)
                util.create_log('Moving to folder: '+folder)
                ftp.retrlines('LIST', filelist.append)
                for latest in filelist:
                    if latest.startswith("-") and "latest file pattern if any" in latest:
                        util.create_log('    Downloading file '+latest)
                        ftp.retrbinary('RETR '+latest, open(latest, 'wb').write)
                ftp.quit()
        return arr_files

    #3.Extracts files downloaded
    def extract_backups(self, arr_backups):
        for backup in arr_backups:
            extract_file(backup)

    #4.Restoring backups
    def restore_backups(self, arr_backups):
        for backup in arr_backups:
            file_name = path_leaf(backup)
            arr_file = get_file_name_with_type(file_name)
            arr_name = explode_by_simbol(arr_file[0],'_')
            #Creando la BD
            db = PostgresDB(user='postgres', password='postgres')
            rta = db.restore(arr_name[len(arr_name)-1], backup)
            if rta=='None':
                print('The backups has been restored succesfully')
            else:
                print('Error at the moment of restoring backup')

    #5.Notify by email
    #def notify_result_process(self):

main = main()
config = main.init_process()
print(config)
main.download_backups(config['ftp'])
#bd = connection_bd(db='test')
#all = bd.fetch_all(query='SELECT * FROM sales;');
#print(all)
#extract_file(os.getcwd()+'\\backups\\SitransBackups_20160615_0806.tar.gz', os.getcwd()+'\\backups')
#arr_backups = get_backups() -> get_specific_files_from_directory(os.getcwd() + '/backups', '.dump'):
#restore_backups(arr_backups)
#print(arr_backups)

"""
Other Option for FTP:
filelist = [] #to store all files
ftp.retrlines('LIST',filelist.append)    # append to list  
"""