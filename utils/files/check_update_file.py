import os
import datetime

from utils.files.find_file import find_file
from utils.print.print_error import print_error


class file :
    rec_time = 0
    new_time = 0

    @staticmethod
    def get_rec_time() :
        return(file.rec_time)

    @staticmethod
    def change_rec_time(time) :
        file.rec_time = time
        return (time)
    @staticmethod
    def get_new_time() :
        return(file.new_time)

    @staticmethod
    def change_new_time(time) :
        file.new_time = time
        return (time)





def files_time_modified(filepath):
#
    try :
    #
        timestamp = os.path.getmtime(filepath)
        file_mod_date = datetime.datetime.fromtimestamp(timestamp)
        return (file_mod_date)
    #
    except :
        return (None)
#

def check_update_file(filename) :
#
    rec_time = 0
    new_time = 0
    tmp_time = 0
    path = find_file(filename)

    if (not path) :
        return (None)
    else :
    #
        tmp_time = files_time_modified(path)
        if (not tmp_time) :
            return (None)
        rec_time = file.get_rec_time()
        new_time = file.get_new_time()
        if (rec_time == 0) :
        #
            rec_time = file.change_rec_time(tmp_time)
            return (0)
        #
        else :
        #
            new_time = file.change_new_time(tmp_time)
            if (not (new_time == rec_time)) :
            #
                rec_time = file.change_rec_time(tmp_time)
                return (1)
            #
            else :
                return (0)
        #
    #
#

# #
# This function must be called once to instantiate its static variables.
# [1] if the file has been modified
# [0] if nothing happened
# [None] if there was an error.
# > #
# check_update_file('main.py') 
#  \ 1 init variable static
# if (check_update_file('main.py')) 
#  \ 2  Check if file is update
# < #