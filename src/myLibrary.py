#!/usr/bin/env python                                                                                
# -----------------------------------------------------------------------------------------                                                                        
#                              ____        ___                                           
#                              `MM'     68b MM                                           
#                               MM      Y89 MM                                           
#    ___  __    __  ____    ___ MM      ___ MM____  ___  __    ___   ___  __ ____    ___ 
#    `MM 6MMb  6MMb `MM(    )M' MM      `MM MMMMMMb `MM 6MM  6MMMMb  `MM 6MM `MM(    )M' 
#     MM69 `MM69 `Mb `Mb    d'  MM       MM MM'  `Mb MM69 " 8M'  `Mb  MM69 "  `Mb    d'  
#     MM'   MM'   MM  YM.  ,P   MM       MM MM    MM MM'        ,oMM  MM'      YM.  ,P   
#     MM    MM    MM   MM  M    MM       MM MM    MM MM     ,6MM9'MM  MM        MM  M    
#     MM    MM    MM   `Mbd'    MM       MM MM    MM MM     MM'   MM  MM        `Mbd'    
#     MM    MM    MM    YMP     MM    /  MM MM.  ,M9 MM     MM.  ,MM  MM         YMP     
#    _MM_  _MM_  _MM_    M     _MMMMMMM _MM_MYMMMM9 _MM_    `YMMM9'Yb_MM_         M      
#                       d'                                                       d'      
#                   (8),P                                                    (8),P       
#                    YMM                                                      YMM  
#    
# -----------------------------------------------------------------------------------------      

""" Library of My Functions.

This file contains function I've created to include in 
projects.
"""

__author__ = "Chuck Nelson"
__copyright__ = "Copyright 2024, myLibrary Project"
__credits__ = ["Chuck Nelson"]

__license__ = "MIT"
__maintainer__ = "Chuck Nelson"
__email__ = "chuck_nelson@hotmail.com"
__status__ = "Ongoing Development"

# Created Date: 09/03/2024
# Last Updated Date: 

import datetime, os, sys

# ==============================================
# ===             Functions                  ===
# ==============================================

# **************************************
# ***        General Functions       ***
# **************************************

def isBoolFromText(strValue):
    if strValue == "True": return True
    else: return False

# **************************************
# ***     Date / Time Functions      ***
# **************************************

def getTimeStamp():
    # Returns date in format: mm-dd-YYYY @ HH:MM::SS [AM/PM]
    dt = datetime.datetime.now()
    fullDate = f"{dt.strftime("%m")}/{dt.strftime("%d")}/{dt.strftime("%Y")}"
    time = f"{dt.strftime("%I")}:{dt.strftime("%M")}::{dt.strftime("%S")} "
    period = f"{dt.strftime("%p")}"
    TimeStamp = fullDate + " @ " + time + period
    return TimeStamp

def getTimeStampFile():
    # Returns date in format: mm-dd-YYYY_@_HH:MM—SS-[AM/PM]
    # This returns a stamp which can be used in a file name.
    dt = datetime.datetime.now()
    fullDate = f"{dt.strftime("%m")}-{dt.strftime("%d")}-{dt.strftime("%Y")}"
    time = f"{dt.strftime("%I")}-{dt.strftime("%M")}--{dt.strftime("%S")}-"
    period = f"{dt.strftime("%p")}"
    TimeStamp = fullDate + "_@_" + time + period
    return TimeStamp

# **************************************
# ***         File Functions         ***
# **************************************