"""
    All main fun for print color in terminal
"""
import sys
from termcolor import colored

def print_red(txt) :
#
    """
        for print txt in red
    """
    if txt :
        sys.stderr.write(colored(txt + '\n', 'red'))
        
#

def print_blue(txt) :
#
    """
        for print txt in blue
    """
    if txt :
        print(colored(txt, 'blue'))
#

def print_green(txt) :
#
    """
        for print txt in green
    """
    if txt :
        print(colored(txt, 'green'))
#

def print_yellow(txt) :
#
    """
        for print txt in yellow
    """
    if txt :
        print(colored(txt, 'yellow'))
#