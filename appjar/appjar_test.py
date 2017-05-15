# import the library
from appJar import gui

# top slice - CREATE the GUI
app = gui()

### fillings go here ###
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")

# bottom slice - START the GUI
app.go()