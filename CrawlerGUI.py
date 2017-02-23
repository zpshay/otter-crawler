##################################################################
# CrawlerGUI.py                                                  #
# Written by ARN                                                 #
#                                                                #
# When run, will produce a GUI with a JSON file's contents       #
##################################################################


#!/usr/bin/python3

import json

from tkinter import *


# Code that adds widgets

root = Tk()
root.geometry("1000x500")

resultsDisplay = Text(root)
resultsDisplay.pack(side = LEFT, fill = BOTH, expand = YES)

scrollbar = Scrollbar(root, orient = VERTICAL, command = resultsDisplay.yview)
scrollbar.pack(side = RIGHT, fill = Y)

resultsDisplay.insert(INSERT, "Here is your JSON\n\n")


#Code to read and display JSON
#Changing the file in this code will change the file that will be read

with open("video.json") as json_file:
    json_data = json.load(json_file)
    for item in json_data:
        resultsDisplay.insert(INSERT, item)
        resultsDisplay.insert(INSERT, '\n')

