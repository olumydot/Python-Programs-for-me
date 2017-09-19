from tkinter import *  #import all definition from tinker

new_window = Tk() #creates a new window called "new_window"

new_label = Label(new_window, text = "Welcome to GUI lessons in Python") #creates the new label

new_button = Button(new_window, text = "Close this window") #creates the new window

new_label["justify"] = LEFT

new_label["cursor"] = "plus"

new_label["text"] = "Welcome to GUI lessons with Tkinter in Python"

new_label.pack() #put the newly created label in the window

new_button.pack() #place it in the window


new_window.mainloop() #create and event loop


from tkinter import *  #import all definition from tinker# Import all definitions from tkinter


def processOK():
    print("OK button is clicked")


def processCancel():
    print("Cancel button is clicked")



window = Tk() # Create a window

btOK = Button(window, text = "OK", fg = "red", bg = "blue", command = processOK) #means when button is pressed then processOK is executed. fg is foreground

btCancel = Button(window, text = "Cancel", bg = "yellow",command = processCancel) #background color of the button is yellow "bg". First arguement is always the parent container. in this case window


btOK.pack() # Place the OK button in the window

btCancel.pack() # Place the Cancel button in the window


window.mainloop()# Create an event loop


# to change the widget property you use thie:
#widgetName["propertyName"] = newPropertyValue
#for example:

#new_label["justify"] = LEFT
#new_label["text"] = "Welcome to GUI lessons with Tkinter in Python"