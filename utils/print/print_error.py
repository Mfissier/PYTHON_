import traceback
import sys

from termcolor import colored

def print_error(text):
#
    if (text):
    #
        sys.stderr.write(
            colored("Error : " + text + "\n", 'red'))
        sys.stderr.write("\033[91m")
        traceback.print_exc()
        sys.stderr.write("\033[0m\n")
    #
#

# #
# Allows you to write a custom error, while adding the exact path and line of the error
# #