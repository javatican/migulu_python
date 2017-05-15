#!/usr/bin/python3
# import the library
from appJar import gui

# top slice - CREATE the GUI
app = gui()

def press(btn):
    items = app.getListItems("list")
    if len(items)> 0:
        app.removeListItem("list", items[0])


app.addListBox("list", ["apple", "orange", "pear", "kiwi"])
#setListBoxMulti("list",multi=True) #多選, 否則單選
app.addButton("press",  press)

# bottom slice - START the GUI
app.go()