from utils.files.find_file import find_file
from utils.print.print_error import print_error

def main() :
#
    # find_file : 
    path = find_file('print_eror.py')
    if (not (path)) :
        print_error("This path does not exist !")
    else :
        print(path)
#

if __name__ == "__main__":
    main()