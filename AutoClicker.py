# Basic original code taken from GeeksForGeeks https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/
# Heavily modified to my specific use case with optional command-line arguments

import sys
import time
import threading
from pynput.mouse import Button, Controller     # Needed for clicking buttons (left, right, or middle) on mouse
from pynput.keyboard import Listener, KeyCode   # Needed for start, stop, and exit keys from keyboard


# Stores number of arguments into one parameter so len() doesnt have to be called numerous times
argslength = len(sys.argv)

# Will give too many arguments message if too many command-line arguments are given
if argslength > 6:
        print ("Maximum of 5 valid command-line arguments: [seconds_delay] [mouse_button] [start_key] [stop_key] [exit_key]")
        input ("Number of command-line arguments provided: " + str(argslength - 1))
        exit()
      
# Standard parameters used in program without command-line arguments  
delay = 0.001
button = Button.left
start_key = KeyCode(char='-')
stop_key = KeyCode(char='=')
exit_key = KeyCode(char='\\')
    
# Use command-line arguments for parameters if given
# Uses various error-checks for each parameter
if argslength >= 2:
    # Will give error message if input delay is not a valid number
    try:
        delay = float(sys.argv[1])
    except:
        print ("Input error: First parameter [seconds_delay] must be a valid number.")
        input ("Invalid parameter given: '" + sys.argv[1] + "'")
        exit()
    
    if argslength >= 3:   
        inputmousebutton = sys.argv[2].lower()
        if inputmousebutton == "left":
                button = Button.left      
        elif inputmousebutton == "right":
                button = Button.right
        elif inputmousebutton == "middle":
                button = Button.middle
            
        # Will give error message if input mouse button is not 'left', 'right', or 'middle'
        if inputmousebutton != "left" and inputmousebutton != "right" and inputmousebutton != "middle":
            print ("Input error: Second parameter [mouse_button] parameter must be 'left', 'right', or 'middle'.")
            input ("Invalid parameter given: '" + sys.argv[2] + "'")
            exit()
            
        if argslength >= 4:  
            # Will give error message if input start_key button is not a valid keyboard key
            try: 
                start_key = KeyCode(char=sys.argv[3].lower())
            except:
                print ("Input error: Third parameter [start_key] must be a valid keyboard key.")
                input ("Invalid parameter given: '" + sys.argv[3] + "'")
                exit()
            
            if argslength >= 5: 
                # Will give error message if input stop_key button is not a valid keyboard key
                try:
                    stop_key = KeyCode(char=sys.argv[4].lower())
                except:
                    print ("Input error: Fourth parameter [stop_key] must be a valid keyboard key.")
                    input ("Invalid parameter given: '" + sys.argv[4] + "'")
                    exit()
                
                if argslength >= 6:  
                    # Will give error message if input exit_key button is not a valid keyboard key
                    try:
                        exit_key = KeyCode(char=sys.argv[5].lower())
                    except:
                        print ("Input error: Fifth parameter [exit_key] must be a valid keyboard key.")
                        input ("Invalid parameter given: '" + sys.argv[5] + "'")
                        exit()
  
# Threaded class for controlling mouse clicks
class ClickMouse(threading.Thread):
    
    #Class is defined with input delay and selected mouse button
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    # Method for starting auto-clicking
    def start_clicking(self):
        self.running = True

    # Method for stopping auto-clicking
    def stop_clicking(self):
        self.running = False

    # Method for exiting program auto-clicking
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # Method for running loops that execute auto-clicking
    def run(self):
        # Loop keeps program running until 'exit_key' pressed and causes program_running to be False
        while self.program_running:
            # Loop will only execute after 'start_key' pressed and causes 'running' parameter to be True
            # Loop will stop executing if 'stop_key' pressed and causes 'running' parameter to be False
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


# Threaded class instance and controller
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


# Method for executing code if the start, stop, or exit key is pressed
def on_keypress(key):

    # Starts auto-clicking if not already auto-clicking and 'start_key' pressed
    if key == start_key:
        if click_thread.running == False:
            click_thread.start_clicking()
    
    # Stops auto-clicking if already auto-clicking and 'stop_key' pressed
    elif key == stop_key:
        if click_thread.running == True:
            click_thread.stop_clicking()
    
    # Ends program entirely if 'exit_key' pressed
    elif key == exit_key:  
        if click_thread.running == True:
            click_thread.stop_clicking()  
        click_thread.exit()
        listener.stop()


# Listens for start, stop, or exit keys to be pressed
with Listener(on_press=on_keypress) as listener:
    listener.join()