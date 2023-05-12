# Code taken from GeeksForGeeks https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/
# Modified to my specific use case with command-line arguments

import sys
import time
import threading
from pynput.mouse import Button, Controller
  
# pynput.keyboard is used to watch events of 
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode
  
if len(sys.argv) != 1 and len(sys.argv) != 6:
        print ("Must have none or 5 arguments: [seconds delay] [mouse button] [start key] [stop key] [exit key]")
        print (len(sys.argv))
        exit()
      
#standard parameters used in program without command-line arguments  
if len(sys.argv) == 1:
    delay = 0.001
    button = Button.left
    start_key = KeyCode(char='-')
    stop_key = KeyCode(char='=')
    exit_key = KeyCode(char='\\')
    
#use command-line arguments for parameters if given
elif len(sys.argv) == 5:
    delay = int(sys.argv[1])
    
    if sys.argv[2] == "left":
        button = Button.left      
    elif sys.argv[2] == "right":
        button = Button.right
    elif sys.argv[2] == "middle":
        button = Button.middle
           
    start_key = KeyCode(char=sys.argv[3])
    stop_key = KeyCode(char=sys.argv[4])
    exit_key = KeyCode(char=sys.argv[5])
  
# threading.Thread is used 
# to control clicks
class ClickMouse(threading.Thread):
    
  # delay and button is passed in class 
  # to check execution of auto-clicker
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    # method to check and run loop until 
    # it is true another loop will check 
    # if it is set to true or not, 
    # for mouse click it set to button 
    # and delay.
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
  
  
# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()
  
  
# on_press method takes 
# key as argument
def on_press(key):
    
    # starts auto-clicking if not already auto-clicking
    if key == start_key:
        if click_thread.running == False:
            click_thread.start_clicking()
              
    #stops auto-clicking if already auto-clicking
    elif key == stop_key:
        if click_thread.running == True:
            click_thread.stop_clicking()
    
    #ends script entirely if 'exit_key' pressed
    elif key == exit_key:  
        if click_thread.running == True:
            click_thread.stop_clicking()  
        click_thread.exit()
        listener.stop()
  
# actualy start of executing code
with Listener(on_press=on_press) as listener:
    listener.join()