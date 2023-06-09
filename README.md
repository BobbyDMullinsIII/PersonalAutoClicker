# PersonalAutoClicker
Repository for an auto clicker that I made in Python3.

Python3 and the pynput library must be installed to run this program.<br>
(Tested with specifically Python 3.11.3 and pynput 1.7.6)

In order to run, either double click on the 'AutoClicker.py' file, or input one of these in a cmd within the same folder.<br>
(Not all of these may work, depending on your Python3 installation)

***./AutoClicker.py*** <br>
***python3 AutoClicker.py*** <br>
***py AutoClicker.py*** <br>
<br>
<br>
<br>
Program optional command-line arguments (In this order):

***[seconds_delay]*** - Number of seconds between each delay. (Must be full or decimal number, ***Default: '0.001'***)

***[mouse_button]*** - Mouse button to auto-click. (Must be 'left', 'right', or 'middle', ***Default: 'left'***)

***[start_key]\**** - Key to start auto-clicking. (Must be valid keyboard key, ***Default: '-'***)

***[stop_key]\**** - Key to stop auto-clicking. (Must be valid keyboard key, ***Default: '='***)

***[exit_key]*** - Key to fully exit auto-clicker program. (Must be valid keyboard key, ***Default: '\\'***)

\**[start_key]* and *[stop_key]* can be the same key.
<br>
<br>
<br>
Example run command with command-argument order:

***py AutoClicker.py [seconds_delay] [mouse_button] [start_key] [stop_key] [exit_key]*** <br>
<br>
Run command with all example command-line arguments:

***py AutoClicker.py 0.001 left - = \\*** <br>
<br>
Run command with only 2 example command-line arguments:

***py AutoClicker.py 0.001 left*** <br>
