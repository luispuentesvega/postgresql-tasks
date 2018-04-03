import logging
import datetime
import tarfile
import re
import ntpath
import os
import shutil

class util():
    def create_log(str):
        logging.basicConfig(filename='logs/log' + datetime.datetime.now().strftime("%Y%m%d") + '.log',
                            format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p', level=logging.DEBUG)
        logging.debug(str)

    def extract_file(file, path):
        tar = tarfile.open(file)
        response = tar.extractall(path)
        tar.close()
        return response

    def explode_string_by_simbol(name, simbol='_'):
        words = re.split(simbol, name)
        doclist = []
        for word in words:
            doclist.append(word)
        return doclist

    def path_leaf(path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def get_file_name_with_type(name):
        file = os.path.splitext(name)
        return [file[0], file[1].replace('.', '')]

    def get_specific_files_from_directory(directory, type):
        arr_files = []
        for r, d, f in os.walk(directory):
            for files in f:
                if type in files:
                    arr_files.append(os.path.join(r, files))
        return arr_files

    def delete_files_from_directory(dirpath):
        print('Path %s'%dirpath)
        for filename in os.listdir(dirpath):
            print('Filename %s'%filename)
            filepath = os.path.join(dirpath, filename)
            try:
                shutil.rmtree(filepath)
            except OSError:
                os.remove(filepath)
