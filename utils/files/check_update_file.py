import os
import datetime

from utils.files.find_file import find_file
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

class file :
#
    """class static for save status of file check"""
    rec_time = 0
    new_time = 0

    @staticmethod
    def get_rec_time() :
        """Change var file.rec_time"""
        return file.rec_time

    @staticmethod
    def change_rec_time(time) :
    #
        """Change var file.rec_time"""
        file.rec_time = time
        return time
    #

    @staticmethod
    def get_new_time() :
        """Get file.new_time"""
        return(file.new_time)

    @staticmethod
    def change_new_time(time) :
    #
        """Get file.new_time"""
        file.new_time = time
        return (time)
    #
#

def files_time_modified(filepath):
#
    """take_time when the file is modify"""
    try :
    #
        timestamp = os.path.getmtime(filepath)
        file_mod_date = datetime.datetime.fromtimestamp(timestamp)
        return (file_mod_date)
    #
    except : # pylint: disable=bare-except
        return None
#

def check_update_file(filename, mode_dev = False) :
#
    """
        The first call to this function is just to initialize a record. 
        The next calls will tell if the named file has had a change
        ex :
        1/ check_update_file("main.py") (init)
        2/ check_update_file("main.py") (check)
        this function return (1): if main.py is modify
    """
    if mode_dev :
        print_blue('Fun : check_update_file()')
    path = find_file(filename)
    if not path :
    #
        if mode_dev :
            print_red("The path does not exist !")
        return None
    #
    else :
    #
        tmp_time = files_time_modified(path)
        if not tmp_time :
            return None
        rec_time = file.get_rec_time()
        new_time = file.get_new_time()
        if not rec_time :
        #
            if mode_dev :
                print_yellow('First time call. Register file time...')
                print_blue('------------------------')
            rec_time = file.change_rec_time(tmp_time)
            return 0
        #
        else :
        #
            new_time = file.change_new_time(tmp_time)
            if new_time != rec_time :
            #
                rec_time = file.change_rec_time(tmp_time)
                if mode_dev :
                    print_green('The file has been modified')
                    print_blue('------------------------')
                return 1
            #
            else :
                if mode_dev :
                    print_green('Result : The file has not been modified')
                    print_blue('------------------------')
                return 0
        #
    #
#

# #
# This function must be called once to instantiate its static variables.
# [1] if the file has been modified # [0] if nothing happened # [None] if there was an error.
# #