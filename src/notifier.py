from pynotifier import Notification
import time, pathlib
import requests
from discord import SyncWebhook


def __always_true():
    return True

class Notifier:
    def __always_true():
        return True

    def __init__(self, title: str, info: str, state = __always_true):
        self.title, self.info = title, info
        self.status_check = state

    def send(self):
        dir = pathlib.Path(__file__).parent.absolute().as_posix() + '/grouch.ico'
        notif = Notification(
            title=self.title,
            description=self.info,
            icon_path=dir,
            duration=7,
            urgency=Notification.URGENCY_CRITICAL
        )
        
        notif.send()
        file = open("webhook.txt", "r") #store webhook URL in webhook.txt, placeholder is present
        url = file.read()
        file.close()
        webhook = SyncWebhook.from_url(url)
        message = ("%s \n %s \n" % (self.title, self.info))
        webhook.send(content=message) #just placed here so it sends when system notification sends
        time.sleep(7)

    def run(self):
        while not self.status_check():
            continue
        self.send()

    def run_async(self):
        if self.status_check():
            self.send()

    def run_force(self):
        self.send()
