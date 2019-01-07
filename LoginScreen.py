from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

import time


# Declare both screens
class LoginScreen(Screen):
    message = StringProperty()

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

    def submit(self):
        self.message = 'lol %s ' % self.f_username.text
        time.sleep(1)
        self.manager.current = 'lobby'
        self.manager.gm.username = self.f_username.text