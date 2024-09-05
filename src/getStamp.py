#!/usr/bin/env python  

""" Get Stamp.

This app will print to console a time stamp that can be 
cut and pasted into documents to display the date.

Uses: When updating code bases or documentation and you
would like to put in a time stamp for the changes
"""

__author__ = "Chuck Nelson"
__copyright__ = "Copyright 2024, myLibrary Project"
__credits__ = ["Chuck Nelson"]

__license__ = "MIT"
__maintainer__ = "Chuck Nelson"
__email__ = "chuck_nelson@hotmail.com"
__status__ = "Ongoing Development"

# Created Date: 09/04/2024
# Last Updated Date: 09/04/2024 @ 08:24::53 PM

# Imports
import sys
import myLibrary as ml

# Current command line argements:
#  => "display" or "Display"
#  => "file" or "File"

def main():
    # Get Passed in arguments
    result = getArgv()
    if not result: # No argument was given
        print(f"Missing Argument! Please try again.")
        printHelp()
    else:
        printStamp(result.lower())

def getArgv():
    try:
        argument = sys.argv[1]
    except IndexError:
        return False
    return argument

def printHelp():
    print("\n                getStamp Help                ")
    print("=============================================")
    print("  This app returns a date / time stamp ")
    print("  formatted for either display or for a file")
    print("  name.\n\n")
    print("     Command Line Arguments")
    print("         getStamp.py [display]")
    print("         getStamp.py [file]")
    print("\n\nEND HELP!\n\n")


def printStamp(strArgv):
    if strArgv == "display":
        print(f"\n\nDisplay Stamp: {ml.getTimeStamp()}\n\n")
    elif strArgv == "file":
        print(f"\n\nFile Stamp: {ml.getTimeStampFile()}\n\n")
    else:
        print(f"\n\nUnrecognized command line argument!\n\n")
        printHelp()

main()