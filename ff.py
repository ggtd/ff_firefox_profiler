#!/usr/bin/python
# -*- coding: utf-8 -*-

# ---- docs ----
#pip install curses-menu
#
#

import os
from cursesmenu import *
from cursesmenu.items import *

APP_USER_HOME=os.getenv("HOME")
APP_WORK_DIR=APP_USER_HOME+'/.ff_data'

try:
    os.mkdir(APP_WORK_DIR)
except:
    pass


def open_project(NAME):

    if NAME=="": NAME=raw_input("Name (new) project: ")
    if  NAME=="": return
    os.system("/Applications/Firefox.app/Contents/MacOS/firefox --profile "+str(APP_WORK_DIR)+'/'+str(NAME))


def menu():
    menu = CursesMenu("Browser Profile", "Select")
    function_item = FunctionItem("Call a Python function", input, ["Enter an input"])
    menu.append_item(FunctionItem("New Project", open_project, [""]))
    DIRS=os.listdir(APP_WORK_DIR)
    for data in DIRS:
        menu.append_item(FunctionItem(data, open_project, [str(data)]))

    menu.show()


menu()
