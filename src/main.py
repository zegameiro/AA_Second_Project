from getopt import GetoptError, getopt
from constants import STUDENT_NUMBER, EDGES_PERCENTAGE, GRAPHS

import sys
import random
import os
import time

def main(argv):

    folder = ""

    try:
        opts, args = getopt(argv, "hf:", ["folder="])
    except GetoptError:
        print("main.py -f <path_to_folder>")
        sys.exit(2)

    for opt, arg in opts:

        if opt == "-h":
            print("main.py -f <path_to_folder>")
            sys.exit()
        
        elif opt in ("-f", "--folder"):
            folder = arg

    if folder == "":
        print("Please provide a valid folder path.")
        sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])


