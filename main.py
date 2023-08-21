from utils.files.check_update_file import check_update_file
from utils.files.find_file import find_file
from utils.print.print_error import print_error
import time

def main() :
#
    print('here for test')
    print(check_update_file('main.py'))
    time.sleep(4)
    print(check_update_file('main.py'))
#

if __name__ == "__main__":
    main()